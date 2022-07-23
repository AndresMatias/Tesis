from datetime import datetime,time,timedelta

ahora=datetime.now()
mm=ahora.minute
mmAux=(ahora+timedelta(minutes=1)).minute
while(mm!=mmAux):
	mm=datetime.now().minute

print(mmAux)