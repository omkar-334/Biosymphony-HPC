import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

system_points = np.loadtxt('Ar_1681_50_50_50.xyz', skiprows=2, usecols = (1,2))

box_size = [50,50]
cutoff_distance = 5

kdtree = scipy.spatial.KDTree(system_points, boxsize=box_size)

distances, neighbours = kdtree.query(query_points, k=100, distance_upper_bound=cutoff_distance)

distances_zero = distances[0]
neighbours_zero = neighbours[0]

mask = ~np.isinf(distances_zero)

nighbours_masked = neighbours_zero[mask]
neighbours_x = []
neighbours_y = []

for index in nighbours_masked:
  neighbours_x.append(system_points[index][0])
  neighbours_y.append(system_points[index][1])

system_graph = plt.scatter(system_points[:, 0], system_points[:,1])
query_points = np.array([[25,0]])

#query_points[:,0], query_points[:,1]
query_graph = plt.scatter(query_points[:,0], query_points[:,1])
neighbours_graph = plt.scatter(neighbours_x, neighbours_y )