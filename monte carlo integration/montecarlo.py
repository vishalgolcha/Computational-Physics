from math import *
import numpy as np
import matplotlib.pyplot as plt
from random import *

def mean(x):
	bu=0
	for i in range(len(x)):
		bu+=x[i]
	return bu/len(x)

def square_mean(x):
	bu=0
	for i in range(len(x)):
		bu+=(x[i]*x[i])
	return bu/len(x)

def func(x,a):
	return x*x*cos((pi*x)/a)*cos((pi*x)/a)

def dx(x,c):
	return (func(x+c)-func(x-c))/(2*c);

rand_m=[]
mean_mean=[]

a_eqn=3 # or can bes chosen as 3 

b= a_eqn/2.0
a= 0

for i in range(100,200,10):
	su=0
	for j in range(i):
		g=random()*(b-a) +a
		su+=func(g,a_eqn)
	mean_mean.append(su/i)

# print mean_mean
final_mean=mean(mean_mean)
final_var=square_mean(mean_mean)-(final_mean*final_mean)

# print final_mean
print("variance after monte carlo :")
print final_var
print("mean after monte carlo :")
print final_mean*2  # (multiplying with the limits)
print("final answer :")
#since (a/2-0)*(4/a) =2
print sqrt(final_mean*2)





# output when a=1
# variance after monte carlo :
# 3.32688514749e-07
# mean after monte carlo :
# 0.0322725674651
# final answer :
# 0.179645671991 +- sqrt(var)

# output when a=3
# variance after monte carlo :
# 7.49906756677e-05
# mean after monte carlo :
# 0.29643681544
# final answer :
# 0.544460113727


#plotting part


# xval= np.arange(-10., 10.,0.01)
# axes = plt.gca()
# axes.set_xlim([-10,10])
# axes.set_ylim([-10,10])
# #print xval*(1.0-xval)
# # plt.plot(xval,np.exp(xval)-np.sin(pi*xval), 'b')
# plt.plot(xval,np.exp(xval)-np.sin(pi*xval), 'b')
# plt.xticks(np.arange(min(xval), max(xval)+1, 2))
# plt.axhline(0, color='black')
# plt.axvline(0,color='black')
# plt.savefig(".png")


