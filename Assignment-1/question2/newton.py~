from math import *
import numpy as np
import matplotlib.pyplot as plt

def func(x):
	# return exp(x)
	# return  x*exp(-x*x)
	# return x*(1.0-x)
	return exp(x)-sin(pi*x)
def dx(x,c):
	return (func(x+c)-func(x-c))/(2*c);
	
x=[]
y=[]
er=[]
def NewRaph(xi,c,max_error):
	x.append(xi)
	er.append(func(xi));
	count=0

	while 1:
		print er 
		count+=1
		j=len(x)-1
		x.append(x[j]-(func(x[j])/dx(x[j],c)))
		er.append(func(x[j]))
		
		# if 1<2 :#and (fabs((er[len(er)-1]-er[len(er)-2])/er[len(er)-2]))>max_error:
		z=fabs((x[len(x)-1]-x[len(x)-2])/x[len(x)-2])
		if z<max_error :
			break

	for i in range(len(x)):
		print '%d %.10f %.10f'%(i+1,x[i],er[i])


#initial guess 2 and we can go on similarly root came to be -1.10721047376
NewRaph(2,0.001,0.000001)
print x[len(x)-1]
xval= np.arange(-10., 10.,0.01)
axes = plt.gca()
axes.set_xlim([-10,10])
axes.set_ylim([-10,10])
#print xval*(1.0-xval)
# plt.plot(xval,np.exp(xval)-np.sin(pi*xval), 'b')
plt.plot(xval,np.exp(xval)-np.sin(pi*xval), 'b')
plt.xticks(np.arange(min(xval), max(xval)+1, 2))
plt.axhline(0, color='black')
plt.axvline(0,color='black')
plt.savefig("22.png")

