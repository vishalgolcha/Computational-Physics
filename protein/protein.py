from math import *
import numpy as np
import matplotlib as mpl
mpl.use('QT4Agg')
import matplotlib.pyplot as plt
from random import *

Matrix = [[0 for x in range(25)] for y in range(25)]
# taking a 25*25grid for simulation 


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def  bolt_prob(u):
	return exp((-1*u)/(10)) # temperature was taken as 10 u is change in enrgy

def valid(x,y ):
	if x>=0 and x <25 and y >=0 and y<25:
		return True
	else:
		return False

def Neighbour_Energy(i,j):
	ans=0
	if j-1 >= 0 and parent_Matrix[i][j-1]==-1 and Matrix[i][j-1]==1 :
		ans+= 1000
	if j<9 and parent_Matrix[i][j+1]==-1 and Matrix[i][j+1]==1 :
		ans+= 1000
	if i<9 and parent_Matrix[i+1][j]==-1 and Matrix[i+1][j]==1:
		ans+= 1000
	if i>0 and parent_Matrix[i-1][j]==-1 and Matrix[i-1][j]==1:
		ans+= 1000
	return ans

av=[]
av_time=[]

x_pos=[0 for i in range(25)]
y_pos=[0 for i in range(25)]

Matrix[0][0] =1 # signifies occupied
parent_Matrix=[[-1 for x in range(25)] for y in range(25)] 

# create a random walk to simulate protein creation

for i in range(24):
	while(True):
		dx= 2*(random()-0.5)	
		dy= 2*(random()-0.5) 
		if dx<0 :
			dx= -1
		else :
			dx= 1
		
		if dy<0 :
			dy= -1
		else :
			dy= 1		

		if valid(x_pos[i]+dx,y_pos[i]+dy) and Matrix[x_pos[i]+dx][y_pos[i]+dy]==0 :
			
			print dx,dy
			Matrix[x_pos[i]+dx][y_pos[i]+dy]=1
			x_pos[i+1]=x_pos[i]+dx
			y_pos[i+1]=y_pos[i]+dy
			parent_Matrix[x_pos[i]+dx][y_pos[i]+dy]=i
			# print x_pos[i+1]
			# print y_pos[i+1]
			break

# ans is initial enrgy
ans=0

for i in range(10):
	for j in range(10):
		ans+=Neighbour_Energy(i,j)

print ans		

for k in  range(10):
  	
	Initial_Energy = ans/2
	# print Initial_Energy

	delta_E=0

	plt.ion()

	Es=[Initial_Energy]
	ts=[0]
	tc=0
	
	# chose a random particle

	
	
	while True:
		particle_no= (int)(0+25*random())
		tc+=1
		delta_E=0

		# try to change location of particle

		rand_x = 2*(random()-0.5)
		rand_y = 2*(random()-0.5)
	 	

		if delta_E<0:
			
			delta_E-=Neighbour_Energy(x_pos[particle_no],y_pos[particle_no]);
	 		delta_E+=Neighbour_Energy(x_pos[particle_no]+rand_x,y_pos[particle_no]+rand_y)
			Matrix[x_pos[particle_no]+rand_x][y_pos[particle_no]+rand_y] =1
			Matrix[x_pos[particle_no]][y_pos[particle_no]] =0

			Initial_Energy+=delta_E		
			# continue;
		elif delta_E>0:
			g=random()

			if g < bolt_prob(delta_E):
				delta_E-=Neighbour_Energy(x_pos[particle_no],y_pos[particle_no]);
	 			delta_E+=Neighbour_Energy(x_pos[particle_no]+rand_x,y_pos[particle_no]+rand_y)
				Matrix[x_pos[particle_no]+rand_x][y_pos[particle_no]+rand_y] =1
				Matrix[x_pos[particle_no]][y_pos[particle_no]] =0
				# print "bolt energy"
				# print bolt_prob(delta_E)
				# print "\n"
				Initial_Energy+=delta_E 
				# print "accepted"		
		
		Es.append(Initial_Energy)
		ts.append(tc)
		if tc==500:
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
	# axes = plt.gca()
	# axes.set_xlim([min(ts),max(ts)+3])
	# axes.set_ylim([min(Es),max(Es)+3])
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
	# plt.xticks(np.arange(min(ts), max(ts)+1, 2000))
	# plt.axhline(0, color='black')
	# plt.axvline(0,color='black')
	plt.savefig("Energyplot0"+str(k)+".png")

	plt.clf()


	ave=mean(Es)
	av.append(ave)


final_energy_Average=mean(av)
print "equillibrium energy"
print final_energy_Average






































#Author 
#Vishal Golcha 