#https://rhodesmill.org/skyfield/almanac.html#transits

from skyfield.api import load
from skyfield import almanac
#print('Load bsp file ...')
eph = load('de421.bsp')

year = 2021
ts = load.timescale()
#Lunar eclipses
# ['Penumbral', 'Partial', 'Total']
from skyfield import eclipselib
print('Lunar eclipses in',year)
t0 = ts.utc(year, 1, 1)
t1 = ts.utc(year, 12, 31)
t, y, details = eclipselib.lunar_eclipses(t0, t1, eph)

for ti, yi in zip(t, y):
    print(ti.utc_strftime('%Y-%m-%d %H:%M'),
          'y={}'.format(yi),
          eclipselib.LUNAR_ECLIPSES[yi])