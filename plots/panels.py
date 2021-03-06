# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Panelling

import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = False
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['ytick.direction'] = 'out'

# ## Drawing panels
#
# Panels are obtained by using the [subplot](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html) method, which returns an axe object.
#
# <div class="alert alert-info">
#     <strong>Remark</strong> The <i>plt.gca()</i> method is identical to <i>plt.subplot(1, 1, 1)</i>
# </div>

fig = plt.figure()
for p in range(1, 3*3+1):
    ax = plt.subplot(3, 3, p)  # number of rows, number of columns, subplot index (starts at 1!)
    plt.text(0.5, 0.5, 'Axes number '+str(p), ha='center', va='center')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

# ## Setting panel properties
#
# The [subplots_adjust](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html) method allows to control some panelling properties (horizontal and vertical spacing, margins, etc.).

fig = plt.figure()
plt.subplots_adjust(wspace=0.4, hspace=0.1,
                    left = 0.05, right=0.95,
                    bottom=0.05, top=0.95)
for p in range(1, 3*3+1):
    ax = plt.subplot(3, 3, p)
    plt.text(0.5, 0.5, 'Axes number '+str(p), ha='center', va='center')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()

# ## Managing properties
#
# It is possible to store the outcomes of the `subplot` method into a list, to manage some axis properties *a posteriori*

# +
fig = plt.figure()

listax = []
for p in range(1, 3*3+1):
    ax = plt.subplot(3, 3, p)
    listax.append(ax)
    plt.text(0.5, 0.5, 'Axes number '+str(p), ha='center', va='center')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
 
for ax in [listax[6], listax[7], listax[8]]:
    ax.get_xaxis().set_visible(True)
    
for ax in [listax[0], listax[3], listax[6]]:
    ax.get_yaxis().set_visible(True)
    
for ax in [listax[0], listax[1], listax[2]]:
    ax.set_title('Nom titre')

plt.show()
# -

# ## Defining panel grid
#
# To define grid panels, use the [subplot2grid](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot2grid.html) medhod.

# +
fig = plt.figure()
# size of the subplot: 3 by 3
# location of the plot: 0(top), 0(left), spans 3 columns (spans 1 row, default)
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
plt.text(0.5, 0.5, 'Axe 1', ha='center', va='center')

ax2 = plt.subplot2grid((3, 3), (1, 1), rowspan=2)
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)
plt.text(0.5, 0.5, 'Axe 2', ha='center', va='center')

plt.show()
# -

# ## Manual position of subplots
#
# The [axes](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.axes.html) method allows to create axes by providing its position relative to figure coordinates.

fig = plt.figure()
ax = plt.gca() # add a first axes 
ax.text(0.5, 0.5,'First axe', ha='center', va='center')
ax = plt.axes([0.7, 0.7, 0.25, 0.25])
plt.text(0.5, 0.5, 'Small panel', ha='center', va='center')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()

# This can be usefull for instance to **manually position colorbars**.

# +
import numpy as np

delta = 0.01
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
xx, yy = np.meshgrid(x, y)
zz = xx * yy

plt.figure()
plt.subplots_adjust(bottom=0.25)
cs = plt.pcolormesh(zz)
cax = plt.axes([0.25, 0.05, 0.5, 0.1])  # define the position of the colorbar
plt.colorbar(cs, cax, orientation='horizontal')
plt.show()
