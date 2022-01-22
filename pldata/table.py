import pandas as pd
import requests as req
from bs4 import BeautifulSoup


URL = 'https://www.premierleague.com/tables'

res = req.get(URL)
soup = BeautifulSoup(res.text, 'html5lib')

def current_table():
    """ 
        Get the current season table 
    """

    tabela_bruta = soup.find('table')

    for row in tabela_bruta.find_all('tr', {'class': 'expandable'}):
        row.decompose()

    df = pd.read_html(tabela_bruta.prettify())[0]
    df.index = range(1,21)
    df.index.name = 'Position'
    df = df.rename(columns={'Position  Pos': 'Previous Position'})

    for i in range(0,20):
        df['Previous Position'].iloc[i] = df['Previous Position'].iloc[i].split(' ')[-1]

    return df

