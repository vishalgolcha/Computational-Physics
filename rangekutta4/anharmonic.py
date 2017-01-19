# Runge Kutta 4 
from math import *
import numpy as np
import matplotlib.pyplot as plt

a= 0.5 		# reduced
b= 0.25 	# reduced
E= 200

# hr is h reduced  
def V(x):
	return a*(x**2)+b*(x**4)


def func(x,phi):
	return ((2/7.6199)*(V(x)-E)*phi)


def updater(initial,slope,deltax):
	return initial+(slope*deltax)


h=0.001
t=10**(-5)      
x= (-5.0)

phi=[t]
si=[0]
xs=[x]

s_phi =[0,0,0,0]
s_si  =[0,0,0,0]

for i in range(0,10000,1):
	x=xs[i]
	s_si[0]  = func(x,phi[i])    
	s_phi[0] = si[i] 
    
	s_si[1]  = func(x+h/2,updater(phi[i],s_phi[0],h/2))    
	s_phi[1] = updater(si[i],s_si[0],h/2)
   
	s_si[2]  = func(x+h/2,updater(phi[i],s_phi[1],h/2))    
	s_phi[2] = updater(si[i],s_si[1],h/2)
	
	s_si[3]  = func(x+h,updater(phi[i],s_phi[2],h))    
	s_phi[3] = updater(si[i],s_si[2],h)

	si_next  = si[i]  + h*(s_si[0] + 2*s_si[1]  + 2*s_si[2]  + s_si[3])/6
	phi_next = phi[i] + h*(s_phi[0]+ 2*s_phi[1] + 2*s_phi[2] + s_phi[3])/6

	si.append(si_next)
	phi.append(phi_next)
	xs.append(x+h)

# taking out 100 values for the plot 

x_plot=[]
phi_plot=[]
si_plot=[]




# xval= np.arange(-10., 10.,0.01)
# axes = plt.gca()
# axes.set_xlim([-10,10])
# axes.set_ylim([-10,10])
#print xval*(1.0-xval)
# plt.plot(xval,np.exp(xval)-np.sin(pi*xval), 'b')
plt.plot(xs,phi,'b')
# plt.xticks(np.arange(min(xval), max(xval)+1, 2))
# plt.axhline(0, color='black')
# plt.axvline(0,color='black')
plt.savefig("AnharmonicOscillator_again.png")