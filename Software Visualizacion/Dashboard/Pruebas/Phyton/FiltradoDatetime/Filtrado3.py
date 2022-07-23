import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'date':['6/2/2017 10:00:00','5/23/2017','5/20/2017','6/22/2017','6/21/2017'],'Revenue':[100,200,300,400,500]})
df.date = pd.to_datetime(df.date) #Trasforma a dato tipo date

#df.index = pd.to_datetime(df.index)

df=df.sort_values(by="date") #ordeno y reindexo valores, inplace=True para que trabaje sobre el mismo dataframe y drop para que no haga una nueva columna con los antiguos index
df=df.reset_index() #reindexo
df.drop(['index'],axis=1,inplace=True) #borro columna index de los indices anteriores y trbajo sobre el mismo dataframe(inplace=True)

df["ContAux"] = 1 #Genero contador auxiliar

dg = df.groupby(pd.Grouper(key='date', freq='M')).sum() # groupby each 1 month
#dg.index = dg.index.strftime('%B')
#dg.reset_index(inplace=True) #Ver para que sirve drop
dg.reset_index(drop=True,inplace=True) #reindexo para tener un indice que no sea date sobre la misma columna de indice para no crear un nuevo dataframe

print(df)
#Creo una columna x a patir del indice para graficar
dg['x']=dg.index+1

#Extraigo datos en listas
x=dg.index.tolist()
y=dg['ContAux'].tolist()
h=[1,2,3]
print(h)

ax=plt.subplot() #Ejes
ax.set_xticks([1,2]) #Seteo los valores del eje x
#ax.set_yticks([1,2,3,4,5]) #Rango de valores en eje y
#ax.set_xticklabels(['a','b']) Nombre que corresponde a cada valor del eje x

#dg.plot(x="x", y="ContAux", kind="line",ax=ax)

plt.plot(x, y)

plt.show()

