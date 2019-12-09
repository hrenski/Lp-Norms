#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:27:14 2019

@author: flatironstudent
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

n = 101
p = 2

np.random.seed(111)

b = np.random.exponential(10.5, n)
x = np.arange(-5., 52. ,0.01)
p_range = np.arange(0.15, 36, 0.1)

costs = np.power(np.sum(np.power(np.abs(b[None,...] - x[...,None])[None,...], p_range[...,None,None]), axis = -1), 1 / p_range[...,None])
min_costs = x[np.argmin(costs, axis = 1)]

indx = np.argmin(np.abs(p_range - 1))

sns.set()

#-------------------------------------------------------------------------------
fig = plt.figure(figsize = (6, 4))
ax=fig.add_subplot(1,1,1)

ax.plot(p_range, min_costs)
ax.set_xlim([0, p_range.max()])

ax.set_xticks(range(0,int(p_range.max()) + 1,2))
ax.set_yticks(np.arange(0,p_range.max(),2.5))

plt.title(r'Objective Function Minimizers')
plt.xlabel(r'$p$')
plt.ylabel(r'x value that minimizes $f_p$')
plt.tight_layout()
plt.savefig("lp_min.png")

