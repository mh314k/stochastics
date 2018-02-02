import itertools as loops
import matplotlib.pyplot as plt

N = 10
States = [0, 1]
Probs = {0: 0.5, 1: 0.5}

Zeros = [0]*(N+1)
for i in loops.product(States, repeat=N):
    l=list(i)
    n=l.count(0)
    Zeros[n] += 1

Uniform =

for i in range(N+1):
    Zeros[i] = Zeros[i]/(len(States)**N)

plt.plot(Zeros)
plt.show()
