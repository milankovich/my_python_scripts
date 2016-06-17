# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:53:40 2016

@author: Shipeng
"""

import numpy as np
import math
from math import *


def weighted_avg_and_std(values, weights):
    """
    Return the weighted average and standard deviation.

    values, weights -- Numpy ndarrays with the same shape.
    """
    average = np.average(values, weights=weights)
    variance = np.average((values-average)**2, weights=weights)  # Fast and numerically precise
    return (average, math.sqrt(variance))
 
data = []

f = open('mydata_test.txt', 'r')
for line in f:
#    print line
    words = line.split()
    linedata =  [int(words[0]),float(words[1]),float(words[5]),float(words[8])/float(words[5])]
#    print linedata
    data.append(linedata)

data_array = np.asarray(data)

#print data_array

#filtered_array = np.array(filter(lambda row: row[0]==10, data_array))

#print filtered_array
for i in range(217):
    filtered_array = np.array(filter(lambda row: row[0]==2*i, data_array))
    percentSi = filtered_array[:,3]
    weights = filtered_array[:,2]
    time = filtered_array[0,1]
    [average,std] = weighted_avg_and_std(percentSi,weights)
    print time, average, std
    #print average, std

   




