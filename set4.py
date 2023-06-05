#1
import numpy as np
import pandas as pd
ed = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df=pd.DataFrame(ed,index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(df)

#2
import pandas as pd
ed = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df=pd.DataFrame(ed,index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(df)
print("\nChange the name 'James' to ‘Suresh’:")
df['name'] = df['name'].replace('James', 'Suresh')
print(df)

#3
a=np.array([[8,3],[6,9]])
b=np.array([[2,5],[7,8]])
print("Add:")
print(np.add(a,b))
print("Subtract:")
print(np.subtract(a,b))
print("Multiply:")
print(np.multiply(a,b))
print("Divide:")
print(np.divide(a,b))
c=np.array([[4,16],[9,25]])
print("Sqrt:")
print(np.sqrt(c))
d=np.array([1,30,45,60,90])
print("sin:",np.sin(d*np.pi/180))
print("cos:",np.cos(d*np.pi/180))
e=np.array([2,4,3,6])
print("log:",np.log(e))
p=np.array([3,8j])
q=np.array([7,2j])
print("Dot:",np.dot(p,q))
r=np.array([1,-1,-6])
print("Roots:",np.roots(r))

