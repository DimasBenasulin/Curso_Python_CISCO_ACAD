import matplotlib.pyplot as plt
from random import randrange, randint
import numpy as np
#plt.style.use('_mpl-gallery')

# Mi cutre histograma
histo=[0 for i in range(13)]

# make data: ------------------- Tirar los dados n veces

for i in range(10000):
    x = 0.5 + np.arange(13)
    y1 = randint(1, 6)
    y2 = randint(1, 6)
    suma = y1 + y2
    histo[suma] += 1




# plot ------------------------- Visualización
fig, ax = plt.subplots()

ax.bar(x, histo, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 13), ylim=(0, 2000))
      
plt.show()