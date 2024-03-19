import pandas as pd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs
from time import sleep

def read_page(url):
    uClient = uReq(url)
    page = uClient.read()
    uClient.close()
    return page

def get_data():
    url = 'https://www.espn.com/mens-college-basketball/bpi/_/group/'
    df = pd.DataFrame(columns = ['name', 'conf', 'bpi', 'off', 'def', 'ppg', 'oppg'])

    i = 1
    conferences = 32

    while conferences > 1:
        soup = bs(read_page(url+str(i)), 'html.parser')
        foo = soup.findAll('tr', {'class': 'Table__TR Table__TR--sm Table__even'})
        n = len(foo)//2
        for j in range(n):
            id = foo[j].find('a', {'class': 'AnchorLink'})['href']
            soup = bs(read_page('https://www.espn.com'+id), 'html.parser')
            bar = soup.findAll('div', {'class': 'tc h2 clr-gray-03'})
            ppg = bar[0].text
            oppg = bar[3].text
            team = foo[j].findAll('td')
            stats = foo[j+n].findAll('div')
            df.loc[len(df)] = [team[0].text, team[1].text, float(stats[1].text), float(stats[4].text), float(stats[5].text), float(ppg), float(oppg)]
        if n != 0:
            conferences -= 1
        i += 1
        sleep(1)
    df = df.sort_values(by=['bpi', 'off'], ascending=False)
    df.to_csv('dataset.tsv', sep='\t', index=False)
    df.to_csv('dataset.csv', index=False)

def get_bracket():
    url1 = 'https://www.espn.com/mens-college-basketball/bpi/_/group/100'
    url2 = 'https://www.espn.com/mens-college-basketball/bpi/_/group/100/sort/bpi.bpi/dir/asc'
    df = pd.DataFrame(columns = ['name', 'bpi', 'off', 'def', 'ppg', 'oppg'])

    for url in [url1, url2]:
        soup = bs(read_page(url), 'html.parser')
        foo = soup.findAll('tr', {'class': 'Table__TR Table__TR--sm Table__even'})
        for i in range(34):
            id = foo[i].find('a', {'class': 'AnchorLink'})['href']
            soup = bs(read_page('https://www.espn.com'+id), 'html.parser')
            bar = soup.findAll('div', {'class': 'tc h2 clr-gray-03'})
            ppg = bar[0].text
            oppg = bar[3].text
            name = foo[i].td.text
            stats = foo[i+50].findAll('td')
            df.loc[len(df)] = [name, float(stats[1].text), float(stats[4].text), float(stats[5].text), float(ppg), float(oppg)]
    df = df.sort_values(by=['bpi', 'off'], ascending=False)
    df.to_csv('bracket.tsv', sep='\t', index=False)
    df.to_csv('bracket.csv', index=False)