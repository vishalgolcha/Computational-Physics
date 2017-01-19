from math import *
import numpy as np
import matplotlib.pyplot as plt

# a = raw_input();                
a=100.0
c = 0.0
d = pi/4
e = (d-c)/a                     
j = 1.0
z=e
# e=int(e)+1
# print e
co=1
while(z!=pi):
	if co==101:
		break
	# print z
	o = tan(z)/z
	# print o
	z+= e
	j +=o
	co+=1

h =tan(pi/4.0)/(pi/4.0)
# print h
# print exp(pi)
# print j
# print g
# print h
# print j
val = e*(j)-0.5*e*(1 + h)

# print "val :"
print val

# print "\n"
# answer 0.848971887309

xval= np.arange(0.01,pi,0.01)
axes = plt.gca()
axes.set_xlim([0,4])
axes.set_ylim([-10,10])
#print xval*(1.0-xval)
# plt.plot(xval,np.exp(xval)-np.sin(pi*xval), 'b')
plt.plot(xval,np.tan(xval)/xval, 'b')
plt.plot(0,1, 'b')
plt.xticks(np.arange(min(xval), max(xval)+1, 0.5))
plt.axhline(0, color='black')
plt.axvline(0,color='black')
# plt.savefig("32.png")