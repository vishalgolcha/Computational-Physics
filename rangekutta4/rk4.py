from math import *
import numpy as np
import matplotlib.pyplot as plt

E=
h= 
m=
aa=                  #alpha
bb= 				 #beta

def const(x):
	return ((4*m*pi)/h)*((aa*x**2 + bb*x**4)-E)

# phi= d(si)/dx\
# //input phi and si for intital consitions even xo 
h=0.5
for x in range(-0.5,100,0.5):
	ks1= phi
	kp1= const(x)*(si)
	ks2= phi+(h*0.5*kp1)
	kp2= const(x)*(ks1*h*0.5)+kp1
	ks3= phi+(h*0.5*kp2)
	kp3= const(x)*(ks2*h*0.5)+kp1
	ks4= phi+(h*0.5*kp3)
	kp4= const(x)*(ks3*h*0.5)+kp1
	phi= phi+ (h/6)*(kp1+2*kp2+2*kp3+kp4)
	si = si + (h/6)*(ks1+2*ks2+2*ks3+ks4)
	ks1=ks2=ks3=ks4=0;
    kp1=kp2=kp3=kp4=0;
