#1
import numpy as np
y = np.array([[2,4,6], [1,3,5], [9,7,8]])
print(y)
print('\n')
print(np.apply_along_axis(sorted,1, y))
print('\n')
print(np.apply_along_axis(sorted, 0, y))
print()

import numpy as np
x = np.arange(24).reshape(4,3,2)
print(x)
print("\n")
print(np.apply_over_axes(np.sum, x, [0,0]))
print("\n")
print(np.apply_over_axes(np.sum, x, [0,1]))
print("\n")
print(np.apply_over_axes(np.sum, x, [0,2]))
print("\n")
print(np.apply_over_axes(np.sum, x, [2,0]))
print("\n")
print(np.apply_over_axes(np.sum, x, [1,0]))
print("\n")

import numpy as np
def fun(a, b):
 if a > b:
     return a + b
 else:
     return a - b
 if a >= b:
   return a + b
 else:
   return a - b
vecfun = np.vectorize(fun)
print(vecfun(np.arange(5), 5))
print(vecfun(np.arange(5), [1,2,3,4,5]))
print(vecfun([[2,4,6,1]], [1,2,3,4]))

#2
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

#3
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
