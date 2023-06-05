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
student_data1 = pd.DataFrame({
'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
'marks': [200, 210, 190, 222, 199]})
student_data2 = pd.DataFrame({
'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William',
'Madeeha Preston'],
'marks': [201, 200, 198, 219, 201]})
print("Original DataFrames:")
print(student_data1)
print("-------------------------------------")
print(student_data2)
print("\nJoin the said two dataframes along rows:")
result_data = pd.concat([student_data1, student_data2])
print(result_data)

#3
import pandas as pd
student_data1 = pd.DataFrame({
'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
'marks': [200, 210, 190, 222, 199]})
dicts = [{'student_id': 'S6', 'name': 'Scarlette Fisher', 'marks': 203},
{'student_id': 'S7', 'name': 'Bryce Jensen', 'marks': 207}]
print("Original DataFrames:")
print(student_data1)
print("\nDictionary:")
print(dicts)
combined_data = student_data1._append(dicts, ignore_index=True, sort=False)
print("\nCombined Data:")
print(combined_data)
