#1
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print('First array:')
print(a)
print('Append elements to array:')
print(np.append(a, [7,8,9]) )
print('Append elements along axis 0:')
print(np.append(a, [[7,8,9]],axis = 0))
print('Append elements along axis 1:')
print(np.append(a, [[5,5],[7,9]],axis = 1))
print ('\n' )

import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
print('First array:')
print(a)
print ('Axis parameter not passed. The input array is flattened before insertion.')
print (np.insert(a,3,[11,12]))
print ('Broadcast along axis 0:')
print (np.insert(a,2,[11],axis = 0) )
print('Broadcast along axis 1:' )
print (np.insert(a,2,11,axis = 1))
print ('\n' )

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print( 'First array:' )
print(a)
print ('The shape of first array:' )
print (a.shape)
b = np.resize(a, (3,2))
print('Second array:' )
print(b)
print('The shape of second array:' )
print(b.shape)
# Observe that first row of a is repeated in b since size is bigger
print('Resize the second array:' )
b = np.resize(a,(3,3))
print(b)
print ('\n' )

import numpy as np
a = np.arange(12).reshape(3,4)
print('First array:')
print(a)
print('Array flattened before delete operation as axis not used:' )
print( np.delete(a,5) )
print ('Column 2 deleted:' )
print(np.delete(a,1,axis = 1))
print ('Row 2 deleted:' )
print(np.delete(a,1,axis = 0))
print ('A slice containing alternate values from array deleted:' )
a = np.array([1,2,3,4,5,6,7,8,9,10])
print (np.delete(a, np.s_[::2]))
print ('\n' )

import numpy as np
a = np.array([[1,2],[3,4]])
print('First array:')
print (a)
b = np.array([[5,6],[7,8]])
print ('Second array:' )
print (b)
# both the arrays are of same dimensions
print ('Joining the two arrays along axis 0:' )
print (np.concatenate((a,b)) )
print ('Joining the two arrays along axis 1:' )
print (np.concatenate((a,b),axis = 1))
print ('\n' )

import numpy as np
a = np.array([[1,2],[3,4]])
print('First array:')
print (a)
b = np.array([[5,6],[7,8]])
print ('Second array:' )
print (b)
print ('Horizontal stacking:' )
c = np.hstack((a,b))
print (c)
print ('\n' )

import numpy as np
a = np.array([[1,2],[3,4]])
print('First array:')
print (a)
b = np.array([[5,6],[7,8]])
print ('Second array:' )
print (b)
print ('Vertical stacking:' )
c = np.vstack((a,b))
print (c)

#2
from datetime import datetime
date1 = datetime(year=2020, month=12, day=25)
print("Date from a given year, month, day:")
print(date1)
from dateutil import parser
date2 = parser.parse("1st of January, 2021")
print("\nDate from a given string formats:")
print(date2)

#3
import pandas as pd
import numpy as np
from datetime import datetime
dates = [datetime(2011, 9, 1), datetime(2011, 9, 2)]
print("Time-series with two index labels:")
time_series = pd.Series(np.random.randn(2a), dates)
print(time_series)
print("\nType of the index:")
print(type(time_series.index))
