# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:01:20 2016

@author: Shipeng
"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn import metrics
from matplotlib.patches import FancyArrowPatch
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d import Axes3D

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)



mydata = open('com.txt', 'r')

time = []
x = []
y = []
z = []
Xlist = []

for line in mydata:
    string = line.rstrip()
    myline = string.split()
    time.append(float(myline[0]))
    x.append(float(myline[1]))
    y.append(float(myline[2]))
    z.append(float(myline[3]))
    Xlist.append([float(myline[2]),float(myline[3]),float(myline[4])])

X = np.asarray(Xlist)



db = DBSCAN(eps=5, min_samples=10).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_



# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)

# Plot result
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'
        
    class_member_mask = (labels == k)
    xyz = X[class_member_mask & core_samples_mask]
    if (len(xyz[:,0])> 0 and k == 13):

        #print xyz[:,0], xyz[:,1], xyz[:,2]
        
        ax.plot(xyz[:,0], xyz[:,1], xyz[:,2], 'o', markersize=10, color=col)
        for i in range(len(xyz[:,0])-1):
            a = Arrow3D([xyz[i,0], xyz[i+1,0]], [xyz[i,1], xyz[i+1,1]], 
                [xyz[i,2], xyz[i+1,2]], mutation_scale=20, 
                lw=1, arrowstyle="-|>", color=col)
            ax.add_artist(a)
#        print k
        #print xyz[:,0], xyz[:,1], xyz[:,2]
              
        ax.plot([mean(xyz[:, 0])], [mean(xyz[:, 1])], [mean(xyz[:, 2])], 'o', markersize=30, color=col)
 #       for i in range(len(xyz[:,0])-1):
 #           a = Arrow3D([xyz[i,0], xyz[i+1,0]], [xyz[i,1], xyz[i+1,1]], 
 #               [xyz[i,2], xyz[i+1,2]], mutation_scale=20, 
 #               lw=3, arrowstyle="-|>", color=col)
 #           ax.add_artist(a)
        
    #print "\n"
    #if (len(xyz[:,0])> 0):
        print "\n", mean(xyz[:, 0]), mean(xyz[:, 1]), mean(xyz[:, 2]), ":\n"
    #for i in range(len(xyz)):
    #    print xyz[i, 0], xyz[i, 1], xyz[i, 2]
    


mydata = open('com_Cu.txt', 'r')
time = []
x = []
y = []
z = []
Xlist = []

for line in mydata:
    string = line.rstrip()
    myline = string.split()
    time.append(float(myline[0]))
    x.append(float(myline[1]))
    y.append(float(myline[2]))
    z.append(float(myline[3]))
    Xlist.append([float(myline[2]),float(myline[3]),float(myline[4])])

X = np.asarray(Xlist)



db = DBSCAN(eps=5, min_samples=10).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_



# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)

# Plot result

unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'

    class_member_mask = (labels == k)

    xyz = X[class_member_mask & core_samples_mask]
    if (len(xyz[:,0])> 0 and k == 7):
        #print xyz[:,0], xyz[:,1], xyz[:,2]
        
        ax.plot([xyz[0,0]], [xyz[0,1]], [xyz[0,2]], 'o', markersize=5, color="b")
        ax.plot(xyz[1:,0], xyz[1:,1], xyz[1:,2], 'o', markersize=5, color="k")
        for i in range(len(xyz[:,0])-1):
            a = Arrow3D([xyz[i,0], xyz[i+1,0]], [xyz[i,1], xyz[i+1,1]], 
                [xyz[i,2], xyz[i+1,2]], mutation_scale=10, 
                lw=1, arrowstyle="-|>", color="k")
            ax.add_artist(a)
    #print "\n"
    if (len(xyz[:,0])> 0):
        print k,"\t", mean(xyz[:, 0]),"\t", mean(xyz[:, 1]),"\t", mean(xyz[:, 2])
    #for i in range(len(xyz)):
    #    print xyz[i, 0], xyz[i, 1], xyz[i, 2]

      
plt.show()

