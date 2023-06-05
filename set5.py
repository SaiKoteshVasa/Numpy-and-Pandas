#1
import pandas as pd
df = pd.DataFrame({
'school_code': ['s001','s002','s003','s001','s002','s004'],
'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
'weight': [35, 32, 33, 30, 31, 32],
't_id':['t1', 't2', 't3', 't4', 't5', 't6']})
print("Default Index:")
print(df.head(10))
print("\nt_id as new Index:")
df1 = df.set_index('t_id')
print(df1)
print("\nReset the index:")
df2 = df1.reset_index()
print(df2)

#2
import numpy as np
a=np.array([1,2])
print(a,a.dtype)
b=np.array([1.2,2.4])
print(b,b.dtype)
c=np.array([1+2j,3+3j])
print(c,c.dtype)
d=np.array(['apple','banana','grape'])
print(d,d.dtype)
