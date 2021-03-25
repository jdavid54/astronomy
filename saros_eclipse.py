
annee = 365.25
e_lune = 0.0549        # excentricité lune
e_terre = 0.0167       # excentricité terre
rm_lune = 384*10e3     # rayon moyen orbite lunaire
rm_terre = 150*10e6    # rayon moyen orbite terrestre

apo_lune = rm_lune*(1+e_lune)
peri_lune = rm_lune*(1-e_lune)
print(apo_lune, peri_lune)

apo_terre = rm_terre*(1+e_terre)
peri_terre = rm_terre*(1-e_terre)
print(apo_terre, peri_terre)

mois_dracon = 27.2
annee_dracon = 346.6
mois_synod = 29.5

# ligne des noeuds
revol_noeuds = 18.03  # années ou 6790 jours sens rétrograde = sens des aiguilles d'une montre
S1S2 = annee/2
saison = (1 - 1/revol_noeuds)*S1S2
print(S1S2, saison)


from datetime import date   # seulement la date
# passage soleil à la ligne de noeuds tous les 173.3 jours
P1 = date(2000, 1, 25)
P2 = date(2000, 7, 16)
P3 = date(2001, 1, 5)
P4 = date(2001, 6, 28)
print(P2 - P1)
print(P3 - P2)
print(P4 - P3)

    
from datetime import timedelta  # import function 
delta_passage = timedelta(
    days = 173,              # 173 days
    seconds = 0,           
    microseconds = 0,    
    milliseconds = 0,   
    minutes = 0,            
    hours = 8,              # 0.3 j = 8 heures
    weeks = 0               
)
print('delta',delta_passage) 

# date suivantes après P4
for k in range(1,5):
    print('P'+str(k+4)+'=',P4 + k*delta_passage)

# an 2000
Ecl1 = date(2000,2,5)
Ecl2 = date(2000,7,1)
Ecl3 = date(2000,7,31)
Ecl4 = date(2000,12,25)
# an 2001
Ecl5 = date(2001,5,21)
# an 2018
Ecl6 = date(2018,2,15)
Ecl7 = date(2018,7,13)
Ecl8 = date(2018,8,11)

# eclipse solaire tous les 147 jours ou 30 jours (cycle 2 solaires, 1 lunaire)
print(Ecl2 - Ecl1)
print(Ecl3 - Ecl2)
print(Ecl4 - Ecl3)
print(Ecl5 - Ecl4)
print(Ecl6 - Ecl1)
print(Ecl7 - Ecl2)
print(Ecl8 - Ecl3)
# entre 2000 et 2018 soit un cycle de 18.6 ans
#  saros = 18 ans 11 jours et 7 heures = 6585.3 jours
# 0 ou 2 =eclipse lunaire, 1 ou 3=eclipse solaire
sequence = ('011011',  #2000
         '21210',
         '01003',
         '0301',
         '1212',
         '1210',    # 2005
         '0303',
         '0301',
         '1212',
         '100120',  #2009
         '3030',
         '110112',  #2011
         '1210',    #2012
         '01001',
         '0301',
         '1212',
         '1210',
         '0303'      #2017
)   # 2018 répète 2000

delta_saros = timedelta(
    days = 6585,              # 6585 days
    seconds = 0,           
    microseconds = 0,    
    milliseconds = 0,   
    minutes = 0,            
    hours = 7,              # 0.3 j = 7 heures
    weeks = 0)

print('saros', delta_saros)
# date suivantes après P4
for k in range(5):
    print('An '+str(k*18+2000)+'=',Ecl1 + k*delta_saros)

long_seq = []
n = 0
for s in sequence:
    for t in range(len(s)):
        n += 1
        print(s[t],end='')
        long_seq.append(s[t])
print(long_seq, n)

espace = [0]
for i in range(len(long_seq)-1):
    if long_seq[i] != long_seq[i+1] and long_seq[i] != "2" and long_seq[i] != "3":
        #print(long_seq[i])
        espace.append(15)
    else:
        #print(long_seq[i],long_seq[i+1],147)
        interval = 147
        if long_seq[i] == "2" or long_seq[i] == "3":
            interval = 163
        espace.append(interval)
print(espace)

Ecl = date(2000,1,21)
'''
for n,k in enumerate(espace):
    delta = timedelta(days = k, hours = 7)
    Ecl += delta
    type = 'solaire'
    if long_seq[n] in ['0', '2']: type = 'lunaire'
    print(Ecl, 'Eclipse '+type)
    
Ecl1 = date(2001,1,9)
Ecl2 = date(2001,6,21)
print(Ecl2-Ecl1)

Ecl1 = date(2001,7,5)
Ecl2 = date(2001,12,14)
print(Ecl2-Ecl1)

Ecl1 = date(2003,5,31)
Ecl2 = date(2003,11,8)
print(Ecl2-Ecl1)

Ecl1 = date(2007,3,19)
Ecl2 = date(2007,8,28)
print(Ecl2-Ecl1)
'''
eclipses = [(2000,1,21),(2000,2,5),(2000,7,1),(2000,7,16),(2000,7,31),(2000,12,25),
            (2001,1,9),(2001,6,21),(2001,7,5),(2001,12,14),(2001,12,30),
            (2002,5,26),(2002,6,10),(2002,6,24),(2002,11,19),(2002,12,4),
            (2003,5,16),(2003,5,31),(2003,11,8),(2003,11,23),
            (2004,4,19),(2004,5,4),(2004,10,14),(2004,10,28),
            (2005,4,8),(2005,4,24),(2005,10,3),(2005,10,17),
            (2006,3,14),(2006,3,29),(2006,9,7),(2006,9,22),
            (2007,3,3),(2007,3,19),(2007,8,28),(2007,9,11),
            (2008,2,7),(2008,2,21),(2008,8,1),(2008,8,16),
            (2009,1,26),(2009,2,9),(2009,7,7),(2009,7,21),(2009,8,5),(2009,12,31),
            (2010,1,15),(2010,6,26),(2010,7,11),(2010,12,21),
            (2011,1,4),(2011,6,1),(2011,6,15),(2011,7,1),(2011,11,25),(2011,12,10),
            (2012,5,20),(2012,6,4),(2012,11,13),(2012,11,28),
            (2013,4,25),(2013,5,9),(2013,5,25),(2013,10,18),(2013,11,3),
            (2014,4,15),(2014,4,29),(2014,10,8),(2014,10,23),
            (2015,3,20),(2015,4,4),(2015,9,13),(2015,9,28),
            (2016,3,8),(2016,3,23),(2016,9,1),(2016,9,16),
            (2017,2,10),(2017,2,26),(2017,8,7),(2017,8,21)]

for e in range(len(eclipses)-1):
    print(eclipses[e], date(*eclipses[e+1]) - date(*eclipses[e]))
    