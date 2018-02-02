import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from itertools import accumulate as acc

mpl.rcParams['legend.fontsize'] = 7

fig = plt.figure()
ax = fig.gca(projection='3d')
for i in range(5):
    z = list(acc(np.random.choice(np.arange(-1,1,step=(i+1)*0.01),size=200)))
    x = list(acc(np.random.choice(np.arange(-1,1,step=(i+1)*0.01),size=200)))
    y = list(acc(np.random.choice(np.arange(-1,1,step=(i+1)*0.01),size=200)))
    ax.plot(x, y, z, label='3d Brawny wit dt = {}'.format((i+1)*0.01))
ax.legend()

plt.show()
