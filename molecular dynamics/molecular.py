from math import *
import numpy as np
import matplotlib as mpl
mpl.use('QT4Agg')
import matplotlib.pyplot as plt
from random import *
#  20 particles 10 * 10 grid
sig=1
eps=1
# grid 12 *12 assume
# initial velocity in 1 in x and y
pys=[[0] for i in range(10)]
pxs=pys
vxs=[[1] for i in range(10)]
vys=[[1] for i in range(10)]
axs=pys
ays=pys

distx=[[0 for x in range(10)] for y in range(10)] #distance matrix
disty=[[0 for x in range(10)] for y in range(10)] #distance matrix

def distance(xs,ys,t):
	for i in range(20):
		for j in range(20):
			distx[i][j]= xs[i][t]-x[j][t]
			disty[i][j]= ys[i][t]-ys[j][t]

def rcalc(x,y):
	return  (x**2+y**2)**0.5

def force(x,y):
	r= rcalc(x,y)
	return 24*(2*((1/r)**13)-(1/r)**7)

# putting it on the boundary 
for i in range(5):
	pxs[i]= 2*i
	pys[i]= 10

for i in range(5):
	pxs[5+i]= 10
	pys[5+i]= 10-2*i

for i in range(5):
	pxs[10+i]= 10-2*i
	pys[10+i]= 0

for i in range(5):
	pxs[15+i]= 0
	pys[15+i]= 2*i

# randomized displacements and velocities  

for i in range(20):
	
	dx= random()-0.5
	dy= random()-0.5
	
	dvx=2*(random()-0.5)
	dvy=2*(random()-0.5)
	
	pxs[i].append(pxs[i][0]+dx)
	pys[i].append(pys[i][0]+dy)
	
	vxs[i].append(vxs[i][0]+dvx)
	vys[i].append(vys[i][0]+dvy)


t=1 # now since two values added to the lists already

# temporary lists for forces you need to have
xs=[0 for i in range(20)]
ys=[0 for i in range(20)]
fx=[0 for i in range(20)]
fy=[0 for i in range(20)]
vx=[0 for i in range(20)]
vy=[0 for i in range(20)]

#  one time step have to put this in a loop 
distance(pxs,pys,1)

for i in range(20):
	for j in range(20):
		if j!=i:
			r=rcalc(distx[i][j],distx[i][j])
			if r<=3:
				f=force(r)
				fx[i]+= f*pxs[i][t]/r   
				fy[i]+= f*pys[i][t]/r
	axs[i].append(fx[i])
	ays[i].append(fy[i])			

# use verlet after this 
# boundary consition + no simultaneous updates here remember 
# forces have been calculated 
