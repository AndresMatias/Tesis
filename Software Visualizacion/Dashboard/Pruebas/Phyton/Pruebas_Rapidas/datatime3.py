from datetime import datetime,time,timedelta

h1=time(12,0,0)
h2=time(15,0,0)


# https://python-para-impacientes.blogspot.com/2014/02/operaciones-con-fechas-y-horas.html

# Asigna formato de ejemplo1
formato1 = "%A"
formato2 = "%d-%m-%y %I:%m %p"
formato2 = "%H %p"
# Asigna formato de ejemplo1
# formato1 = "%A %B %d %H:%M:%S %Y"


hoy = datetime.today()  # Asigna fecha-hora

# Aplica formato ejemplo1
cadena1 = hoy.strftime(formato2)  


# Muestra fecha-hora según ejemplo1
print("Formato1:", cadena1)
