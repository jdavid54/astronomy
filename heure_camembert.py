import datetime
import time

now=datetime.datetime.now()
print(now)
am=' AM'
mi=' midi'
if now.hour>12:
	am=' PM'
	mi=' minuit'
zero=""
if now.minute<10:zero="0"

# cadran 12 ou 24
cadran=12
heure_cadran=now.hour%cadran
minute_cadran=now.minute/60
heureminute_cadran = heure_cadran + minute_cadran
reste_cadran=cadran-heureminute_cadran
if cadran>12:
	am=''
	mi=' minuit'
print (heure_cadran,  minute_cadran, reste_cadran,am)

import matplotlib.pyplot as plt
import numpy as np

def func(pct, allvals):
    absolute = (pct/100.*np.sum(allvals))
    return "{:1.1f}h\n({:1.1f}%)".format(absolute, pct)

def timetogo():
    reste='il reste\n'
    sep=':'
    reste_heure=int(reste_cadran)
    reste_mn=60-now.minute
    if reste_mn==60:
        sep=''
        reste_heure+=1
        reste_mn=''
    reste=reste+str(reste_heure)+sep+str(reste_mn)+'\navant'+mi
    return reste

t=timetogo()
print(t)
fig1, ax1 = plt.subplots()
#labels = 'heure', 'mn', 'reste'
labels = str(heure_cadran),str(now.minute),t
clock = [heure_cadran, minute_cadran, reste_cadran]
explode = (0, 0, 0.1)
ax1.pie(clock, explode=explode, labels=labels, autopct=lambda pct: func(pct,clock), 
        shadow=True, startangle=90, counterclock=False, frame=False)
zero=""
if now.minute<10:zero="0"
plt.title(str(heure_cadran)+":"+zero+str(now.minute)+am)
ax1.axis('equal')  

plt.show()