#1
import numpy as np
import pandas as pd
s = pd.Series(['X', 'Y', 'Z', 'Aaba', 'Baca', np.nan, 'CABA', None, 'bird', 'horse', 'dog'])
print("Original series:")
print(s)
print("\nConvert all string values of the said Series to upper case:")
print(s.str.upper())
print("\nConvert all string values of the said Series to lower case:")
print(s.str.lower())
print("\nLength of the string values of the said Series:")
print(s.str.len())

#2
color1 = pd.Index(['   Green', 'Black ', '  Red  ', 'White', ' Pink   '])
print("Original series:")
print(color1)
print("\nRemove whitespace")
print(color1.str.strip())
print("\nRemove left sided whitespace")
print(color1.str.lstrip())
print("\nRemove Right sided whitespace")
print(color1.str.rstrip())
