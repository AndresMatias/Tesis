import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

y = np.random.rand(10,4)
y[:,0]= np.arange(10)
df = pd.DataFrame(y, columns=["X", "A", "B", "C"])

#ax = df.plot(x="X", y="A", kind="bar")
df.plot(x="X", y="B", kind="line")
#df.plot(x="X", y="C", kind="line", ax=ax, color="C3")

plt.show()