#https://rhodesmill.org/skyfield/almanac.html#transits

from skyfield.api import load
from skyfield import almanac
# ['New Moon', 'First Quarter', 'Full Moon', 'Last Quarter']
#print('Load bsp file ...')
eph = load('de421.bsp')

ts = load.timescale()
#Sunrise and Sunset
RISE_SET = ['Sunset', 'Sunrise']

from skyfield.api import N, W, wgs84
lat, lon = (48.8796966,2.5415929)
#print('Bluffton using wgs84 :',lat,lon)
bluffton = wgs84.latlon(lat, lon)
body = 'Sun'

#Sunrise and Sunset
RISE_SET = ['Sunset', 'Sunrise']
day = 26
month = 1
year = 2021
print('\nSunrise and sunset on',day,'at',lat,lon)

t0 = ts.utc(year, month, day)
t1 = ts.utc(year, month, day+1)
t, y = almanac.find_discrete(t0, t1, almanac.sunrise_sunset(eph, bluffton))

for ti, yi in zip(t, y):
    print(ti.utc_iso(), RISE_SET[yi])
