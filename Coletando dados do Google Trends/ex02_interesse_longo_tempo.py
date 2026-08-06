import pandas as pd
from trendspyg import download_google_trends_interest_over_time

DEFAULT_TIMEFRAME   = 'today_12-m'
DEFAULT_GEO         = 'BR'

def get_interest_over_time(keyword:str, geo:str, timeframe:str) -> pd.DataFrame:
    """
    Retorna o interesse ao longo do tempo para uma palavra-chave.
    
        Args:
            - keyword: str  - palavra chave pesquisada.
            - geo: str      - codigo do país 
            - timeframe:str - intervalo do google trends
        
        Returns pandas.DataFrame
    
    """
    try:
        dados = download_google_trends_interest_over_time(
            keyword=keyword,
            geo=DEFAULT_GEO,
            timeframe=DEFAULT_TIMEFRAME,
            output_format='dataframe')

        if dados is not None and not dados.empty:
            dados['date'] = pd.to_datetime(dados['date'])

        return dados
    except Exception as e:
       raise RuntimeError(f'Erro ao consultar Google Trends: {e}') from e

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    dados = get_interest_over_time('bitcoin')
    print(dados)

    plt.figure(figsize=(10,6))
    plt.plot(dados.date, dados.value, marker='o')
    plt.title("Trends para Bitcoin")
    plt.xlabel('Data')
    plt.ylabel('Trends')
    plt.figtext(.99, .01, 'Fonte dos dados: Google Trends (trendspyg)', ha='right', fontsize=8, color='gray')
    plt.grid(alpha=.3)
    plt.tight_layout()
    plt.savefig('Bitcoin ao longo do tempo.png')