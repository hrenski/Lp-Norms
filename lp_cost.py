#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:27:14 2019

@author: flatironstudent
"""

from matplotlib import animation, rc
from matplotlib.ticker import FormatStrFormatter


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

n = 101
p = 2

np.random.seed(111)

b = np.random.exponential(10.5, n)
x = np.arange(-5., 52. ,0.01)
p_range = np.power(2, np.arange(np.log2(0.15), np.log2(36.), 0.1))

costs = np.power(np.sum(np.power(np.abs(b[None,...] - x[...,None])[None,...], p_range[...,None,None]), axis = -1), 1 / p_range[...,None])
min_costs = x[np.argmin(costs, axis = 1)]

indx = np.argmin(np.abs(p_range - 1))


#-------------------------------------------------------------------------------
sns.set()

font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 6}

rc('font', **font)

fig = plt.figure(figsize = (4, 2.5))
ax=fig.add_subplot(1,1,1)

ax.set_xlim(x.min(), x.max())
ax.set_ylim(0, costs.max())
ax.set_xticks(np.arange(-5,55,5))

xdata, ydata = [], []
ln, = plt.plot([], [], 'r', linewidth = 0.5)
ln2, = plt.plot([], [], 'b', linewidth = 0.5)
txt = plt.text(0,0,'')

plt.xlabel("x", **font)
plt.ylabel("Cost Function Value", **font)
def update(p):
    indx = np.argmin(np.abs(p_range - p))
    costs_p = costs[indx]

    m = int(np.round(np.log10(costs_p).max()))
    f = int(np.round((costs_p / 10.**m).max()))

    ln.set_data(x, costs_p)
    ln2.set_data([min_costs[indx], min_costs[indx]], [0, (np.arange(0., f + 2., 0.5) * 10.**m).max()])
    txt.set_text(r'$x = ${0:0.2f}'.format(min_costs[indx]))
    txt.set_position((min_costs[indx] + 1, 1.05 * 10**m))

    ax.set_xlim(x.min(), x.max())
    ax.set_title(r'$p = ${0:0.2f}'.format(p_range[indx]), **font)

    yt = np.arange(0., 1.3, 0.2) * 10.**m

    ax.set_ylim(0, yt.max())
    ax.set_yticks(yt)
    ax.ticklabel_format(style='sci', axis='y', scilimits=(m, m))
    ax.tick_params(axis='both', which='major', labelsize=6)
    ax.yaxis.offsetText.set_fontsize(6)
    plt.tight_layout()

    return ln, ln2, txt,



ani = animation.FuncAnimation(fig, update, frames=p_range, blit=False)
ani.save('lp_cost.gif', writer='imagemagick')

#plt.show()

