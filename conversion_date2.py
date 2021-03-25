from conversion_date import *
'''
===== What does the Chinese year look like? =====
The Chinese calendar – like the Hebrew – is a combined solar/lunar calendar in that it strives to have its years coincide
with the tropical year and its months coincide with the synodic months. It is not surprising that a few similarities exist
between the Chinese and the Hebrew calendar:

An ordinary year has 12 months, a leap year has 13 months.
An ordinary year has 353(5*30+7*29), 354(6*30+6*29), or 355(7*30+5*30) days, a leap year has 383, 384, or 385 days.(12months + 30days)
When determining what a Chinese year looks like, one must make a number of astronomical calculations:

1) First, determine the dates for the new moons. Here, a new moon is the completely “black” moon (that is, when the moon is in
conjunction with the sun), not the first visible crescent used in the Islamic and Hebrew calendars. 
The date of a new moon is the first day of a new month.

2) Secondly, determine the dates when the sun’s longitude is a multiple of 30 degrees. (The sun’s longitude is 0 at Vernal Equinox,
90 at Summer Solstice, 180 at Autumnal Equinox, and 270 at Winter Solstice.) These dates are called the Principal Terms and
are used to determine the number of each month:

    Principal Term 1 occurs when the sun’s longitude is 330 degrees.
    Principal Term 2 occurs when the sun’s longitude is 0 degrees.
    Principal Term 3 occurs when the sun’s longitude is 30 degrees.
    ... etc.
    Principal Term 11 occurs when the sun’s longitude is 270 degrees.
    Principal Term 12 occurs when the sun’s longitude is 300 degrees.

Each month carries the number of the Principal Term that occurs in that month.
In rare cases, a month may contain two Principal Terms; in this case the months numbers may have to be shifted.
Principal Term 11 (Winter Solstice) must always fall in the 11th month.
All the astronomical calculations are carried out for the meridian 120 degrees east of Greenwich.
This roughly corresponds to the east coast of China.
Some variations in these rules are seen in various Chinese communities.

===== What years are leap years? =====
Leap years have 13 months. To determine if a year is a leap year, calculate the number of new moons between the 11th month
in one year (i.e., the month containing the Winter Solstice) and the 11th month in the following year. If there are 13 new moons
from the start of the 11th month in the first year to the start of the 11th month in the second year, a leap month must be inserted.

In leap years, at least one month does not contain a Principal Term. The first such month is the leap month.
It carries the same number as the previous month, with the additional note that it is the leap month.

===== How does one count years? =====
Unlike most other calendars, the Chinese calendar does not count years in an infinite sequence. Instead years have names
that are repeated every 60 years. (Historically, years used to be counted since the accession of an emperor, but this was abolished after the 1911 revolution.)
Within each 60-year cycle, each year is assigned a name consisting of two components:

The first component is a Celestial Stem:
('Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý')
1.	jiǎ	(Giap)       6.	jǐ (Ky)
2.	yǐ (At)          7.	gēng (Canh)
3.	bǐng (Binh)      8.	xīn (Tân)
4.	dīng (Dinh)      9.	rén (Nhâm)
5.	wù (Mau)        10.	guǐ (Quy')
These words have no English equivalent.

The second component is a Terrestrial Branch:
('Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi')
1.	zǐ (rat)	            7.	wǔ (horse)
2.	chǒu (ox)	            8.	wèi (sheep)
3.	yín (tiger)	            9.	shēn (monkey)
4.	mǎo (hare, rabbit)	   10.	yǒu (rooster)
5.	chén(dragon)	       11.	xū (dog)
6.	sì (snake)	           12.	hài (pig)
The names of the corresponding animals in the zodiac cycle of 12 animals are given in parentheses.

Each of the two components is used sequentially. Thus, the 1st year of the 60-year cycle becomes jiǎ-zǐ,
the 2nd year is yǐ-chǒu, the 3rd year is bǐng-yín, etc. When we reach the end of a component, we start from
the beginning: The 10th year is guǐ-yǒu, the 11th year is jiǎ-xū (restarting the Celestial Stem), the 12th year
is yǐ-hài, and the 13th year is bǐng-zǐ (restarting the Terrestrial Branch). Finally, the 60th year becomes guǐ-hài.

This way of naming years within a 60-year cycle goes back approximately 2000 years. A similar naming of days and
months has fallen into disuse, but the date name is still listed in calendars.

It is customary to number the 60-year cycles since 2637 BC, when the calendar was supposedly invented, or since 2697 BC,
sixty years earlier, when the reign of Emperor Huang-di began. In one of those years the first 60-year cycle started,
which means that we are currently in the 78th or 79th sixty-year cycle.

===== What is the current year in the Chinese calendar? =====
The current 60-year cycle started on 2 February 1984 (?? 1986). That date bears the name bǐng-yín (Bính Dần) in the 60-day cycle,
and the first month of that first year bears the name bǐng-yín in the 60-month cycle.

This means that the year xīn-chǒu (Tân Sửu), the 38th year in the current cycle, started on 12 February 2021.

The year rén-yín (Nhâm Dần), the 39th year in the current cycle, will start on 1 February 2022.
'''
CAN = ("Gi\341p", "\u1EA4t", "B\355nh", "\u0110inh", "M\u1EADu", "K\u1EF7", "Canh", "T\342n", "Nh\342m", "Qu\375");
CHI = ("T\375", "S\u1EEDu", "D\u1EA7n", "M\343o", "Th\354n", "T\u1EF5", "Ng\u1ECD", "M\371i", "Th\342n", "D\u1EADu", "Tu\u1EA5t", "H\u1EE3i");

def getYearCanChi(year):
    return CAN[(year+6) % 10] + " " + CHI[(year+8) % 12];
    
def test1():
    canchi = getYearCanChi(1984)
    print(canchi)

    for k in range(60):
        print(k+1, 1984+k, getYearCanChi(1954+k), end=' / ')
        


import numpy as np
PI = np.pi

# First get the new moon julian day
def NewMoon(k):
    '''
    Compute the time of the k-th new moon after the new moon of 1/1/1900 13:52 UCT 
    (measured as the number of days since 1/1/4713 BC noon UCT, e.g., 2451545.125 is 1/1/2000 15:00 UTC).
    Returns a floating number, e.g., 2415079.9758617813 for k=2 or 2414961.935157746 for k=-2
    Algorithm from: "Astronomical Algorithms" by Jean Meeus, 1998
    '''
    #T, T2, T3, dr, Jd1, M, Mpr, F, C1, deltat, JdNew
    T = k/1236.85 #Time in Julian centuries from 1900 January 0.5
    T2 = T * T
    T3 = T2 * T
    dr = PI/180
    Jd1 = 2415020.75933 + 29.53058868*k + 0.0001178*T2 - 0.000000155*T3
    Jd1 = Jd1 + 0.00033 * np.sin((166.56 + 132.87*T - 0.009173*T2)*dr) #Mean new moon
    M = 359.2242 + 29.10535608*k - 0.0000333*T2 - 0.00000347*T3 #Sun's mean anomaly
    Mpr = 306.0253 + 385.81691806*k + 0.0107306*T2 + 0.00001236*T3 #Moon's mean anomaly
    F = 21.2964 + 390.67050646*k - 0.0016528*T2 - 0.00000239*T3 #Moon's argument of latitude
    C1=(0.1734 - 0.000393*T)*np.sin(M*dr) + 0.0021*np.sin(2*dr*M)
    C1 = C1 - 0.4068*np.sin(Mpr*dr) + 0.0161*np.sin(dr*2*Mpr)
    C1 = C1 - 0.0004*np.sin(dr*3*Mpr)
    C1 = C1 + 0.0104*np.sin(dr*2*F) - 0.0051*np.sin(dr*(M+Mpr))
    C1 = C1 - 0.0074*np.sin(dr*(M-Mpr)) + 0.0004*np.sin(dr*(2*F+M))
    C1 = C1 - 0.0004*np.sin(dr*(2*F-M)) - 0.0006*np.sin(dr*(2*F+Mpr))
    C1 = C1 + 0.0010*np.sin(dr*(2*F-Mpr)) + 0.0005*np.sin(dr*(2*Mpr+M))
    if (T < -11):
        deltat= 0.001 + 0.000839*T + 0.0002261*T2 - 0.00000845*T3 - 0.000000081*T*T3
    else:
        deltat= -0.000278 + 0.000265*T + 0.000262*T2
    JdNew = Jd1 + C1 - deltat
    return JdNew

print()

def getNewMoonDay(k, timeZone):
    '''
    Compute the day of the k-th new moon in the given time zone.
    The time zone if the time difference between local time and UTC: 7.0 for UTC+7:00
    tz in range(0,24)
    '''
    return int(NewMoon(k) + 0.5 + timeZone/24)

# julian day of k-th new moon after the new moon of 1/1/1900 13:52 UCT
# returns a floating number, e.g., 2415079.9758617813 for k=2 or 2414961.935157746 for k=-2
k = 0
jdnew0 = NewMoon(k)
print(f'{k}-th New Moon day of 1/1/1900 13:52 :',jdnew0)
k = 3
jdnewk = NewMoon(k)
print(f'{k}-th New Moon day after',jdnewk)
print(f'Number of days for the next {k} months:', jdnewk - jdnew0)


# Compute the day of the k-th new moon in the given time zone. (tz utc = 0)
tz = 0
print(getNewMoonDay(k,tz))


def SunLongitude(jdn):
    '''
    Compute the longitude of the sun at any time.
    Parameter: floating number jdn, the number of days since 1/1/4713 BC noon
    Algorithm from: "Astronomical Algorithms" by Jean Meeus, 1998
    '''
    #var T, T2, dr, M, L0, DL, L, theta, omega;
    T = (jdn - 2451545.0 ) / 36525;     # Time in Julian centuries from 2000-01-01 12:00:00 GMT
    T2 = T*T;
    dr = PI/180   # degree to radian
    M = 357.52910 + 35999.05030*T - 0.0001559*T2 - 0.00000048*T*T2   # mean anomaly, degree
    L0 = 280.46645 + 36000.76983*T + 0.0003032*T2                    # mean longitude, degree
    DL = (1.914600 - 0.004817*T - 0.000014*T2)*np.sin(dr*M);
    DL = DL + (0.019993 - 0.000101*T)*np.sin(dr*2*M) + 0.000290*np.sin(dr*3*M);
    theta = L0 + DL; # true longitude, degree
    # obtain apparent longitude by correcting for nutation and aberration
    omega = 125.04 - 1934.136 * T;
    L = theta - 0.00569 - 0.00478 * np.sin(omega * dr);  # Longitude, degree
    # Convert to radians
    L = L*dr;
    L = L - PI*2*(int(L/(PI*2))); # Normalize to (0, 2*PI)
    return L;


def getSunLongitude(dayNumber, timeZone):
    '''
    Compute sun position at midnight of the day with the given Julian day number. 
    The time zone if the time difference between local time and UTC: 7.0 for UTC+7:00.
    The def returns a number between 0 and 11. 
    From the day after March equinox and the 1st major term after March equinox, 0 is returned. 
    After that, return 1, 2, 3 ...
    '''
    L = SunLongitude(dayNumber - 0.5 - timeZone/24)
    return int(L/PI*6), L*180/PI, (int(L/PI*6)+2)%12


'''
The sun’s longitude is 0 at Vernal Equinox, 90 at Summer Solstice, 180 at Autumnal Equinox, and 270 at Winter Solstice.)
These dates are called the Principal Terms and are used to determine the number of each month:

    Principal Term 1 occurs when the sun’s longitude is 330 degrees.                       => getSunLongitude() returns 11
    Principal Term 2 occurs when the sun’s longitude is 0 degrees. (vernal equinox)        => getSunLongitude() returns 0
    Principal Term 3 occurs when the sun’s longitude is 30 degrees.                        => getSunLongitude() returns 1
    Principal Term 4 occurs when the sun’s longitude is 60 degrees.
    Principal Term 5 occurs when the sun’s longitude is 90 degrees. (summer solstice)
    Principal Term 6 occurs when the sun’s longitude is 120 degrees.
    Principal Term 7 occurs when the sun’s longitude is 150 degrees.
    Principal Term 8 occurs when the sun’s longitude is 180 degrees. (autumnal equinox)
    Principal Term 9 occurs when the sun’s longitude is 210 degrees.
    Principal Term 10 occurs when the sun’s longitude is 240 degrees.                      => getSunLongitude() returns 8
    Principal Term 11 occurs when the sun’s longitude is 270 degrees. (winter solstice)    => getSunLongitude() returns 9
    Principal Term 12 occurs when the sun’s longitude is 300 degrees.
'''
TIETKHI = ("Xu\u00E2n ph\u00E2n", "Thanh minh", "C\u1ED1c v\u0169", "L\u1EADp h\u1EA1", "Ti\u1EC3u m\u00E3n", "Mang ch\u1EE7ng",
    "H\u1EA1 ch\u00ED", "Ti\u1EC3u th\u1EED", "\u0110\u1EA1i th\u1EED", "L\u1EADp thu", "X\u1EED th\u1EED", "B\u1EA1ch l\u1ED9",
    "Thu ph\u00E2n", "H\u00E0n l\u1ED9", "S\u01B0\u01A1ng gi\u00E1ng", "L\u1EADp \u0111\u00F4ng", "Ti\u1EC3u tuy\u1EBFt", "\u0110\u1EA1i tuy\u1EBFt",
    "\u0110\u00F4ng ch\u00ED", "Ti\u1EC3u h\u00E0n", "\u0110\u1EA1i h\u00E0n", "L\u1EADp xu\u00E2n", "V\u0169 Th\u1EE7y", "Kinh tr\u1EADp")

jdn = jdFromDate(1,1,2000)
print(jdn)
TK, L, PT = getSunLongitude(jdn, 0)
print('Sun longitude 1/1/2000 ', TK, TIETKHI[2*TK], '-', TIETKHI[2*TK+1])
# returns 9 Đông chí - Tiểu hàn

jdn = jdFromDate(9,3,2021)
print(jdn)
TK, L, PT = getSunLongitude(jdn, 0)
print('Sun longitude 9/3/2021 ', TK,  TIETKHI[2*TK], '-',TIETKHI[2*TK+1])
# returns 11, Vũ Thủy - Kinh trập

# mars equinox 21/3/2021
jdn = jdFromDate(21,3,2021)
print(jdn)
TK, L, PT = getSunLongitude(jdn, 0)
# every TK contains 2 TIETKHIs
print('Sun longitude 21/3/2021 ', TK,  TIETKHI[2*TK],'-', TIETKHI[2*TK+1])
# returns 0, Xuân phân - Thanh minh

def getLunarMonth11(yy, timeZone):
    '''
    Find the day that starts the luner month 11 of the given year for the given time zone
    '''
    #k, off, nm, sunLong
    #off = jdFromDate(31, 12, yy) - 2415021.076998695
    off = jdFromDate(31, 12, yy) - 2415021
    k = int(off / 29.530588853)       # k = number of complete lunar months since 1/1/1900 (jd=2415021) to the end of the year yy
    nm = getNewMoonDay(k, timeZone)                 # get the julian day of this k-th new moon
    sunLong = getSunLongitude(nm, timeZone)[0]      # get the sun longitude at local midnight
    #print(sunLong)
    if (sunLong >= 9):                              # getSunLongitude() returns 9 for winter solstice
        nm = getNewMoonDay(k-1, timeZone)           # get the previous new moon because the k-th lunar month does not include the winter solstice
    return nm, sunLong                              # the month beginning with nm is the 11th month which include the winter solstice

tz = 0
yy = 2021
print('\nFind 11-th new moon of a year: ', yy)

nm11, sunLong = getLunarMonth11(yy, tz)      # 11th new moon of the year
print('julian day', nm11, f'11th new moon of {yy}', jdToDate(nm11), sunLong)

yy = 2018
print('\nFind 11-th new moon of a year: ', yy)

nm11, sunLong = getLunarMonth11(yy, tz)      # 11th new moon of the year
print('julian day', nm11, f'11th new moon of {yy}', jdToDate(nm11), sunLong)