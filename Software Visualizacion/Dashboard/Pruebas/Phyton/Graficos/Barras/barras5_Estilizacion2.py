# libraries
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(facecolor='#33B5FF') #Color de fondo facecolor
grafica=fig.add_subplot(111)


# Choose the height of the bars
height = [3, 12, 5, 18, 45]

# Choose the names of the bars
bars = ('group1', 'group2', 'group3', 'group4', 'group5')
x_pos = np.arange(len(bars))

print(x_pos)

# Create names on the x-axis
plt.xticks(x_pos, bars, color='orange')
plt.yticks(color='orange')

# Create bars
grafica.bar(x_pos, height)
# Show graphic
plt.show()