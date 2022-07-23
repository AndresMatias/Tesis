import matplotlib.pyplot as plt
datos=[1, 2, 3, 4]
plt.plot(datos,datos) #Recta uno
#plt.plot([4,5,6,7],[3,2,1,1],label="hola")       #Recta dos
plt.annotate('datos',xy=(2, 2),xycoords='data',xytext=(0,+30),textcoords='offset points',color='#000000',fontsize=16,arrowprops=dict(arrowstyle="->"))
#plt.plot([7,12],[1,6])       #Recta tres
plt.ylabel('Algunos Numeros')
#plt.axis("off") #Saco ejes

plt.show()