# improved euler  
from math import *
import numpy as np
import matplotlib.pyplot as plt


def func(q):
	return 0.12- (200/3)*q


def updater(initial,slope,deltax):
	return initial+(slope*deltax)


h=0.001
# t=10**(-5)      
# x= (-5.0)

q=[0]
xs=[0]

s_q  =[0,0]           

# taken initial q to be 5  


for i in range(0,500,1):
	x=xs[i]    
	s_q[0] 	= func(q[i])
	q_nt 	= q[i]+ s_q[0]*h         
	s_q[1] 	= func(q_nt)
	q_next  = q[i] + h*(s_q[0]+s_q[1])/2
	q.append(q_next)
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
plt.plot(xs,q,'b')
# plt.xticks(np.arange(min(xval), max(xval)+1, 2))
# plt.axhline(0, color='black')
# plt.axvline(0,color='black')
plt.savefig("capacitor.png")