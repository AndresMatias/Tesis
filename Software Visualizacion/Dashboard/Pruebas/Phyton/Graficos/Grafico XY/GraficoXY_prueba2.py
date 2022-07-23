import numpy as np
import matplotlib.pyplot as plt

x=np.arange(10)
y=np.arange(10)

upper = 8 #Limite superior
lower = 4 #Limite inferior

supper = np.ma.masked_where(x < upper, x)  
slower = np.ma.masked_where(x > lower, x)
smiddle = np.ma.masked_where((x < lower) | (x > upper), x)

print(supper)
print(slower)
print(smiddle)

fig, ax = plt.subplots()
# ax.plot(x, smiddle, x, slower, x, supper)

y=np.zeros(len(x))

ax.plot(smiddle,y)
ax.plot(slower,y)
ax.plot(supper,y)
plt.show()