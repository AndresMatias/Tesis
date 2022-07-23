import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np 

plt.axes()

 #--------------Limites externos-------------
pac1 = mpatches.Arc([0, 0], 10, 10, 0, theta1=0, theta2=180, hatch = '') # Limite Superior
pac2 = mpatches.Arc([0, 0], 4, 4, 0, theta1=0, theta2=180, hatch = '') # Limite inferior
pac1.set_color('cyan')
pac2.set_color('cyan')
plt.gca().add_patch(pac1)
plt.gca().add_patch(pac2)
 #--------------Limites internos----------------
pac3 = mpatches.Arc([0, 0], 8, 8, 0, theta1=0, theta2=180, hatch = '') # Limite Superior
pac4 = mpatches.Arc([0, 0], 6, 6, 0, theta1=0, theta2=180, hatch = '') # Limite inferior
pac3.set_color('red')
pac4.set_color('red')
plt.gca().add_patch(pac3)
plt.gca().add_patch(pac4)
#---------------Relleno-----------------------
lista=np.arange(6, 8, 0.01) #Nro de arcos
vector=np.array(lista)
for i in range(0,len(vector)):
    pacn= mpatches.Arc([0, 0], vector[i], vector[i], 0, theta1=120, theta2=180, hatch = '')
    pacn.set_color('green')
    plt.gca().add_patch(pacn)






plt.axis('equal')
plt.show()