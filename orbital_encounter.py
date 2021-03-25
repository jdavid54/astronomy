# https://docs.scipy.org/doc/scipy/reference/constants.html
# https://het.as.utexas.edu/HET/Software/Astropy-1.0/constants/index.html
import numpy as np
import scipy.constants
import astropy.constants
    
def home():
    i = input('On rentre à la maison ? O/n')
    if i!='n':
        return True

G = scipy.constants.gravitational_constant
#print('G:',G)
M = astropy.constants.M_earth.value  
#print('M:',M.name, M.value,M.uncertainty, M.unit, M.reference) # lower case
GM = astropy.constants.GM_earth.value
#print('GM=G*M:', G*M.value)
#print(GM.value)
R = astropy.constants.R_earth.value/1000  #km
ve = 2650   # vitesse d'éjection du propergol
md = 95000  # masse du satellite au départ
mr = 8000   # masse de propergol restant
mp = 8000   #masse de propergol embarqué
h0 = 200    # altitude de départ
h2 = h0
print('Altitude de départ(km) = ',h0)
h1 = 300   # altitude visée
print('Altitude visée (km)=',h1)

while True:    
    #55
    a0 = (h0+R)*1000
    if (h1==h0) and (h2==h0):
        print('Vous êtes en orbite circulaire: ',h0)
    if (h1==h2) and (h1!=h0):
        print('Vous restez en orbite ',h2,'/',h0)
    if (h1!=h2) and (h1!=h0):
        print('Vous amorcez l\'orbite ',h0,'/',h1)
    # visée orbite circulaire    
    if (h1!=h2) and (h1==h0):
        print('Vous amorcez l\'orbite circulaire ',h0)
    #60    
    v0 = np.sqrt(GM/a0)
    print('v0 = ', v0, ',alt = ', h0)
    r2 = h2 + R
    a1= (h0+h2)/2 + R
    vr = v0*np.sqrt(r2/a1)
    print('vr = ', vr)
    r1 = h1 + R
    a2 = (h0+h1)/2 + R
    vn = v0*np.sqrt(r1/a2)
    print('vn= ', vn)
    #95
    dv = abs(vn-vr)
    x = np.exp(dv/ve)
    mp = md * (1-1/x)
    print('mp = ', mp)
    #110
    mr = mr - mp
    md = md - mp
    if h1 == 120 and home(): break
    #120
    v1 = vn * a0 / (r1*1000)
    print('v1 = ', v1 ,',alt = ', h1)
    vc = np.sqrt(GM / (r1*1000))
    print('vc = ', vc)
    ar = R + (120 + h1)/2
    vp = vc * np.sqrt(6498/ar)  # 6498 = R + 120 altitude
    dvr = abs(v1-vp)
    x = np.exp(dvr/ve)
    mpr = md * (1-1/x)
    print('mpr = ', mpr)
    if mpr >= mr:
        print('Manoeuvre impossible')
        mr = mr + mp
        md = md +mp
    else:
        print('mr = ',mr,'md = ',md)
        h2 = h0
        h0 = h1
    print()
    #195
    print('Votre altitude actuelle : ', h0)
    h1 = int(input('Altitude suivante = '))
    if h1==0: break
    while h1<120:
        print('Altitude trop basse')
        h1=int(input('Redonnez une valeur >= 120 : '))