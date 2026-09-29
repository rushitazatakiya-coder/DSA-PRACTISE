# to import array in our programme we have three methods

#1 import array

import array
a=array.array('i',[10,20,30,40,50])
for i in range(5):
    print(a[i])

#2 import array as arr

import array as arr
a=arr.array('i',[1,2,3,4,5])
for i in range(5):
    print(a[i])

#3 from array import *

from array import *
a=array('i',[11,22,33,44,55])
for i in range(5):
    print(a[i])





