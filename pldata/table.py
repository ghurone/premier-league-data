import pandas as pd
import requests as req
from bs4 import BeautifulSoup


months = {'January': '01', 'February': '02', 'March': '03', 'April': '04',
         'May': '05', 'June': '06', 'July': '07', 'August': '08',
         'September': '09', 'October': '10', 'November': '11', 'December': '12'}

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

    df = df.rename(columns={'Position  Pos': 'Previous Position', 'Played  Pl': 'Played', 'Won  W': 'Won',
                            'Drawn  D': 'Drawn', 'Lost  L': 'Lost', 'Points  Pts': 'Points', 'Form': 'Last Five'})

    df['Position'] = range(1, 21)
    df['Previous Position'] = df.loc[:, 'Previous Position'].str[-2:].str.strip()
    df['Abbreviation'] = df.loc[:, 'Club'].str[-3:]
    df['Club'] = df.loc[:, 'Club'].str[:-3].str.strip()

    temp = df.loc[:, 'Last Five'].str.replace('  ', ' ').str.split(' ').str
    df['Last Five'] = temp[0] + ' - ' + temp[10] + ' - ' + temp[20] + ' - ' + temp[30] + ' - '+ temp[40]

    temp = df.loc[:, 'Next'].str.replace('  ', ' ').str.split(' ').str
    df['Next'] = temp[-3] + ' x ' + temp[-1] + ' (' + temp[-6] + '-' + temp[-5].map(months) + '-' + temp[-4] + ' ' + temp[-2] + ')'

    df = df[['Position', 'Previous Position', 'Abbreviation', 'Club', 'Points', 'Played', 'Won',
            'Drawn', 'Lost', 'GF', 'GA', 'GD', 'Last Five', 'Next']]
    
    return df


if __name__ == '__main__':
    print(current_table())