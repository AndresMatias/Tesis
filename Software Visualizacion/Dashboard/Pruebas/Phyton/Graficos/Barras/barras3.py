import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime,timedelta,date

hoy=date.today()
ahora=datetime.now()
delta=timedelta(hours=12)
ayer=ahora-delta
prueba=datetime(20, 12, 31, 23, 59, 59, 0, tzinfo=None)

print("La hora es {}".format(ayer.hour))
print("El minuto es {}".format(ayer.minute))
print("El segundo es {}".format(ayer.second))

#print("{0}:{1}".format(ayer.hour,ayer.minute))

# ayer=str(ayer)[:-3]
#print(hoy)

print(ayer.strftime('%H:%M:%S')) #Formato de impresion de hora minutos y segundos

inicio=ahora.strftime('%H:%M:%S')
fin=ayer.strftime('%H:%M:%S')
miDic={inicio:0,fin:100}
data1=0
data2=ahora
data3=miDic(inicio)
year=["Periodo"]

plt.figure(figsize=(9,7))
plt.barh(year,data3,color="green",label="Python")
# plt.barh(year,data2,color="yellow",left=np.array(data3),label="JavaScript")
# plt.barh(year,data1,color="red",left=np.array(data3)+np.array(data2),label="C++")

plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
plt.show()