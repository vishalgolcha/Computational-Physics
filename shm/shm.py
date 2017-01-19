# Runge Kutta 4 
from math import *
import numpy as np
import matplotlib.pyplot as plt


def func(y):
	return	-4*pi*pi*y 


def updater(initial,slope,deltax):
	return initial+(slope*deltax)


h=0.001
# t=10**(-5)      
# x= (-5.0)

y=[5]
p=[0]
xs=[0]

s_y  =[0,0,0,0]
s_p  =[0,0,0,0]


# taken initial y to be 5  


for i in range(0,10000,1):
	x=xs[i]
	s_p[0]  = func(y[i])    
	s_y[0] 	= p[i] 
    
	s_p[1]  = func(updater(y[i],s_y[0],h/2))    
	s_y[1] 	= updater(p[i],s_p[0],h/2)
   
	s_p[2]  = func(updater(y[i],s_y[1],h/2))    
	s_y[2] 	= updater(p[i],s_p[1],h/2)
	
	s_p[3]  = func(updater(y[i],s_y[2],h))    
	s_y[3] 	= updater(p[i],s_p[2],h)

	p_next  = p[i] + h*(s_p[0] + 2*s_p[1]  + 2*s_p[2]  + s_p[3])/6
	y_next  = y[i] + h*(s_y[0]+ 2*s_y[1] + 2*s_y[2] + s_y[3])/6

	p.append(p_next)
	y.append(y_next)
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
plt.plot(xs,y,'b')
# plt.xticks(np.arange(min(xval), max(xval)+1, 2))
# plt.axhline(0, color='black')
# plt.axvline(0,color='black')
plt.savefig("shm_positiontime.png")
plt.clf()
plt.plot(xs,p,'g')

plt.savefig("shm_velocitytime.png")


# printing out values of y at integral values of t 
print "printing out height values at integral t \n"

for i in range(10):
	print y[i*1000]   # time step was 1000 hence i*1000

#  results of the above print5
# 5.0
# 5.0
# 4.99999999999
# 4.99999999999
# 4.99999999999
# 4.99999999999
# 4.99999999999
# 4.99999999998
# 4.99999999998


# hence the y becomes less and less accurate although not by much as out initial position was 5