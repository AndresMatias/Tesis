import numpy as np
import matplotlib.pyplot as plt
 
data1=[30]
data2=[20]
data3=[50]
year=["Periodo"]

plt.figure(figsize=(9,7))
plt.barh(year,data3,color="green",label="Python")
plt.barh(year,data2,color="yellow",left=np.array(data3),label="JavaScript")
plt.barh(year,data1,color="red",left=np.array(data3)+np.array(data2),label="C++")

plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
plt.show()