# Purpose: Plots distribution of Gaia alert object magnitudes versus date of observation
# Autor: Miroslav Mocak
# Slovak Organization for Space Activiities
# Date: 31/10/2016
# Acknowledgement: Thanks to all posting great stuff about python coding on internet
# Usage: run gaia_alerts.py

import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import numpy as np

def SetMatplotlibParams():
#	plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    plt.rc('font',**{'family':'serif','serif':['Times New Roman']})
    plt.rc('font',size=20.)
    plt.rc('lines',linewidth=2,markeredgewidth=2.,markersize=10)
    plt.rc('axes',linewidth=1.5)
    plt.rcParams['xtick.major.size']=8.
    plt.rcParams['xtick.minor.size']=4.
    plt.rcParams['figure.subplot.bottom']=0.13
    plt.rcParams['figure.subplot.left']=0.07	

# r is prepended to consider string as raw, otherwise \U is consider escape character , haha
file=open(r'alerts.csv','r')  # the latest csv file can be downloaded from here http://gsaweb.ast.cam.ac.uk/alerts/alerts.csv
reader = csv.reader(file) # creates reader object

next(file) # skip header

dates = []
alertmag = []

for row in reader: # iterates the rows of the file in orders
    dates.append(row[1])
    alertmag.append(float(row[4]))
#    print(row[1],row[5]) 
file.close()	

SetMatplotlibParams()

x = [dt.datetime.strptime(d,'%Y-%m-%d %H:%M:%S').date() for d in dates] # convert string to date

#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())

dmin = '2016-01-01 00:00:00'
dmax = '2016-11-10 00:00:00'
xmin = dt.datetime.strptime(dmin,'%Y-%m-%d %H:%M:%S').date()
xmax = dt.datetime.strptime(dmax,'%Y-%m-%d %H:%M:%S').date()
ymin = 13.
ymax = 21.

fig=plt.figure(1,figsize=(16,6))
plt.axis([xmin,xmax,ymin,ymax])

plt.plot(x,np.asarray(alertmag),'ro')

#plt.text(+16.e3,+1.e3,r"SOUTH")
	
plt.xlabel('Date of Observation')
plt.ylabel('Magnitude (Gaia G band)')
plt.legend(loc=1,prop={'size':14})
plt.title(r'Gaia Alerts')

name='gaiaalertsnow'
#dir=''
plt.savefig(name+'.png')

plt.show()

