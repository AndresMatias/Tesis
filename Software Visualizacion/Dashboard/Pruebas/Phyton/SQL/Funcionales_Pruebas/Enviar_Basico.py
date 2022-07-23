import pyodbc
#Parametros  de Conexion
direccion_servidor='DESKTOP-TVTMCR0'
nombre_bd='Inyectora'
nombre_usuario ='alladio'
password='12345'

try:
    #ODBC Driver 17 for SQL Server
    # Especificar el controlador ODBC, el nombre del servidor, la base de datos, etc. directamente
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD='+password)
    # Crea un cursor a partir de la conexión
    cursor=conexion.cursor()
    #Ejecuto Consulta para enviar datos
    query=('INSERT INTO Tabla_Pruebas(Estado) Values(?)')
    query2='UPDATE Combinaciones SET IdCode=18.0 where SIM=5600670.0'
    cursor.execute(query2)
    cursor.commit()

except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
finally:
    cursor.close()

print("Fin Programa")    
