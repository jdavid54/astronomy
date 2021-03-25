#https://rhodesmill.org/skyfield/almanac.html#transits

from skyfield.api import load
from skyfield import almanac
# ['New Moon', 'First Quarter', 'Full Moon', 'Last Quarter']
#print('Load bsp file ...')
#eph = load('https://naif.jpl.nasa.gov/pub/naif/JUNO/kernels/spk/de421.bsp')
eph = load('de421.bsp')
ts = load.timescale()
year = 2021
print('\nMoon phases in',year)
t0 = ts.utc(year, 1, 1)
t1 = ts.utc(year, 12, 31)
t, y = almanac.find_discrete(t0, t1, almanac.moon_phases(eph))
#print(t.utc_iso())
#print(y)
#print([almanac.MOON_PHASES[yi] for yi in y])
for ti, yi in zip(t, y):
    #print(ti.utc_iso(), almanac.MOON_PHASES[yi])
    print(ti.utc_strftime('On %Y,%b %d at %H:%M:%S (UTC)'), almanac.MOON_PHASES[yi])
    if almanac.MOON_PHASES[yi] == 'Last Quarter':
        print()
    