# -*- coding: utf-8 -*-
"""MFk-Means Implementation.ipynb

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

data = pd.read_csv('address/data.csv')
# processing the data as per requirements

# =================================================================== 
#       After data processing convert data into numpy array
#       data = data.values
# ===================================================================

"""# K-Means of Multidimensional class"""

class KMeans:
  def __init__(self,n_clusters=2,max_iter=100):
    self.n_clusters = n_clusters
    self.max_iter = max_iter
    self.centroids = None

  def fit_predict(self,X):

    random_index = random.sample(range(0,X.shape[0]),self.n_clusters)
    self.centroids = X[random_index]

    for i in range(self.max_iter):

      # assign clusters
      cluster_group,wcss = self.assign_clusters(X)
      old_centroids = self.centroids

      # move centroids
      self.centroids = self.move_centroids(X,cluster_group)

      # check finish
      if (np.array(old_centroids==self.centroids)).all():
        break

    return cluster_group,wcss

  def assign_clusters(self,X):
    cluster_group = []
    # distances = []
    wcss = 0

    for row in X:
      distances = []
      for centroid in self.centroids:

        # Manhattan distance formula to find distance between n-dimensional data points
        # as per mentioned in Research paper
        
        distances.append(np.dot(abs(row-centroid),1).sum())  

      min_distance = min(distances)

      wcss += (min_distance)**2
      index_pos=distances.index(min_distance)
      cluster_group.append(index_pos)

    return np.array(cluster_group),wcss

  def move_centroids(self,X,cluster_group):

    new_centroids = []
    cluster_type = np.unique(cluster_group)

    for type in cluster_type:
      new_centroids.append(X[cluster_group == type].mean(axis=0))
    return np.array(new_centroids) 

  def _inertia(self,X,n_clusters=2):

    km = KMeans(self.n_clusters,self.max_iter)
    _,dist_sqr = km.fit_predict(X)

    return dist_sqr

"""Elbow Test to find Optimal K"""

inertia = []
K = 10
n = range(2,K+1)

for k in n:
    km = KMeans(n_clusters=k)
    inertia.append(km._inertia(data,k))

#plotting elbow graph
plt.plot(n, inertia, 'bx-')
plt.xlabel('K')
plt.ylabel('Inertia')
plt.show()

"""Predicting at optimal K, let's say at 3"""

model = KMeans(n_clusters=3)
labels,_ = model.fit_predict(X) #prediction gives labels and inertia at that number of clusters
labels = pd.DataFrame(labels)

"""Printing the output"""

output = pd.concat((labels,data),axis=1)
output = output.rename({0:'labels'},axis=1)
output.head()
