from io import open
# archivo_texto=open("Archivo 1.txt","w") #Creo archivo y lo abro en modo escritura, esto reescribe el archivo si existe
# frase="Escribiendo en mi archivo \ndia lunes"
# archivo_texto.write(frase) #escribo
# archivo_texto.close() #cierro

# archivo_texto=open("Archivo 1.txt","r") #Creo archivo y lo abro en modo lectura
# print(archivo_texto.read())
# archivo_texto.close()

archivo_texto=open("Archivo 1.txt","r") #Creo archivo y lo abro en modo lectura
lista=archivo_texto.readlines() #lectura linea por linea
print(lista)
print(lista[0]) #leo la posicion 0
archivo_texto.close()

archivo_texto=open("Archivo 1.txt","a") #Creo archivo y lo abro en para agregar informacion
archivo_texto.write("\nAgregando linea")
archivo_texto.close()