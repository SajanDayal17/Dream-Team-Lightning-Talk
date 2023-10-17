# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:32:26 2023

@author: sajan
"""

import numpy as np

#creation of arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, -1, 1, 8])
arr3 = np.array([True, False, True])
arr4 = np.array([True, True, False])

#Truth Testing
istrue=np.all(arr3)
print(istrue)

#Logical Operations
logical=np.logical_and(arr3, arr4)
print(logical)

#Comparison
comparison=np.greater(arr1, arr2)
print(comparison)

#ArrayContents
contents=np.isfinite(arr1)
print(contents)