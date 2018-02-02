import numpy as np
from itertools import accumulate as acc
import matplotlib.pyplot as plt

h = []
plt.figure(1)
plt.subplot(211)
for i in range(1000):
    a = list(acc(list(np.random.choice([-1, 1], size=5000))))
    h.append(a[49])
    lst1 = [0] + a
    plt.plot(lst1, linewidth=0.2)
plt.subplot(212)
n, bins, patches = plt.hist(h, 10, normed=1)
plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
plt.show()
