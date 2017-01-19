from math import *
import numpy as np
import matplotlib.pyplot as plt

# initialize
N0 =20001
NP =10000
N1 =200

n = N0
h = 1.0/NP
h2 = h*h/2
kappa = 39.5

t  = [0]
x  = [1.97]
y  = [0]
r  = [x[0]]
vx = [0]
vy = [0.816]
gx = [-kappa/(r[0]**2)]
gy = [0]

for i in range(n):
  t.append(h*(i+1))
  x.append(x[i]+h*vx[i]+h2*gx[i])
  y.append(y[i]+h*vy[i]+h2*gy[i])
  r.append((x[i+1]*x[i+1]+y[i+1]*y[i+1])**0.5);
  r3 = r[i+1]**3;
  gx.append((-1*kappa*x[i+1])/r3);
  gy.append((-1*kappa*y[i+1])/r3);
  vx.append(vx[i]+h*(gx[i+1]+gx[i])/2)
  vy.append(vy[i]+h*(gy[i+1]+gy[i])/2)

trefined=[] 
rrefined=[]
xrefined=[]
yrefined=[]


# for i in range(3500,4000,1):
#   print x[i]

# for i in range(3500):
#   xrefined.append(x[i])
#   yrefined.append(y[i])


plt.plot(x,y,'g')


# # for i in range(1000):
#   # print x[i]

# # for i in range(100):
# #   trefined.append(i)
# #   rrefined.append(r[i*200])

# # axes = plt.gca()
# # # axes.set_xlim([0,n+1])
# # # axes.set_ylim([-10,10])
# # plt.plot(trefined,rrefined,'b')
# # plt.xticks(np.arange(0,100,20))
# # # print np.arange(0,20000,200)
# # plt.yticks(np.arange(min(rrefined), max(rrefined)+1,1))
# # # plt.axhline(0, color='black')
# # # plt.axvline(0,color='black')

plt.savefig("verletnew.png")


































#author
#vishal golcha