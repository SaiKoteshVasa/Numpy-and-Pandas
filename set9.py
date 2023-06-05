#1
import numpy as np
print("Concatenate two strings:")
print(np.char.add(['hello'],['xyz']))
print(np.char.add(['hello','hii'],['abc','xyz']))
print("Multiply:")
print(np.char.multiply('srkr ',3))
print("Center:")
print(np.char.center('hello',20,fillchar='*'))
print("Capitalize:")
print(np.char.capitalize('hello world'))
print("Title:")
print(np.char.title('hello!! how are you?'))
print("Lower:")
print(np.char.lower('Hello SRKR'))
print("Upper:")
print(np.char.upper('python lab'))
print("Split:")
print(np.char.split(('Numpy and Pandas'),sep=' '))
print("Splitlines:")
print(np.char.splitlines('hello\nhow are you??'))
print("Strip:")
print(np.char.strip('bhimavaram','a'))
print("Join:")
print(np.char.join(':','dmy'))
print(np.char.join([':','-'],['dmy','ymd']))
print("Replace:")
print(np.char.replace('This is java lab','java','python'))

#2
import pandas as pd
df=pd.read_excel(r"C:\Users\SAI KOTESH\Documents\emp.xlsx")
print(df)

#3
df=pd.read_excel(r"C:\Users\SAI KOTESH\Documents\emp.xlsx")
print("Sum:",df['Age'].sum())
print("Mean:",df['Age'].mean())
print("Min:",df['Age'].min())
print("Max:",df['Age'].max())

