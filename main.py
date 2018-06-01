import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from numpy import complex as im
from numpy import absolute as cabs

def f(z, c):
	return z**2 + c

def isin_M(c, max_iter=75):
	z = im(0, 0)
	m = 4.0
	k = 10
	s = 2.0

	for i in range(max_iter):
		z = f(z, c)
		for i in range(k):
			if cabs(z) > m - (m-s)/k*i:
				return 1.0 - 1.0/k*i
	return 0.0

n = 500
low_r, hi_r = -2.0, 0.5
low_i, hi_i = -1.25, 1.25

def construct_grid(r_range, i_range, n):
	low_r, hi_r = r_range
	low_i, hi_i = i_range

	dr = (hi_r - low_r)/float(n)
	di = (hi_i - low_i)/float(n)

	return np.array(
		[[im(low_r+i*dr, hi_i-j*di) for j in range(n)] 
		for i in range(n)])

grid = construct_grid((low_r, hi_r), (low_i, hi_i), n)
visin_M = np.vectorize(isin_M)
M = visin_M(grid).T

fig, ax = plt.subplots()
img = ax.imshow(M, cmap='gray')
plt.show()
