from math import *
import numpy as np
import matplotlib as mpl
# from matplotlib import mpl
mpl.use('QT4Agg')
import matplotlib.pyplot as plt
from random import *

Matrix = [[0 for x in range(100)] for y in range(100)]

def  bolt_prob(u):
	return exp((-1*u)/(10.0))
	# return exp((-1*u)/(2.269185))

def Neighbour_Energy(i,j):
	ans=0
	if j-1 >= 0:
		ans+= Matrix[i][j]*Matrix[i][j-1]
	if j<99:
		ans+= Matrix[i][j]*Matrix[i][j+1]
	if i<99:
		ans+= Matrix[i][j]*Matrix[i+1][j]
	if i>0:
		ans+= Matrix[i][j]*Matrix[i-1][j]
	return ans
  
for i in range(100):
	for j in range(100):
		g=random()
		if g>0.5 :
			Matrix[i][j]= -1
		else:
			Matrix[i][j]= 1 
# print Matrix

ans=0

for i in range(100):
	for j in range(100):
		ans+=Neighbour_Energy(i,j)

Initial_Energy = ans/2
print Initial_Energy

delta_E=0

plt.ion()
magnetisation=sum([sum(x) for x in Matrix])
Es=[Initial_Energy]
ts=[0]
tc=0
Ms=[magnetisation]

while True:
	tc+=1
	delta_E=0
	rand_x = 0+(int)((99)*random())
	rand_y = 0+(int)((99)*random())
 	
 	# print rand_x ,rand_y
 	# flip the spin 
 	delta_E-=Neighbour_Energy(rand_x,rand_y)
 	Matrix[rand_x][rand_y]*=-1
	delta_E+=Neighbour_Energy(rand_x,rand_y);
	

	delta_M=0

	if delta_E<0:
		Initial_Energy+=delta_E		
		delta_M= 2*Matrix[rand_x][rand_y]
		# continue;
	elif delta_E>0:
		g=random()

		if g < bolt_prob(delta_E):
			# print "bolt energy"
			# print bolt_prob(delta_E)
			# print "\n"
			Initial_Energy+=delta_E 
			delta_M= 2*Matrix[rand_x][rand_y]
			# print "accepted"
		else:
			# re flip
			Matrix[rand_x][rand_y]*=-1
			# print "re flipped"
	
	
	Es.append(Initial_Energy)
	ts.append(tc)
	Ms.append(magnetisation+delta_M)
	if tc==16000:
		
		x=np.array(Matrix);
		
		# print x

		cmap = mpl.colors.ListedColormap(['red','blue','blue'])
		bounds=[-1,0,1]
		norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

		# tell imshow about color map so that only set colors are used
		img = plt.imshow(x,interpolation='nearest',
		                    cmap = cmap,norm=norm)

		plt.savefig('finalspinstate410010.png')
		plt.clf()
		break;
	# print delta_E , Initial_Energy
	# xval= np.arange(-10., 10.,0.01)
axes = plt.gca()
axes.set_xlim([min(ts),max(ts)+3])
axes.set_ylim([min(Es),max(Es)+3])
#print xval*(1.0-xval)
# plt.plot(xval,np.exp(xval)-np.sin(pi*xval), 'b')

# change figure size 
# Get current size
# fig_size = plt.rcParams["figure.figsize"]
 
# Prints: [8.0, 6.0]
# print "Current size:", fig_size
# plt.rcParams["figure.figsize"] = [20,15]
# fig_size[0] = 12
# fig_size[1] = 9
# plt.rcParams["figure.figsize"] = fig_size

plt.plot(ts,Es,'b')
plt.xticks(np.arange(min(ts), max(ts)+1, 2000))
plt.axhline(0, color='black')
plt.axvline(0,color='black')
plt.savefig("Energyplot5310010.png")

plt.clf()

# Magnetisation plot
# axes = plt.gca()
# axes.set_xlim([min(ts),max(ts)+3])
# axes.set_ylim([min(Ms),max(Ms)+3])
# plt.plot(ts,Ms,'r')
# plt.xticks(np.arange(min(ts), max(ts)+1, 2000))
# plt.axhline(0, color='black')
# plt.axvline(0,color='black')
# plt.savefig("magnet_plot6.png")




























#Author 
#Vishal Golcha 