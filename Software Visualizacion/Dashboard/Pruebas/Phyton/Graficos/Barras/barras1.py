import numpy as np
import matplotlib.pyplot as plt
 
# data1=[30,20,10,0,0]
# data2=[20,20,20,20,0]
# data3=[50,60,70,80,100]

# year=["2015","2016","2017","2018","2019"]

# plt.figure(figsize=(9,7))
# plt.barh(year,data3,color="green",label="Python")
# plt.barh(year,data2,color="yellow",left=np.array(data3),label="JavaScript")
# plt.barh(year,data1,color="red",left=np.array(data3)+np.array(data2),label="C++")

# plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
# plt.show()

#-----------------------------------------------------------------------------------
data=[50,60,70,80,100]
color=['red','blue','yellow','green','orange']
data1=[0,50,110,180,260]

plt.figure(figsize=(9,7))
# plt.barh('Datos',data,color=color,left=data1,label="Python")

# plt.figure(figsize=(9,7))
# plt.barh(data1,data,color=color,label="Python")
# plt.barh(year,data2,color="yellow",left=np.array(data3),label="JavaScript")
# plt.barh(year,data1,color="red",left=np.array(data3)+np.array(data2),label="C++")

plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
plt.show()