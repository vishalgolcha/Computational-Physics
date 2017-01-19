from math import *
import numpy as np
import matplotlib.pyplot as plt
from random import *

xo=0
yo=1
step=0.1
def  func(x,y):
	return x*y 
y=[yo] #given
x=[xo] #given
f=[xo] #given
cnt=0

for i in range(40):
	y_i=y[cnt]+(func(x[cnt],y[cnt])*step)
	y.append(y_i)
	x.append(x[cnt]+step)
	f.append(func(x[cnt],y[cnt]))
	cnt+=1

print x
print y

	
xval= np.arange(-10., 10.,0.01)
axes = plt.gca()
axes.set_xlim([-10,10])
axes.set_ylim([-10,10])
#print xval*(1.0-xval)
# plt.plot(xval,np.exp(xval)-np.sin(pi*xval), 'b')
plt.plot(x,y,'b')
plt.xticks(np.arange(min(x), max(x)+1, 2))
plt.axhline(0, color='black')
plt.axvline(0,color='black')
plt.savefig("euler.png")