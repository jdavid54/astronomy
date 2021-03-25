# links :
# https://docs.astropy.org/en/stable/constants/#module-astropy.constants
# https://docs.scipy.org/doc/scipy/reference/constants.html

import scipy.constants
import astropy.constants as const
import astropy.units as u

G = const.G
c = const.c
m_e = const.m_e  # electron mass
au = const.au
print(c, m_e, au, end='\n\n')

M_sun = const.M_sun   #sun mass
M_jup = const.M_jup   # jupiter mass
M_earth = const.M_earth   # earth mass
R_earth = const.R_earth

print(M_sun, M_jup, M_earth, R_earth)


def energy(m):
    E = m*c**2
    return E.to('MeV')

E = energy(m_e)
print('Energy:', E.to('MeV'))

def force_gravity(M,m,d):
    return G*M*m/d**2

f = force_gravity(M_sun, M_earth, au)
print('Pull force Sun-Earth:', f.to('N'))

f = force_gravity(M_earth, 1*u.kg , R_earth)
print('Pull force Earth-1kg mass:', f.to('N'))


def var_force(M,m,d):  # variation of force
    return -2*G*M*m/d**3   # unit : m3/(kg s2)*kg2/m3 = kg/s2

vf = var_force(M_earth, u.kg, au)
print('Force variation', vf)

def delta_force(m1,m2,r,d):
    return var_force(m1,m2,au)*2*r, -4*G*m1*m2*r/d**3

d = delta_force(M_earth, u.kg, R_earth, au)
print('Delta force between antipods', d[0].to('N'), d[1].to('N'))

def cohesion_force(m,r):    # force between half parts of a mass
    return G*m**2/(4*r**2)

cof = cohesion_force(M_earth, R_earth)
print('Earth cohesion force', cof.to('N'))


# Roche limit
# distance when cohesion force = delta_force
# if delta_force is greater than cohesion force, the mass will be shattered

def d_roch(M,m,d,r):
    return 2.52*r*(M/m)**(1/3)

roch = d_roch(M_sun, M_earth, au, R_earth)
print('Roch limit Sun-Earth', roch, roch/au)
