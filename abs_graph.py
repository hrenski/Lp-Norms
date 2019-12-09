#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

fig = plt.figure(figsize = (4, 2.89))

ax = plt.gca()
ax.set_aspect('equal')

x = np.arange(-4., 4 + 0.01, 0.01)
y = np.abs(x)

plt.plot(x, y)

plt.axvline(x = 0, color = "black", linewidth = 0.5)
plt.axhline(y = 0, color = "black", linewidth = 0.5)

plt.title(r'$y = |x|$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')

plt.xticks(list(range(-4,5)))
plt.yticks(list(range(-1,5)))

plt.tight_layout()
plt.savefig('abs_graph.png')
