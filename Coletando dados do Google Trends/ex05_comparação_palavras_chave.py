"""
Comparação de Palavras-chave

Objetivo:
    Comparar o interesse relativo ao longo do tempo para múltiplas
    palavras-chave utilizando a biblioteca trendspyg.

Autor:
    Wellington M Santos
"""

# BIBLIOTECAS #
from trendspyg              import download_google_trends_comparison
from trendspyg.exceptions   import DownloadError, BrowserError, RateLimitError
import pandas as pd
from loguru import logger

# CONFIGURAÇÕES #
DEFAULT_GEO = "BR"
DEFAULT_TIMEFRAME = "today 12-m"


# FUNÇÕES #
def get_comparison(
    keywords: list[str],
    geo: str = DEFAULT_GEO,
    timeframe: str = DEFAULT_TIMEFRAME,
    include_geo = False
) -> dict:
    """
    Coleta dados comparativos do Google Trends.

    Args:
        keywords: Lista de 2 a 5 palavras-chave.
        geo: Código geográfico.
        timeframe: Intervalo da pesquisa.

    Returns:
        Dicionário com os dados da comparação.
    """

    try:
        logger.info(f"Coletando comparação para: {', '.join(keywords)}")
        data = download_google_trends_comparison(
            keywords,
            geo=geo,
            timeframe=timeframe,
            include_geo=include_geo,
            # headless=False
        )

        logger.info("Dados coletados com sucesso")

        return data

    except RateLimitError as e:
        raise RuntimeError(
            "Google Trends limitou a requisição de forma persistente. "
            "Aguarde alguns minutos antes de tentar novamente."
        ) from e

    except DownloadError as e:
        raise RuntimeError(
            "Google Trends limitou a consulta temporariamente."
        ) from e

    except BrowserError as e:
        raise RuntimeError(
            "Google Trends mudou a página. "
            "Atualize o trendspyg ou tente novamente mais tarde."
        ) from e

    except Exception as e:
        raise RuntimeError(
            f"Erro ao consultar o Google Trends: {e}"
        ) from e


def prepare_interest_over_time(data: dict) -> pd.DataFrame:
    """
    Transforma interest_over_time em DataFrame.
    """

    records = data.get("interest_over_time", [])

    if not records:
        return pd.DataFrame()

    df = pd.DataFrame(records)

    values = pd.DataFrame(df.pop("values").tolist())

    df = pd.concat([df, values], axis=1)

    df["date"] = pd.to_datetime(df["date"])

    return df


def prepare_averages(data: dict) -> pd.DataFrame:
    """
    Transforma as médias da comparação em DataFrame.
    """

    averages = data.get("averages", {})

    if not averages:
        return pd.DataFrame()

    df = ( pd.Series(averages, name="media")
          .rename_axis("keyword")
          .reset_index()
    )

    return df


# MAIN #
def main():

    keywords = ["python", "IA", "Ciência de Dados"]

    env = get_comparison( keywords=keywords)

    dados_tempo = prepare_interest_over_time(env)

    dados_medias = prepare_averages(env)

    print("\nINTERESSE AO LONGO DO TEMPO\n")
    print(dados_tempo)

    print("\nMÉDIA DO PERÍODO\n")
    print(dados_medias)

    import matplotlib.pyplot as plt

    plt.figure(figsize=(10,6))
    for keyword in keywords:
        plt.plot(dados_tempo['date'], dados_tempo[keyword], label=keyword, linewidth=2)
    plt.title('Interesse Relativo ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Índice de interesse relativo')
    plt.ylim(0,100)
    plt.legend(title='Palavra-chave')
    plt.figtext(.99, .01, 'Fonte dos dados: Google Trends (trendspyg)', ha='right', fontsize=8, color='gray')
    plt.grid(alpha=.4)
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.savefig('interesse relativo ao longo do tempo.png')
    plt.close()


if __name__ == "__main__":
    main()