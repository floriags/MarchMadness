import numpy as np
import pandas as pd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

df = pd.read_csv("teams.csv")
df = df[:4]

def formula(idx1, idx2):
    team1 = df.iloc[idx1]
    seed1 = team1['seed']
    rank1 = team1['rank']
    ppg1 = team1['ppg']
    oppg1 = team1['oppg']
    bpi1 = team1['bpi']
    off1 = team1['off']
    def1 = team1['def']

    team2 = df.iloc[idx2]
    seed2 = team2['seed']
    rank2 = team2['rank']
    ppg2 = team2['ppg']
    oppg2 = team2['oppg']
    bpi2 = team2['bpi']
    off2 = team2['off']
    def2 = team2['def']

df = df.sort_values(by=['bpi'], ascending=False)

url = 'https://www.espn.com/mens-college-basketball/bpi'

df = pd.DataFrame(columns = ['team', 'bpi', 'bpi_rank', 'off', 'def', 'ppg', 'oppg'])

def read_page(url):
    uClient = uReq(url)
    page = uClient.read()
    uClient.close()
    return page

soup = bs(read_page(url), 'html.parser')
teams = soup.findAll('tr', {'class': 'Table__TR Table__TR--sm Table__even'})

for i in range(5):
    team = teams[i+50]
    t = team.findAll('div')
    df.loc[len(df)] = [teams[i].find('img', alt=True)['alt'], float(t[1].text.strip()), float(t[2].text), float(t[4].text), float(t[5].text), 0, 0]

#print(df)

#df.to_csv('madness.csv', index=False)

exit()

weights = np.linspace(1, 0, 17)

def formula1(idx1, idx2):
    team1 = df.iloc[idx1]
    ppg1 = team1["PPG"]
    oppg1 = team1["OPPG"]
    weight1 = weights[team1["Seed"]]

    team2 = df.iloc[idx2]
    ppg2 = team2["PPG"]
    oppg2 = team2["OPPG"]
    weight2 = weights[team2["Seed"]]

    score1 = ((ppg1*weight1)+(oppg2*weight2))
    score2 = ((ppg2*weight2)+(oppg1*weight1))

    print("{} {:.2f} - {:.2f} {}".format(team1["Team"], score1, score2, team2["Team"]))

    if score1 == score2:
        print("\n\nLikt\n\n")

    if score1 > score2:
        return team1.name
    return team2.name

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

"""
ls = {
    "Alabama": 1, "Purdue": 1, "Houston": 1, "Kansas": 1,
    "Arizona": 2, "Marquette": 2, "Texas": 2, "UCLA": 2,
    "Baylor": 3, "Kansas St": 3, "Xavier": 3, "Gonzaga": 3,
    "Virginia": 4, "Tennessee": 4, "Indiana": 4, "UConn": 4,
    "San Diego St": 5, "Duke": 5, "Miami": 5, "Saint Mary's": 5,
    "Creighton": 6, "Kentucky": 6, "Iowa State": 6, "TCU": 6,
    "Missouri": 7, "Michigan St": 7, "Texas A&M": 7, "Northwestern": 7,
    "Maryland": 8, "Memphis": 8, "Iowa": 8, "Arkansas": 8, 
    "West Virginia": 9, "FAU": 9, "Auburn": 9, "Illinois": 9,
    "Utah State": 10, "USC": 10, "Penn State": 10, "Boise St": 10,
    "NC State": 11, "Providence": 11, "MSST": 11, "ASU": 11,
    "Charleston": 12, "Oral Roberts": 12, "Drake": 12, "VCU": 12,
    "Furman": 13, "Louisiana": 13, "Kent State": 13, "Iona": 13,
    "USCB": 14, "Montana St": 14, "Kennesaw St": 14, "Grand Canyon": 14,
    "Princeton": 15, "Vermont": 15, "Colgate": 15, "UNC Asheville": 15,
    "AMCC": 16, "TXSO": 16, "N Kentucky": 16, "Howard": 16
}

def picker(team1, team2):
    seed1 = ls[team1]
    seed2 = ls[team2]
    tmp1 = team2
    tmp2 = seed2
    if seed2 < seed1:
        team1 = team2
        team2 = tmp1
        seed1 = seed2
        seed2 = tmp2
    
    tot = seed1+seed2

    if np.random.random() > (seed1/tot):
        return team1
    return team2

#First Round
fr1 = picker("Alabama", "AMCC")
fr2 = picker("Maryland", "West Virginia")
fr3 = picker("San Diego St", "Charleston")
fr4 = picker("Furman", "Virginia")
fr5 = picker("Creighton", "NC State")
fr6 = picker("USCB", "Baylor")
fr7 = picker("Utah State", "Missouri")
fr8 = picker("Arizona", "Princeton")
fr9 = picker("TXSO", "Purdue")
fr10 = picker("Memphis", "FAU")
fr11 = picker("Oral Roberts", "Duke")
fr12 = picker("Tennessee", "Louisiana")
fr13 = picker("Kentucky", "Providence")
fr14 = picker("Montana St", "Kansas St")
fr15 = picker("Michigan St", "USC")
fr16 = picker("Marquette", "Vermont")

fr17 = picker("N Kentucky", "Houston")
fr18 = picker("Iowa", "Auburn")
fr19 = picker("Drake", "Miami")
fr20 = picker("Indiana", "Kent State")
fr21 = picker("Iowa State", "MSST")
fr22 = picker("Kennesaw St", "Xavier")
fr23 = picker("Texas A&M", "Penn State")
fr24 = picker("Texas", "Colgate")
fr25 = picker("Howard", "Kansas")
fr26 = picker("Arkansas", "Illinois")
fr27 = picker("VCU", "Saint Mary's")
fr28 = picker("UConn", "Iona")
fr29 = picker("ASU", "TCU")
fr30 = picker("Grand Canyon", "Gonzaga")
fr31 = picker("Northwestern", "Boise St")
fr32 = picker("UNC Asheville", "UCLA")

#Second round
sr1 = picker(fr1, fr2)
sr2 = picker(fr3, fr4)
sr3 = picker(fr5, fr6)
sr4 = picker(fr7, fr8)
sr5 = picker(fr9, fr10)
sr6 = picker(fr11, fr12)
sr7 = picker(fr13, fr14)
sr8 = picker(fr15, fr16)

sr9 = picker(fr17, fr18)
sr10 = picker(fr19, fr20)
sr11 = picker(fr21, fr22)
sr12 = picker(fr23, fr24)
sr13 = picker(fr25, fr26)
sr14 = picker(fr27, fr28)
sr15 = picker(fr29, fr30)
sr16 = picker(fr31, fr32)

#Sweet 16
ss1 = picker(sr1, sr2)
ss2 = picker(sr3, sr4)
ss3 = picker(sr5, sr6)
ss4 = picker(sr7, sr8)

ss5 = picker(sr9, sr10)
ss6 = picker(sr11, sr12)
ss7 = picker(sr13, sr14)
ss8 = picker(sr15, sr16)

#Elite 8
ee1 = picker(ss1, ss2)
ee2 = picker(ss3, ss4)

ee3 = picker(ss5, ss6)
ee4 = picker(ss7, ss8)

#Final Four
ff1 = picker(ee1, ee2)
ff2 = picker(ee3, ee4)

winner = picker(ff1, ff2).upper()


print("{} - {} | {} - {} | {} - {} | {} - {} | {} - {} | {} - {} | {} - {} | {} - {}".format(fr1, fr2, fr3, fr4, fr5, fr6, fr7, fr8, fr9, fr10, fr11, fr12, fr13, fr14, fr15, fr16))

print("\n\t{} - {}\t\t|\t\t{} - {}\t\t|\t\t{} - {}\t\t|\t\t{} - {}".format(sr1, sr2, sr3, sr4, sr5, sr6, sr7, sr8))

print("\n\t\t\t\t\t\t{} - {}\t\t\t\t|\t\t\t\t{} - {}".format(ss1, ss2, ss3, ss4))

print("\n\t\t\t\t\t\t\t\t\t\t{} - {}".format(ee1, ee2))

print("\n\t\t\t\t\t\t\t\t\t\t\t{}".format(ff1))
print("\n\t\t\t\t\t\t\t\t\t\t\t{}".format(winner))
print("\n\t\t\t\t\t\t\t\t\t\t\t{}".format(ff2))

print("\n\t\t\t\t\t\t\t\t\t\t{} - {}".format(ee3, ee4))

print("\n\t\t\t\t\t\t{} - {}\t\t\t|\t\t\t\t{} - {}".format(ss5, ss6, ss7, ss8))

print("\n\t{} - {}\t\t|\t\t{} - {}\t\t|\t\t{} - {}\t\t|\t\t{} - {}".format(sr9, sr10, sr11, sr12, sr13, sr14, sr15, sr16))

print("{} - {} | {} - {} | {} - {} | {} - {} | {} - {} | {} - {} | {} - {} | {} - {}".format(fr17, fr18, fr19, fr20, fr21, fr22, fr23, fr24, fr25, fr26, fr27, fr28, fr29, fr30, fr31, fr32))
"""