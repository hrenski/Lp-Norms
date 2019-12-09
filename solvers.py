#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:27:14 2019

@author: flatironstudent
"""

import numpy as np
from scipy.optimize import minimize
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib

sns.set()

n = 101

np.random.seed(111)
b = np.random.exponential(10.5, n)

fig = plt.figure(figsize = (3,3))
sns.distplot(b, kde = False)


plt.title("Numbers Distribution")
plt.xlabel("Value")
plt.ylabel("CoFrequencyunt")

#plt.tight_layout()

plt.savefig("numbers.png")

