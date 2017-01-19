from math import *
import numpy as np
import matplotlib.pyplot as plt

# a = raw_input();                
a=25.0
c = 0.0
d = pi
e = (d-c)/a                     
j = 0.0
# e=int(e)+1
# print e
z=0.0
co=1
while(z!=pi):
	if co==27:
		break
	# print z
	o = exp(z) -cos(pi*z)
	z+= e
	j +=o
	co+=1
g = exp(0)-cos(pi*0)
h = exp(pi)-cos(pi*pi)
# print exp(pi)
# print j
# print g
# print h
val = e*(j)-0.5*e*(g + h)

# print "val :"
print val
# print "\n"

# answer 22.3050065058

xval= np.arange(0,pi,0.01)
axes = plt.gca()
axes.set_xlim([0,4])
axes.set_ylim([-10,10])
#print xval*(1.0-xval)
# plt.plot(xval,np.exp(xval)-np.sin(pi*xval), 'b')
plt.plot(xval,np.exp(xval)-np.cos(pi*xval), 'b')
plt.xticks(np.arange(min(xval), max(xval)+1, 0.5))
plt.axhline(0, color='black')
plt.axvline(0,color='black')
plt.savefig("31.png")