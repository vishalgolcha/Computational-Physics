from math import *
import numpy as np
import matplotlib as mpl
mpl.use('QT4Agg')
import matplotlib.pyplot as plt
from random import *

Matrix = [[0 for x in range(10)] for y in range(10)]

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def  bolt_prob(u):
	return exp((-1*u)/(2))
	# return exp((-1*u)/(2.269185))

def Neighbour_Energy(i,j):
	ans=0
	if j-1 >= 0:
		ans+= Matrix[i][j]*Matrix[i][j-1]
	if j<9:
		ans+= Matrix[i][j]*Matrix[i][j+1]
	if i<9:
		ans+= Matrix[i][j]*Matrix[i+1][j]
	if i>0:
		ans+= Matrix[i][j]*Matrix[i-1][j]
	return ans

av=[]
av_time=[]

for k in  range(10):
  
	for i in range(10):
		for j in range(10):
			g=random()
			if g>0.5 :
				Matrix[i][j]= -1
			else:
				Matrix[i][j]= 1 
	# print Matrix

	ans=0

	for i in range(10):
		for j in range(10):
			ans+=Neighbour_Energy(i,j)

	Initial_Energy = ans/2
	# print Initial_Energy

	delta_E=0

	plt.ion()

	magnetisation=sum([sum(x) for x in Matrix])
	Es=[Initial_Energy]
	ts=[0]
	tc=0
	Ms=[magnetisation/(100.0)]

	while True:
		tc+=1
		delta_E=0
		rand_x = 0+(int)((9)*random())
		rand_y = 0+(int)((9)*random())
	 	
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
		Ms.append(magnetisation/(100.0)+(delta_M/100.0))
		if tc==8000:
			break;
		# x=np.array(Matrix);
		
		# # print x

		# cmap = mpl.colors.ListedColormap(['black','blue','white'])
		# bounds=[-1,0,1]
		# norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

		# # tell imshow about color map so that only set colors are used
		# img = plt.imshow(x,interpolation='nearest',
		#                     cmap = cmap,norm=norm)

		# plt.pause(0.05)

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
	# print j 
	plt.plot(ts,Es,'b')
	plt.xticks(np.arange(min(ts), max(ts)+1, 2000))
	plt.axhline(0, color='black')
	plt.axvline(0,color='black')
	plt.savefig("Energyplot0"+str(k)+".png")

	plt.clf()


	axes = plt.gca()
	axes.set_xlim([min(ts),max(ts)+3])
	axes.set_ylim([min(Ms),max(Ms)])
	plt.plot(ts,Ms,'r')
	plt.xticks(np.arange(min(ts), max(ts)+1, 2000))
	plt.axhline(0, color='black')
	plt.axvline(0,color='black')
	plt.savefig("magnet_plot0"+str(k)+".png")
	plt.clf()	

	ave=mean(Es)
	av.append(ave)

		
	for i in range(8000):
		if ((Es[i]-ave)/100.0) < 0.01:
			av_time.append(i)
			break;

final_energy_Average=mean(av)
print "equillibrium energy"
print final_energy_Average
print "time_array"
print av_time
print "mean_time"
final_time_average=mean(av_time)
print final_time_average






































#Author 
#Vishal Golcha 