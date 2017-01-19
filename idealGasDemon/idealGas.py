from math import *
import numpy as np
import matplotlib as mpl
mpl.use('QT4Agg')
import matplotlib.pyplot as plt
from random import *

n=40 
vel=[]
E=10

for i in range(40):
	# r= 4*random()-2
	vel.append(((2*E)**(0.5))/40)

# print vel[0]
# print type(vel[0])
Energies=[]

demon_energy=0
total=0

def energy_change(initial,final):
	delta= (final**2 - initial**2)/2	
	return delta
y=[] 

energy=[]

for k in range(0,100,1):
	E=10
	for j in range(0,10000,1):
		total=0
		
		p_no= 0+(int)(40*random())
		r= 4*random()-2.0
		
		ch=vel[p_no]+r

		if energy_change(vel[p_no],ch) <= 0:
			demon_energy -=  energy_change(vel[p_no],ch)
			E+=energy_change(vel[p_no],ch)
			vel[p_no]+=r

		
		else :
			if demon_energy >= energy_change(vel[p_no],ch):
				demon_energy-=energy_change(vel[p_no],ch)
				E+=energy_change(vel[p_no],ch)
				vel[p_no]+=r
		
		energy.append(E)		
		y.append(j)
		total+=E

	break
	# Energies.append(total/10000)
	# y.append(k)



# xval= np.arange(-10., 10.,0.01)
# axes = plt.gca()
# axes.set_xlim([-10,10])
# axes.set_ylim([-10,10])
#print xval*(1.0-xval)
# plt.plot(xval,np.exp(xval)-np.sin(pi*xval), 'b')
plt.plot(y,energy,'b')
# plt.xticks(np.arange(min(xval), max(xval)+1, 2))
# plt.axhline(0, color='black')
# plt.axvline(0,color='black')
plt.savefig("IdealGasEnergy.png")		