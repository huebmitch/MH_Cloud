import matplotlib.pyplot as plt
import random
import numpy as np

position = 0
walk = [position]
steps = 500
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

first10crossing = (np.abs(walk) >= 10).argmax()

print("The walk took", steps, "steps")
print("The walk ended at:", position)
print("The walk reached a MAX of", np.max(walk))
print("The walk reached a MIN of", np.min(walk))
print("The walk was first 10 steps from Origin on step", first10crossing)
print("The most visited place was", np.median(walk))

plt.plot(walk)
plt.show()