import numpy as np
import scipy.constants
import astropy.constants
import matplotlib.pyplot as plt

G = scipy.constants.gravitational_constant
#print('G:',G)
M = astropy.constants.M_earth.value  
#print('M:',M.name, M.value,M.uncertainty, M.unit, M.reference) # lower case
GM = astropy.constants.GM_earth.value
#print('GM=G*M:', G*M.value)
#print(GM.value)
R = astropy.constants.R_earth.value/1000  #km
print(R)
zoom = True

def show_all():
    fig = plt.figure(0)
    ax = fig.add_subplot(111, aspect='equal')
    ax = plt.gca()
    circle = plt.Circle((0, 0), R, color='lightgrey',fill=False)
    ax.add_patch(circle)
    #ax.legend([circle], ['Terre'])
    if zoom:
        z_min, z_max = min(toggle*R/2, toggle*(R+limit/2)), max(toggle*R/2, toggle*(R+limit/2))
        ax.set_xlim(z_min, z_max)
        ax.set_ylim((-limit/2, limit/2))
        if zoom2 or D <10000:
            ax.set_xlim(min(toggle*5500, toggle*7500),max(toggle*5500, toggle*7500))
            ax.set_ylim(-1500, 1500)
    else :
        ax.set_xlim((-limit, limit))
        ax.set_ylim((-limit, limit))
    #plt.plot(0,0,'ro',label='Terre')
    plt.plot(toggle*(h0+R),0,'b+', label='cible')    
    if not zoom:
        plt.plot(toggle*(h1+R)*np.cos(theta*np.pi/180+np.pi), toggle*(h1+R)*np.sin(theta*np.pi/180+np.pi),'y*', label='fantome')
    plt.plot(toggle*(h2+R)*np.cos(theta*np.pi/180), toggle*(h2+R)*np.sin(theta*np.pi/180),'g*', label='chasseur')
    ax.legend()
    plt.show()

# init nombre demi-orbite, ecart angulaire total
n = 0
theta = 0
zoom2 = False

h0 = 500 # altitude cible
print('Altitude de la cible(km) = ',h0)
h1 = 240 # altitude chasseur
h2 = h1
print('Altitude du chasseur(km)=',h1)
a = (h0 + R) * 1000     # en mètres
t0 = 2*np.pi*np.sqrt(a**3/GM)
print('Période de révolution cible : ', round(t0))
# chasseur
A = (h1 + R) * 1000   # en mètres
print()
man = 0
ex_D = (h0-h1)*1000
D = ex_D
toggle=1
ops = [[n,man,h1,h2,A,theta,D,ex_D,toggle]]
while True:    
    man += 1
    limit = max(h0, h1)+R+100
    tn = 2*np.pi*np.sqrt(A**3/GM)
    print('\nOrbite ',h1,'/', h2, n, man, theta)
    print('Période de révolution chasseur après manoeuvre',man,': ', round(tn))

    #3 Ecart angulaire au début après une demi-orbite n=0.5
    dT = (t0 - tn)/2
    print('dT = ', dT)
    #4 écart angulaire
    d_theta = dT*360/t0
    print('d_theta = ', d_theta)
    if dT < 0 :
        print('Chasseur en retard')
    else:
        print('Chasseur en avance')
    #save_theta = theta
    
    theta += d_theta
    print('Theta = ', theta)

    #5 distance chasseur-cible
    save_D = D    
    D = np.sqrt(a**2 + A**2 - 2*a*A*np.cos(theta*np.pi/180))    # en mètres    
    print('Distance cible-chasseur(m) = ', round(D))
    if D < ex_D : print('Good one!')
    if D < 100:   #objectif atteint
         print(theta, D, n)
         break
    else:
        #6 Sommation nombre orbites
        n += 0.5    
        show_all()
        #print('n,man,h1,h2,A,theta,D,ex_D,toggle')
        #print('Saving previous data :',ops[-1])
        # next round
        toggle *= -1
        h1 = h2        
        #7 Fixer altitude du point opposé de l'orbite du chasseur pour manoeuvre suivante
        
        h2 = input('Altitude opposé ou z ou \'u\'n to undo n steps = ')
        if h2 == '0' : break 
        if h2[0] == 'z':
            zoom2 = not zoom2
        # u2 will undo 2 manoeuvers in ops
        # undo the n last manoeuver, restore all   
        if h2[0] == 'u': 
            steps = 1
            if len(ops)>1: # if more than one manoeuver left
                if len(h2)>1 :
                    steps = int(h2[1:])
                for s in range(steps):
                    #delete last data
                    ops.pop()
                    #ops = [(n,man,h1,h2,A,theta,D,ex_D,toggle)]
            else:
                print('Cannot undo further !')
        if h2[0] in 'uz':    
            # reload the last manoeuver
            n = ops[-1][0]
            man = ops[-1][1]
            h1 = ops[-1][2]
            h2 = ops[-1][3]
            A = ops[-1][4]
            theta = ops[-1][5]
            D = ops[-1][6]
            ex_D = ops[-1][7]
            toggle = ops[-1][8]              
        else: # ok to continue
            h2 = int(h2)                                   
            l = []
            l.append(n)
            l.append(man)
            l.append(h1)
            l.append(h2)
            A = ((h1+h2)/2 + R) * 1000
            l.append(A)
            l.append(theta)
            l.append(D)
            l.append(ex_D)
            l.append(toggle)
            # save in ops
            ops.append(l)
            #print('ops:',ops)
            ex_D = D
print('End of mission !')