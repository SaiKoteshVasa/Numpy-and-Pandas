#1
import pandas as pd
df = pd.DataFrame({
'name_code': ['c001','c002','c022', 'c2002', 'c2222'],
'dob': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
'age': [18.5, 21.2, 22.5, 22, 23]
})
print("Original DataFrame:")
print(df)
print("\nCount occurrence of 2 in dob column:")
df['count'] = list(map(lambda x: x.count("2"), df['name_code']))
print(df)

#2
import pandas as pd
df = pd.DataFrame({
'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],
'date_of_sale': ['12/05/2002','16/02/1999','25/09/1998','12/02/2022','15/09/1997'],
'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]
})
print("Original DataFrame:")
print(df)
print("\nSwapp cases in comapny_code:")
df['swapped_company_code'] = list(map(lambda x: x.swapcase(), df['company_code']))
print(df)

#3
import numpy as np
ar1=np.array(35)
print("Zero dimensional array:",ar1)
ar2=np.array([2,3,4])
print("One dimensional array:",ar2)
ar3=np.array([[1,2,6,7],[8,3,4,9]])
print("Two dimensional array:",ar3)
ar4=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("Three dimensional array:",ar4)
ar5=np.array([1,2,3,4],ndmin=5)
print("Multi dimensional array:",ar5)
print("Accesing elements")
print("2nd element in ar2:",ar2[1])
print("3rd element in 2nd row of ar3:",ar3[1,2])
print("Accessing 5 from ar4:",ar4[1,0,0])
print("Slicing:")
print(ar3[1,1:3])
