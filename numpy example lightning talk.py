# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:32:26 2023

@author: Sajan Dayal
ME369P
Lightning Talk
Dream Team
"""

import numpy as np

#creation of arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, -1, 1, 8])
arr3 = np.array([True, False, True])
arr4 = np.array([True, True, False])

#Truth Testing
istrue=np.all(arr3)
print('Is it true: ', istrue)

#Logical Operations
logical=np.logical_and(arr3, arr4)
print('Logical Operations: ', logical)

#Comparison
comparison=np.greater(arr1, arr2)
print('Is is greater: ', comparison)

#ArrayContents
contents=np.isfinite(arr1)
print('Is it finite: ',contents)
isnotanumber=np.isnan(arr1)
print('Is not a number: ', isnotanumber)

#Descriptive Statistics
mean_value = np.mean(arr1)
print('Mean: ', mean_value)
median_value = np.median(arr1)
print('Median: ',median_value)
std_deviation = np.std(arr1)
print('Standard Deviation: ',std_deviation)

#Percentiles and Quartiles
percentile_25 = np.percentile(arr1, 25)
percentile_75 = np.percentile(arr1, 75)
print('25th Percentile: ', percentile_25)
print('75th Percentile: ', percentile_75)

#Check for outliers
z_scores = (arr1 - np.mean(arr1)) / np.std(arr1)
outliers = np.abs(z_scores) > 2
print('Is an outlier: ',outliers)
