import matplotlib.pyplot as plt
#--------------------------------------------------------------------
 #https://numython.github.io/posts/graficas-de-pastel-con-matplotlib/
manzanas = [20,10,25,30]
nombres = ["Ana","Juan","Diana","Catalina"]
colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]
plt.pie(manzanas,labels=nombres, autopct="%0.1f %%", colors=colores)
plt.axis("equal")
plt.show()
#--------------------------------------------------------------------