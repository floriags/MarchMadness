import numpy as np
import pandas as pd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

url = 'https://www.espn.com/mens-college-basketball/bpi/_/group/'
url2 = 'https://www.espn.com/mens-college-basketball/stats/team'
url3 = 'https://www.espn.com/mens-college-basketball/stats/team/_/view/opponent'

df = pd.DataFrame(columns = ['name', 'conf', 'bpi', 'off', 'def', 'ppg', 'oppg'])

def read_page(url):
    uClient = uReq(url)
    page = uClient.read()
    uClient.close()
    return page

for i in range(1,33):
    soup = bs(read_page(url+str(i)), 'html.parser')
    foo = soup.findAll('tr', {'class': 'Table__TR Table__TR--sm Table__even'})
    n = len(foo)//2
    for j in range(n):
        team = foo[j].findAll('td')
        stats = foo[j+n].findAll('div')
        df.loc[len(df)] = [team[0].text, team[1].text, float(stats[1].text), float(stats[4].text), float(stats[5].text), 0, 0]

print(df)
df.to_csv('dataset.csv', index=False)

def formula1(team1, team2):

    w1off = team1['off']
    w1def = team1['def']
    w2off = team2['off']
    w2def = team2['def']

    #team1['off']/team2['def']

    score1 = (team1['ppg']*(w1off/(w1off+w2def))) + (team2['oppg']*(w2def/(w1off+w2def)))
    score2 = (team2['ppg']*(w2off/(w2off+w1def))) + (team1['oppg']*(w1def/(w2off+w1def)))

    print("{} {:.2f} - {:.2f} {}".format(team1['team'], score1, score2, team2['team']))

    if score1 == score2:
        print("\n\nLikt\n\n")

    if score1 > score2:
        return team1.name
    return team2.name

exit()

#Roung of 64
g1 = formula1(0,60)
g2 = formula1(28,32)
g3 = formula1(16,44)
g4 = formula1(12,48)
g5 = formula1(20,40)
g6 = formula1(8,52)
g7 = formula1(24,36)
g8 = formula1(4,56)
g9 = formula1(1,61)
g10 = formula1(29,33)
g11 = formula1(17,45)
g12 = formula1(13,49)
g13 = formula1(21,41)
g14 = formula1(9,53)
g15 = formula1(25,37)
g16 = formula1(5,57)

g17 = formula1(2,62)
g18 = formula1(30,34)
g19 = formula1(18,46)
g20 = formula1(14,50)
g21 = formula1(22,42)
g22 = formula1(10,54)
g23 = formula1(26,38)
g24 = formula1(6,58)
g25 = formula1(3,63)
g26 = formula1(31,35)
g27 = formula1(19,47)
g28 = formula1(15,51)
g29 = formula1(23,43)
g30 = formula1(11,55)
g31 = formula1(27,39)
g32 = formula1(7,59)

#Round of 32
g33 = formula1(g1, g2)
g34 = formula1(g3, g4)
g35 = formula1(g5, g6)
g36 = formula1(g7, g8)
g37 = formula1(g9, g10)
g38 = formula1(g11, g12)
g39 = formula1(g13, g14)
g40 = formula1(g15, g16)

g41 = formula1(g17, g18)
g42 = formula1(g19, g20)
g43 = formula1(g21, g22)
g44 = formula1(g23, g24)
g45 = formula1(g25, g26)
g46 = formula1(g27, g28)
g47 = formula1(g29, g30)
g48 = formula1(g31, g32)

#Sweet 16
g49 = formula1(g33,g34)
g50 = formula1(g35,g36)
g51 = formula1(g37,g38)
g52 = formula1(g39,g40)

g53 = formula1(g41,g42)
g54 = formula1(g43,g44)
g55 = formula1(g45,g46)
g56 = formula1(g47,g48)

#Elite 8
g57 = formula1(g49,g50)
g58 = formula1(g51,g52)

g59 = formula1(g53,g54)
g60 = formula1(g55,g56)

#Final Four
g61 = formula1(g57, g58)
g62 = formula1(g59, g60)

#Final
g63 = formula1(g61, g62)