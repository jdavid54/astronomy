import numpy as np

import matplotlib.dates as mdates
import datetime as dt

pi = np.pi
sin = np.sin
cos = np.cos
tan = np.tan
asin = np.arcsin
acos = np.arccos
atan = np.arctan
torad = pi/180
todeg = 1/torad

debug = False

def hauteur(L,D,H):  # latitude, déclinaison, angle horaire in rad -> hauteur en rad    
    return asin(sin(L)*sin(D)+cos(L)*cos(D)*cos(H))

lat = 48
D = -23.4  #-23.4
H = -20
h = hauteur(lat*torad,D*torad,H*torad)

print(h*todeg)

for h in range(0,95,5):
    print(h,'\t', hauteur(lat*torad,D*torad,h*torad)*todeg)
    
import matplotlib.pyplot as plt

def heigth_trace():
    x = np.linspace(-90, 90,1000)
    y = hauteur(lat*torad,D*torad,x*torad)*todeg
    plt.plot(x,y)
    plt.grid()
    plt.axis("equal")
    plt.show()

def azimuth(lat,dec):  # page 111
    return acos(-sin(dec)/cos(lat))*todeg

from datetime import datetime, timedelta

def declination(d=None):
    D = 23.4
    year = datetime.now().year
    spring_equinoxe = datetime(year,3,20)
    winter_solstice = datetime(year,12,21)
    if d == None :
        ini_time_for_now = datetime.now()
    else:
        ini_time_for_now = spring_equinoxe + timedelta(d)
    if debug:
        print(ini_time_for_now)
        
    #print((winter_solstice - spring_equinoxe).days, ' days from spring equinox to winter solstice')
    ref = spring_equinoxe
    # x = days from spring equinoxe    
    x = (ini_time_for_now - ref).days
    if x < 0:
        x += 365 
    if debug :
        print(x, ' days from last spring equinox')
    return asin(sin(D*torad)*sin(w*x*torad))*todeg
    
D = 23.4
az = azimuth(lat*torad, D*torad)
print(az)

w = 360/365.25   # angle by day

def double_yAxis():
    fig, ax1 = plt.subplots()

    x = np.linspace(0, 366, 1000)
    data1 = asin(sin(D*torad)*sin(w*x*torad))*todeg
    data2 = azimuth(lat*torad, asin(sin(D*torad)*sin(w*x*torad)))/15
    color = 'tab:red'
    ax1.set_xlabel('day from spring equinox')
    ax1.set_ylabel('declination (deg)', color=color)
    ax1.plot(x, data1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('azimuth in time (h)', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, data2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()

def dual_trace():
    fig, ax = plt.subplots()
    x = np.linspace(0, 366, 1000)
    y = asin(sin(D*torad)*sin(w*x*torad))*todeg
    z = azimuth(lat*torad, asin(sin(D*torad)*sin(w*x*torad)))/15
    ax.plot(x,y)
    ax.plot(x,z)
    
    #ax.set_ylim(-25,25)
    plt.grid()
    #plt.axis("equal")
    plt.show()
    
def rise_set():
    fig, ax = plt.subplots()
    x = np.linspace(0, 366, 1000)
    y = 12 - azimuth(lat*torad, asin(sin(D*torad)*sin(w*x*torad)))/15
    z = 12 + azimuth(lat*torad, asin(sin(D*torad)*sin(w*x*torad)))/15
    ax.plot(x,y)
    ax.plot(x,z)
    plt.title('Rise and set time')
    #ax.set_ylim(-25,25)
    plt.grid()
    #plt.axis("equal")
    plt.show()

rise_set()

def adjacent_traces():
    
    fig, axs = plt.subplots(2, 1, sharex=True)
    # Remove horizontal space between axes
    fig.subplots_adjust(hspace=0)
    x = np.linspace(0, 366, 1000)
    s1 = asin(sin(D*torad)*sin(w*x*torad))*todeg
    s2 = azimuth(lat*torad, asin(sin(D*torad)*sin(w*x*torad)))/15
    # Plot each graph, and manually set the y tick values
    axs[0].plot(x, s1, 'red')
    axs[0].grid(True, linestyle='-.')
    color = 'tab:red'
    #axs[0].set_xlabel('day from spring equinox')
    axs[0].set_ylabel('declination (deg)', color=color)
    #axs[0].set_yticks(np.arange(-0.9, 1.0, 0.4))
    #axs[0].set_ylim(-1, 1)

    axs[1].plot(x, s2, 'blue')
    color = 'tab:blue'
    axs[1].set_xlabel('Days from spring equinox')
    axs[1].set_ylabel('azimuth in time (h)', color=color)
    axs[1].grid(True, linestyle='-.')
    #axs[1].set_yticks(np.arange(0.1, 1.0, 0.2))
    #axs[1].set_ylim(0, 1)

    plt.show()
    
#double_yAxis()
#dual_trace()
#adjacent_traces()

# find sun declination for today
dec = declination()
print('declination :', "{:.2f}".format(dec))
# show azimuth for sunset & sunrise
az = azimuth(lat*torad,dec*torad)
sunrise = 180 - az
sunset = 180 + az
print("Azimuth : rise:{:.2f} set:{:.2f}".format(sunrise, sunset))

def azimuth2time(az):  # az in degrees, return sunrise time, sunset time, day length
    t = az/15
    return 12-t, 12+t, 2*t

rise, set, len = azimuth2time(az)
print("Time : rise at {:.2f} set at {:.2f}".format(rise, set))
print("Daylight time : {:.2f}".format(len))


# sun declination over a year
for d in range(0, 7*53, 7):
    #print('===========================================')
    day = datetime(2020,3,20) + timedelta(d)
    dec = declination(d)
    az = azimuth(lat*torad, dec*torad)
    #print(dec, az)
    rise, set, len = azimuth2time(az)
    print(day.date(), "rise:{:.2f} set:{:.2f} len:{:.2f} ".format(rise, set, len))
    
    
def rise_set2():
    fig, ax = plt.subplots()
    x = np.linspace(0, 366, 366)
    y = 12 - azimuth(lat*torad, asin(sin(D*torad)*sin(w*x*torad)))/15
    z = 12 + azimuth(lat*torad, asin(sin(D*torad)*sin(w*x*torad)))/15
    
    now = dt.datetime.now()
    equinox = datetime(2020,3,20)
    then = equinox + dt.timedelta(days=366)
    days = mdates.drange(equinox,then,dt.timedelta(days=1))
    #ax.text(0.0, 0.2, "Date", transform=ax.transAxes, 
    #        fontsize=14, fontname='Monospace', color='tab:blue')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y'))     #('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=15))
    plt.plot(days,y, label='rise')
    plt.plot(days,z, label='set')
    #color = 'tab:blue'
    ax.set_ylabel('time (h)', fontsize=12, fontname='Monospace', color='tab:blue')
    ax.set_xlabel('Date', fontsize=12, fontname='Monospace', color='tab:blue')
    plt.legend()
    plt.gcf().autofmt_xdate()
    
    
    #ax.plot(x,y)
    #ax.plot(x,z)
    plt.title('Rise and set time')
    #ax.set_ylim(-25,25)
    plt.grid()
    #plt.axis("equal")
    plt.show()

rise_set2()