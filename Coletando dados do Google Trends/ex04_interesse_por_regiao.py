"""
Interesses por Região

Objetivo:
    Coletar e tratar dados de interesse relativo por região utilizando a biblioteca trendspyg.


Autor:
    Wellington M Santos
"""

# BIBLIOTECAS #
from trendspyg              import download_google_trends_explore
from trendspyg.exceptions   import DownloadError, BrowserError
import pandas as pd
from loguru import logger

# CONFIGURAÇÕES #   
DEFAULT_GEO = 'BR'
DEFAULT_TIMEFRAME = 'today 12-m'

# FUNÇÕES #
def get_interest_by_region(keyword:str, geo:str, timeframe:str) -> pd.DataFrame:
    """
    Retorna o interesse relativo por região para uma palavra chave.

    Args:
        - keyword: palavra-chave pesquisada
        - geo: codigo do país ISO
        - timeframe: intervalo da pesquisa

    Returns:
        pd.DataFrame 
    """
    try:
        logger.info(f'Coletando dados para palavra-chave: {keyword}')
        data = download_google_trends_explore(
                    keyword=keyword,
                    geo=geo,
                    timeframe=timeframe,
                )

        logger.info('Dados coletados com sucesso')
        if data and data.get('interest_by_region'):
            df = pd.DataFrame(data['interest_by_region'])
            return df

        return pd.DataFrame()


    except DownloadError as e:
        raise RuntimeError("Google Trends limitou a consulta temporariamente") from e
    except BrowserError as e:
        raise RuntimeError('Google Trends mudou a página, atualize o trendspyg ou tente novamente mais tarde.') from e
    except Exception as e:
        raise RuntimeError(f"Erro ao consultar o Google Trends: {e}") from e

def padronizar_dados(data:pd.DataFrame, br:bool=True) -> pd.DataFrame:
    """
    Renomeia as colunas com tratamento extra para dados do Brasil.

    Args:
        - data: pd.DataFrame com trendspyg.download_google_trends_explore chave 'interest_by_region'
        - br: se True retira dos dados 'State of ', renomeia 'Federal District' para 'Distrito Federal' e cria coluna 'uf'
    Returns:
        pd.DataFrame
    """
    if data.empty:
        logger.warning('Sem dados.')
        return data.copy()
    
    logger.info('Preparando dados coletados')
    df = data.copy()
    df = df.rename(columns={'geo_code' : 'codigo',
                            'geo_name' : 'estado', 
                            'value'    : 'indice'})
    if br:
        logger.info('Preparando dados para padrão BR')
        df['estado'] = (df['estado']
                        .str.replace('State of ','', regex=False)
                        .str.replace('Federal District', 'Distrito Federal', regex=False))
        df['uf'] = df['codigo'].str[-2:]
        df.drop(columns=['codigo'], inplace=True)
        df = df[['uf', 'estado', 'indice']]

    return df


# MAIN #
def main():
    dados = get_interest_by_region(keyword='python', geo=DEFAULT_GEO, timeframe=DEFAULT_TIMEFRAME)
    dados = padronizar_dados(dados)
    if dados.empty:
        logger.warning('Não há dados.')
        return
    print(dados)

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10,6))
    plt.barh(dados['estado'], dados['indice'])
    plt.gca().invert_yaxis()
    plt.title('Interesse Relativo por Estado')
    plt.xlabel('Índice de interesse relativo')
    plt.ylabel('Estado')
    plt.figtext(.99, .01, 'Fonte dos dados: Google Trends (trendspyg)', ha='right', fontsize=8, color='gray')
    plt.grid(alpha=.4)
    plt.tight_layout()
    plt.savefig('interesse relativo por estado.png')


if __name__ == '__main__':
    main()