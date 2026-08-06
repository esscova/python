import pandas as pd
from trendspyg import download_google_trends_rss

def get_rss(geo:str='BR') -> pd.DataFrame:
    dados = download_google_trends_rss(geo=geo,
                                    output_format='dataframe')
    return dados

if __name__ == "__main__":
    trends = get_rss()
    print(trends)
