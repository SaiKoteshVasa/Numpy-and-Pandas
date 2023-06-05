#1
import numpy as np
ar1=np.array([[1,2,3],[4,5,6]])
print("Shape of a1:",ar1.shape)
ar2=np.array([1,2,3,4],ndmin=5)
print(ar2)
print("Shape of a2:",ar2.shape)

ar=np.array([[1,2,3],[5,6,7]])
print("Length:",len(ar))

ar1=np.array([1,2,3])
ar2=np.array([[1,2],[3,4]])
ar3=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(ar1.ndim)
print(ar2.ndim)
print(ar3.ndim)

ar=np.array([[1,2,3],[5,6,7]])
print("datatype:",ar.dtype)

ar=np.array([[1,2,3],[5,6,7]])
print(ar.astype(float))

ar=np.array([[1,2,3],[5,6,7]])
print(type(ar))

#2
import pandas as pd
a=pd.Series([3,1,8,4])
b=pd.Series([2,3,6,4])
add=a+b
print(add)
sub=a-b
print(sub)
mul=a*b
print(mul)
div=a/b
print(div)

#3
ar=np.array([10,12,13,15])
print("Numpy array:")
print(ar)
ser=pd.Series(ar)
print("Pandas Series:")
print(ser)
