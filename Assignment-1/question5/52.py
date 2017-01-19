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
A= 1.0-(1.0/exp(pi))
def func(x):
	# return x*x*cos((pi*x)/a)*cos((pi*x)/a)
	return A*exp(x)/((x**2 +cos(x)**2))

def dx(x,c):
	return (func(x+c)-func(x-c))/(2*c);

rand_m=[]
mean_mean=[]
 
# print A
b= 1
a= 0
for i in range(10000,200000,1000):
	su=0
	for j in range(i):
		g=random()
		x_in_y= -1*log(1-(g*A))
		su+=func(x_in_y)
	mean_mean.append(su/i)

# print mean_mean
final_mean=mean(mean_mean)
final_var=square_mean(mean_mean)-(final_mean*final_mean)

# print final_mean
print("variance after monte carlo :")
print final_var
print("mean after monte carlo :")
print final_mean  


# answer for the integral 1.5813996725

# print("final answer :")
# #since (a/2-0)*(4/a) =2
# print sqrt(final_mean*2)





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


