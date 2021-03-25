# méthode conversion de date (julien, gregorien)
# le calendrierjulien commencent en 1/1/4713, un an = 12 mois de 30 jours, + 1 jour tous les 4 ans
#  le calendrier grégorien commence 


def date2jd(dd, mm, yy):
    a = (14-mm)//12
    y = yy+4800-a
    m = mm+12*a-3
    print(a,y,m)
    
    jj = dd + (153*m+2)//5 + 365*y + y//4
    jg = jj - (y//100 - y//400 + 32045)      # date après 4/10/1582
    jd = jj  - 32083
    print(jj, jg, jd)
    
date2jd(1,1,-4712)

def jdFromDate(dd, mm, yy):
    '''
    Compute the (integral) Julian day number of day dd/mm/yyyy, i.e., the number 
    of days between 1/1/4713 BC (Julian calendar) and dd/mm/yyyy. 
    Formula from http://www.tondering.dk/claus/calendar.html
    '''
    #a, y, m, jd
    a = int((14 - mm) / 12)
    y = yy+4800-a
    m = mm+12*a-3
    jd = dd + int((153*m+2)/5) + 365*y + int(y/4) - int(y/100) + int(y/400) - 32045
    if (jd < 2299161):
        jd = dd + int((153*m+2)/5) + 365*y + int(y/4) - 32083    
    return jd

jd = jdFromDate(1,1,-4712)
print(jd)

def jdToDate(jd):
    '''
    Convert a Julian day number to day/month/year. Parameter jd is an integer
    '''
    #a, b, c, d, e, m, day, month, year
    if (jd > 2299160):                      # Le lendemain du 4/10/1582, le calendrier grégorien commence le 15/10/1582
        a = jd + 32044
        b = int((4*a+3)/146097)
        c = a - int((b*146097)/4)
    else:
        b = 0
        c = jd + 32082
    
    d = int((4*c+3)/1461)
    e = c - int((1461*d)/4)
    m = int((5*e+2)/153)
    day = e - int((153*m+2)/5) + 1
    month = m + 3 - 12*int(m/10)
    year = b*100 + d - 4800 + int(m/10)
    return (day, month, year)


day, month, year = jdToDate(0)     # date origine calendrier julien : 1/1/-4173 ou (1,1,-4172) car pas d'année 0
print(day, month, year)

day, month, year = jdToDate(2299160)   # 2299160 : jeudi 4/10/1582   
print(day, month, year)

day, month, year = jdToDate(2299161)    # 2299161 : vendredi 15/10/1582 (+ 10jours)
print(day, month, year)
