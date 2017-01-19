from math import *
import numpy as np
import matplotlib as mpl
mpl.use('QT4Agg')
import matplotlib.pyplot as plt
from random import *


a = [[0 for x in range(7)] for y in range(7)]


# a = [[0]*7]*7


for i in range(7):
	a[i][0]= -1
	a[i][6]=  1

a[0][1]= -0.67
a[0][2]= -0.33
a[0][4]=  0.33
a[0][5]=  0.67

a[6][1]= -0.67
a[6][2]= -0.33
a[6][4]=  0.33
a[6][5]=  0.67

for i in a:
	print i
	print "\n"


for i in range(10000):
	for i in range(1,6,1):
		for j in range(1,6,1):
			a[i][j] = (a[i-1][j]+a[i+1][j+1]+a[i-1][j-1]+a[i][j-1])/4


for i in a:
	print i
	print "\n"

plt.matshow(np.array(a), fignum=100, cmap=plt.cm.gray)
plt.show()