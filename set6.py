import pandas as pd
print("Create an Int64Index:")
df_i64 = pd.DataFrame({
'school_code': ['s001','s002','s003','s001','s002','s004'],
'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill',
'David Parkes'],
'weight': [35, 32, 33, 30, 31, 32]},
index=[1, 2, 3, 4, 5, 6])
print(df_i64)
print("\nView the Index:")
print(df_i64.index)
print("\nFloating-point labels using Float64Index:")
df_f64 = pd.DataFrame({
'school_code': ['s001','s002','s003','s001','s002','s004'],
'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill',
'David Parkes'],
'weight': [35, 32, 33, 30, 31, 32]},
index=[.1, .2, .3, .4, .5, .6])
print(df_f64)
print("\nView the Index:")
print(df_f64.index)

#2
import numpy as np
a=np.array([[15,5,8],[9,7,14]])
print("Mean:",np.mean(a,axis=0))
b=np.array([3,4,9,7,1,5])
print("Median:",np.median(b))
print("SD:",np.std(a))
print("CorrCoeff:",np.corrcoef(a))

