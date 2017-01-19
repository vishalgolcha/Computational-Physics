from math import *
import numpy as np
import matplotlib.pyplot as plt
from random import *
n=100
p=0.01
t=[]
no=[]
no.append(n)
n_new=n
t.append(0)
for i in range(1,100):
	# for j in range(1,n_new):
	for j in range(1,n):
		g=random()
		if g<p:
			n-=1
	no.append(n)
	t.append(i)	

axes = plt.gca()

axes.set_xlim([0,100])
axes.set_ylim([0,n_new])
#print xval*(1.0-xval)
plt.plot(t,no,'b')
plt.xticks(np.arange(0, 100+1,10))
plt.axhline(0, color='black')
plt.axvline(0,color='black')
plt.savefig("radio4.png")