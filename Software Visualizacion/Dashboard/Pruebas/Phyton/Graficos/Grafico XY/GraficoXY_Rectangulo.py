import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import numpy as np

x = np.arange(10)
y = np.arange(10)

fig, ax = plt.subplots(1)

ax.plot([1,4],[1,4])

cajas=[patches.Rectangle((x , y), 0.5, 0.5)]
print(cajas)
# pc = PatchCollection(cajas, facecolor='r', alpha=0.5,edgecolor='None')
# ax.add_collection(pc)
ax.add_patch(cajas)
# ax.add_patch(patches.Rectangle((x, y),0.5,0.5,edgecolor = 'blue',facecolor = 'red',fill=True))
# ax.add_patch(patches.Rectangle((2, 1),0.5,0.5,edgecolor = 'blue',facecolor = 'red',fill=True))

plt.show()