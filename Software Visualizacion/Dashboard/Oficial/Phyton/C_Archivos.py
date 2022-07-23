import pickle
import os.path as path

class ManejoArchivos():
    """ Esta clase gestiona los archivos de configuracion,ajustes y credenciales de conexion a bbdd"""
    def __init__(self):
        pass

    def CargaBBDD(self):
        datos=None #(servidor,bbdd,usuario,contraseña)
        if path.exists('bbdd'):
            fichero=open("bbdd","rb") #rb:leo en binario
            datos=pickle.load(fichero)
            fichero.close() #Cierro
            del(fichero) #Limpio memoria
        return datos

    def GuardarBBDD(self,datos): #datos=(servidor,bbdd,usuario,contraseña)
        """ Metodo para guardar los datos de conexion a una bbdd en modo binario 
            Parametros:
                datos: tupla que debe contener los siguientes datos (servidor,bbdd,usuario,contraseña)"""
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Nota:Se puede mejorar la encriptacion de la contraseña con cryp o algo asi y utilizando variables globales de entorno para hacer la "sal"(palabra qeu escoje uno para encriptar)
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        fichero_binario=open("bbdd","wb") #wb:escritura binaria
        pickle.dump(datos,fichero_binario) #vuelco lista_nombres en fichero_binario
        fichero_binario.close() #Cierro
        del(fichero_binario) #Limpio memoria