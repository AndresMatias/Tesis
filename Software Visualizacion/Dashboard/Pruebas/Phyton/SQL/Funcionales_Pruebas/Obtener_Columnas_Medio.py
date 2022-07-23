import pyodbc
#Parametros  de Conexion
direccion_servidor='DESKTOP-TVTMCR0'
nombre_bd='Inyectora'
nombre_usuario ='alladio'
password='12345'

try:
    #Especificar el controlador ODBC, el nombre del servidor, la base de datos, etc. directamente
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD='+password)
    #Crea un cursor a partir de la conexión
    cursor=conexion.cursor()
    
   
    #------------------------------Consulta de Informacion de Esquema ---------------------------------------------
    #SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Tabla_Pruebas' # Comando Util
    query=("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Tabla_Pruebas'") #Esta Consulta duelve una matriz
    #Ejecuto Consulta para enviar datos
    cursor.execute(query)

    #------------------Obtener Columnas---------------------
    for i in cursor:
        print(i[3]) #En la posicion 3 esta el nombre de las columnas
    #-------------------------------------------------------    

except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
finally:
    cursor.close()

print("Fin Programa")


