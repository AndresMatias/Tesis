
from datetime import datetime,timedelta,date,time
import pyodbc
import numpy as np
import math

#----Fecha y hora sql-----
# sql=datetime.now()
# print(sql)

# turno=[time(12,0,0),time(18,0,0)]
# print(turno)

# print(ahora.hour)
# print(ahora.minute)
# print(ahora.second)


#delta=timedelta(hours=4,minutes=1)

# vTiempo=[]
# delta2=delta/4 #Ventana de tiempo/4: (Tiempo Final- Tiempo Inicial)/4
# for i in range(0,5):
# 	 vTiempo.append(str(ahora+(delta2*i)))
# 	 print(vTiempo[i])

# print(ahora)		
# ayer=ahora-delta
# delta2=ahora-ayer
# Redonde=math.ceil(delta2.total_seconds()/3600)
# print(Redonde)
# prueba=datetime(2021, 12, 31, 23, 59, 59, 0, tzinfo=None)
# prueba2=datetime(2021,12,31)
# print(prueba2)
#ayer=str(ayer)[:-3]
#print(timedelta(days=1, seconds=29156, microseconds=0.5000))

# date_s = (datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
# date_s = datetime.now().isoformat(sep=' ', timespec='milliseconds')

# print(date_s)
# def last_day_of_month(any_day):
#     next_month = any_day.replace(day=28) + timedelta(days=4)
#     return next_month - timedelta(days=next_month.day)

# for month in range(1, 13):
#  	print(last_day_of_month(date(2012, month, 1)).day)

# NroDias=last_day_of_month(date(2012, int("05"), 1)).day
# ListaNroDias=np.array(range(1,NroDias))
# print(str(ListaNroDias))  


# now = datetime.now()
# format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
# print(format)

# today = date.today()
# hora=time(2,2,2)
# print(hora.hour)
# print(today)
