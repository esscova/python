"""
Consultas Relacionadas (Related Queries)

Obj:
    Obter consultas relacionadas de uma palavra-chave utilizando a biblioteca trendspyg.

Autor: Wellington M Santos

* Nota:
    Na documentação, o autor comenta que download_google_trends_explore() é a função mais complexa da biblioteca,
    pois ela depende do carregamento completo do gráfico do Google Trends.

"""

# DEPENDENCIAS #
from trendspyg              import download_google_trends_explore
from trendspyg.exceptions   import DownloadError, BrowserError
from typing import Tuple
import pandas as pd

# CONFIGURAÇÕES #
DEFAULT_GEO         = 'BR'
DEFAULT_TIMEFRAME   = 'today 12-m'

# FUNÇÕES #
def get_related_queries(keyword:str, geo:str, timeframe:str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Retorna consultas relacionados (Top e Rising) para uma palavra-chave.

    Args:
        - keyword: palavra-chave pesquisada
        - geo: código ISO do país
        - timeframe: intervalo da pesqauisa
    Returns:
        tuple[pd.DataFrame, pd.DataFrame] -> (top_queries, rising_queries)
    """
    try:
        data = download_google_trends_explore(
            keyword=keyword,
            geo=geo,
            timeframe=timeframe,
        )

        related = data.get('related_queries', {})
        top     = pd.DataFrame(related.get('top', []))
        rising  = pd.DataFrame(related.get('rising', []))

        return top, rising
    
    except DownloadError as e:
        raise RuntimeError("Google Trends limitou a consulta temporariamente") from e
    except BrowserError as e:
        raise RuntimeError('Google Trends mudou a página, atualize o trendspyg ou tente novamente mais tarde.')
    except Exception as e:
        raise RuntimeError(f"Erro ao consultar o Google Trends: {e}") from e

# MAIN #
def main():
    top, rising = get_related_queries(keyword='Python',
                                      geo=DEFAULT_GEO,
                                      timeframe=DEFAULT_TIMEFRAME)

    if not top.empty and not rising.empty:

        print('\nTOP QUERIES\n')
        print(top)

        print('\nRISING QUERIES\n')
        print(rising)
    

if __name__ == '__main__':
    main()