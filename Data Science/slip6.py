# Write a python program to compute Euclidian Distance between two data points in a dataset. 
# [Hint: Use linalgo.norm function from NumPy] 
import numpy as np 
point_a = np.array((0,0,0))
point_b = np.array((1,1,1))

distance = np.linalg.norm(point_a - point_b)
print(distance)