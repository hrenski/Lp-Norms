#! /usr/bin/env python3

import numpy as np
from matplotlib import animation
import matplotlib.pyplot as plt
import seaborn as sns

def main(save = True):
    sns.set()

    fig, ax = plt.subplots(figsize = (4, 4))
    ax.set_aspect('equal')

    ax.set_xticks([-2, -1, 0, 1, 2])
    ax.set_yticks([-2, -1, 0, 1, 2])

    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')

    plt.tight_layout()

    ax.plot(0., 0., color = 'blue', marker='.', markersize = 2)

    delta = 0.01
    x = np.arange(-2.0, 2.0 + delta, delta)
    y = np.arange(-2.0, 2.0 + delta, delta)
    ys,xs = np.meshgrid(y, x, indexing = 'ij')

    cs = ax.contour(ys,xs, circle(ys, xs), levels = [0.9999, 1, 1.0001], colors = 'orangered', linewidths = 0.5)

    rect = plt.Rectangle((0,0),1,1, fc = 'orangered')
    rect_p = plt.Rectangle((0,2),1,1, fc = 'seagreen')

    plt.legend([rect, rect_p], [r'$l_{2}$ circle', r'$l_{p}$ circle'])

    p_range = np.power(2, np.arange(np.log2(0.15), np.log2(36.), 0.1))
    p_range = np.concatenate((p_range, p_range[::-1]))

    ims = []

    for i in range(p_range.size):
        p = p_range[i]

        im = ax.contour(ys,xs, circle(ys, xs, p), levels = [0.9999, 1, 1.0001], colors = 'seagreen', linewidths = [0.5] * 3)
        add_arts = im.collections

        if p_range[i] <= 29:
          text = r'$p$ = {0:.3f}'.format(p_range[i])
        else:
          text = r'$p = \infty}$'

        an = ax.annotate(text, xy=(0.45, 1.01), xycoords='axes fraction')
        ims.append(add_arts + [an])

    ani = animation.ArtistAnimation(fig, ims, interval = 50, repeat_delay=250, blit=False)

    if save:
        ani.save('circles.gif', writer='imagemagick')
    else:
        plt.show()

def circle(X, Y, p = 2):
    if p > 29:
        Z = np.maximum(np.abs(X), np.abs(Y))
    else:
        Z = np.power(np.abs(X), p) + np.power(np.abs(Y), p)

    return Z

if __name__ == '__main__':
    main(save = False)
