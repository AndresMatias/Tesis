import pickle
import os.path as path
# lista_nombres=["pedro","ana","maria"]

# fichero_binario=open("lista_nombres","wb") #wb:escritura binaria
# pickle.dump(lista_nombres,fichero_binario) #vuelco lista_nombres en fichero_binario
# fichero_binario.close()
# del(fichero_binario) #borro de la memoria

# fichero=open("lista_nombres","rb") #rb:leo en binario
# lista=pickle.load(fichero)
# fichero.close()
# print(lista)
#if path.exists('lista_nombres'):
if path.exists('bbdd'):
    print('existe')
    fichero=open("bbdd","rb") #rb:leo en binario
    datos=pickle.load(fichero)
    print(datos)
    del(fichero) #Limpio memoria
else:
    print('no existe')