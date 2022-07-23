import pandas as pd
import numpy as np
import datetime

list_of_dates = ['2019-11-20', '2020-01-02', '2020-02-05','2020-03-10','2020-04-16','2020-05-01']
employees=['Hisila', 'Shristi','Zeppy','Alina','Jerry','Kevin']
df = pd.DataFrame({'Entrada de Datos': pd.to_datetime(list_of_dates)},index=employees)

#mask = (df['Joined date'] > '2019-06-1') & (df['Joined date'] <= '2020-02-05')
mask = (df['Entrada de Datos'] == '2020-01-02')
filtered_df=df.loc[mask]
print(df)
print("\n",filtered_df)