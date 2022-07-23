import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
#--------------------------------------------------------------------
 #https://numython.github.io/posts/graficas-de-pastel-con-matplotlib/
manzanas = [20,10,25,30]
nombres = ["Ana","Juan","Diana","Catalina"]
colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"] # Si uso gama de colores no uso esto, ver como lo voy a perzonalizar
#colores = None #sin colores puedo poner el argumento y no pasar colores solo un None
fig=plt.figure(facecolor='#33B5FF') #Color de fondo facecolor
grafica=fig.add_subplot(111)

#------------Tratamiento en los Ejes---------------------
#grafica.axis("off") #Saco Ejes
grafica.axis("equal")
#grafica.set_xlabel('Tiempo') #Solo funciona con los ejes activados

#---------------------Titulo y Texto-------------------------------
grafica.set_title('Perido de 12 hs') #Titulo

#--------------------Gama de colores-----------------------------------
normdata = colors.Normalize(min(manzanas), max(manzanas))
colormap = cm.get_cmap("Reds") #Escojo color
colores =colormap(normdata(manzanas))

#----------------------------Grafica-------------------------------
grafica.pie(manzanas,labels=nombres, autopct="%0.1f %%", colors=colores)

legend=grafica.legend()
legend.get_frame().set_facecolor('#33B5FF')#Color de fondo de legend

plt.show()
