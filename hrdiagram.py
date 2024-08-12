#!/usr/bin/env python
from __future__ import print_function,division
### http://www-personal.umich.edu/~mejn/computational-physics/
from matplotlib import pylab
from pylab import scatter,xlabel,ylabel,xlim,ylim,show
from numpy import loadtxt

data = loadtxt("../../Downloads/stars.dat", float)
x = data[:,0]
y = data[:,1]

scatter(x,y)
xlabel("Temperature")
ylabel("Magnitude")
xlim(0,13000)
ylim(-5,20)
show()
