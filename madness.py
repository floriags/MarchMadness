import numpy as np
import pandas as pd

df = pd.read_csv('bracket.csv')
names = df['name']

def bracket(team1, team2):
    name1, bpi1, off1, def1, ppg1, oppg1 = team1[['name', 'bpi', 'off', 'def', 'ppg', 'oppg']].iloc[0]
    name2, bpi2, off2, def2, ppg2, oppg2 = team2[['name', 'bpi', 'off', 'def', 'ppg', 'oppg']].iloc[0]

    #George is getting Upset!
    w1 = bpi1/(bpi1+bpi2)
    w2 = bpi2/(bpi1+bpi2)

    #These Upsets are making me thirsty!
    w1 = off1/(off1+def2)
    w2 = off2/(off2+def1)

    #A bracket about nothing
    w1 = off1/(off1+bpi2)
    w2 = off2/(off2+bpi1)

    score1 = (ppg1+oppg2)*w1
    score2 = (ppg2+oppg1)*w2

    print("{:>26s} {:6.2f} - {:.2f} {:<}".format(name1, score1, score2, name2))

    if score1 > score2:
        return name1
    return name2

print('East')
g1 = bracket(df.loc[names=='UConn Huskies'], df.loc[names=='Stetson Hatters'])
g2 = bracket(df.loc[names=='Florida Atlantic Owls'], df.loc[names=='Northwestern Wildcats'])
g3 = bracket(df.loc[names=='San Diego State Aztecs'], df.loc[names=='UAB Blazers'])
g4 = bracket(df.loc[names=='Auburn Tigers'], df.loc[names=='Yale Bulldogs'])
g5 = bracket(df.loc[names=='BYU Cougars'], df.loc[names=='Duquesne Dukes'])
g6 = bracket(df.loc[names=='Illinois Fighting Illini'], df.loc[names=='Morehead State Eagles'])
g7 = bracket(df.loc[names=='Washington State Cougars'], df.loc[names=='Drake Bulldogs'])
g8 = bracket(df.loc[names=='Iowa State Cyclones'], df.loc[names=='South Dakota State Jackrabbits'])

print('\nWest')
g9 = bracket(df.loc[names=='North Carolina Tar Heels'], df.loc[names=='Howard Bison']) #Wagner Seahawks
g10 = bracket(df.loc[names=='Mississippi State Bulldogs'], df.loc[names=='Michigan State Spartans'])
g11 = bracket(df.loc[names=='Saint Mary\'s Gaels'], df.loc[names=='Grand Canyon Lopes'])
g12 = bracket(df.loc[names=='Alabama Crimson Tide'], df.loc[names=='Charleston Cougars'])
g13 = bracket(df.loc[names=='Clemson Tigers'], df.loc[names=='New Mexico Lobos'])
g14 = bracket(df.loc[names=='Baylor Bears'], df.loc[names=='Colgate Raiders'])
g15 = bracket(df.loc[names=='Dayton Flyers'], df.loc[names=='Nevada Wolf Pack'])
g16 = bracket(df.loc[names=='Arizona Wildcats'], df.loc[names=='Long Beach State Beach'])

print('\nSouth')
g17 = bracket(df.loc[names=='Houston Cougars'], df.loc[names=='Longwood Lancers'])
g18 = bracket(df.loc[names=='Nebraska Cornhuskers'], df.loc[names=='Texas A&M Aggies'])
g19 = bracket(df.loc[names=='Wisconsin Badgers'], df.loc[names=='James Madison Dukes'])
g20 = bracket(df.loc[names=='Duke Blue Devils'], df.loc[names=='Vermont Catamounts'])
g21 = bracket(df.loc[names=='Texas Tech Red Raiders'], df.loc[names=='NC State Wolfpack'])
g22 = bracket(df.loc[names=='Kentucky Wildcats'], df.loc[names=='Oakland Golden Grizzlies'])
g23 = bracket(df.loc[names=='Florida Gators'], df.loc[names=='Boise State Broncos']) #Colorado Buffaloes
g24 = bracket(df.loc[names=='Marquette Golden Eagles'], df.loc[names=='Western Kentucky Hilltoppers'])

print('\nMidwest')
g25 = bracket(df.loc[names=='Purdue Boilermakers'], df.loc[names=='Grambling Tigers']) #Montana State Bobcats
g26 = bracket(df.loc[names=='Utah State Aggies'], df.loc[names=='TCU Horned Frogs'])
g27 = bracket(df.loc[names=='Gonzaga Bulldogs'], df.loc[names=='McNeese Cowboys'])
g28 = bracket(df.loc[names=='Kansas Jayhawks'], df.loc[names=='Samford Bulldogs'])
g29 = bracket(df.loc[names=='South Carolina Gamecocks'], df.loc[names=='Oregon Ducks'])
g30 = bracket(df.loc[names=='Creighton Bluejays'], df.loc[names=='Akron Zips'])
g31 = bracket(df.loc[names=='Texas Longhorns'], df.loc[names=='Virginia Cavaliers']) #Colorado State Rams
g32 = bracket(df.loc[names=='Tennessee Volunteers'], df.loc[names=='Saint Peter\'s Peacocks'])

print('\nSecond round')
g33 = bracket(df.loc[names==g1], df.loc[names==g2])
g34 = bracket(df.loc[names==g3], df.loc[names==g4])
g35 = bracket(df.loc[names==g5], df.loc[names==g6])
g36 = bracket(df.loc[names==g7], df.loc[names==g8])
g37 = bracket(df.loc[names==g9], df.loc[names==g10])
g38 = bracket(df.loc[names==g11], df.loc[names==g12])
g39 = bracket(df.loc[names==g13], df.loc[names==g14])
g40 = bracket(df.loc[names==g15], df.loc[names==g16])
g41 = bracket(df.loc[names==g17], df.loc[names==g18])
g42 = bracket(df.loc[names==g19], df.loc[names==g20])
g43 = bracket(df.loc[names==g21], df.loc[names==g22])
g44 = bracket(df.loc[names==g23], df.loc[names==g24])
g45 = bracket(df.loc[names==g25], df.loc[names==g26])
g46 = bracket(df.loc[names==g27], df.loc[names==g28])
g47 = bracket(df.loc[names==g29], df.loc[names==g30])
g48 = bracket(df.loc[names==g31], df.loc[names==g32])

print('\nSweet 16')
g49 = bracket(df.loc[names==g33], df.loc[names==g34])
g50 = bracket(df.loc[names==g35], df.loc[names==g36])
g51 = bracket(df.loc[names==g37], df.loc[names==g38])
g52 = bracket(df.loc[names==g39], df.loc[names==g40])
g53 = bracket(df.loc[names==g41], df.loc[names==g42])
g54 = bracket(df.loc[names==g43], df.loc[names==g44])
g55 = bracket(df.loc[names==g45], df.loc[names==g46])
g56 = bracket(df.loc[names==g47], df.loc[names==g48])

print('\nElite 8')
g57 = bracket(df.loc[names==g49], df.loc[names==g50])
g58 = bracket(df.loc[names==g51], df.loc[names==g52])
g59 = bracket(df.loc[names==g53], df.loc[names==g54])
g60 = bracket(df.loc[names==g55], df.loc[names==g56])

print('\nFinal Four')
g61 = bracket(df.loc[names==g57], df.loc[names==g58])
g62 = bracket(df.loc[names==g59], df.loc[names==g60])

print('\nChampionship')
g63 = bracket(df.loc[names==g61], df.loc[names==g62])