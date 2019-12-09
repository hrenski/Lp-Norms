#! /usr/bin/env python3

from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_xticks([])
ax.set_yticks([])

data = np.random.random_sample((20,90,360))
lat = np.arange(len(data[0,:,0]))
lon = np.arange(len(data[0,0,:]))
lons,lats = np.meshgrid(lon,lat)

mode = 'imshow'

ims = []
for i in range(len(data[:,0,0])):
    if mode == 'contour':
        im = ax.contourf(lons,lats,data[i,:,:], cmap = 'Greys')
        add_arts = im.collections
    elif mode == 'imshow':
        im = ax.imshow(data[i, :, :], extent=[np.min(lons), np.max(lons),
                                               np.min(lats), np.max(lats)],
                       aspect='auto', cmap = 'Greys')
        add_arts = [im, ]

    text = 'title={0!r}'.format(i)
    ims.append(add_arts)

ani = animation.ArtistAnimation(fig, ims, interval=70,repeat_delay=0, blit=False)

ani.save('blank.gif', writer='imagemagick')
