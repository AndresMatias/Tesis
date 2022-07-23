import pyodbc
#Parametros  de Conexion
direccion_servidor='DESKTOP-TVTMCR0'
nombre_bd='Inyectora'
nombre_usuario ='alladio'
password='12345'

try:
    # Especificar el controlador ODBC, el nombre del servidor, la base de datos, etc. directamente
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD='+password)
    # Crea un cursor a partir de la conexión
    cursor=conexion.cursor()
    q1='SELECT CGolpes from Tabla_Pruebas1'
    q2='SELECT MAX(CGolpes) FROM Tabla_Pruebas1 where SIM=1' #Numero mas alto en CGolpes
    #Ejecuto Consulta
    cursor.execute(q2)
    
    for i in cursor:
        print(i[0])

    #print(cursor[0][0])

except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
finally:
    cursor.close()

print("Fin Programa")    
