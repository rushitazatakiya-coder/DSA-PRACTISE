#Creating array using array

from numpy import *
arr=array([10,20,30,40,50],int)
print(arr)

arr = array([1.5, 2.5, 3, 4, -5.1], float)
print(arr)

arr = array(['a', 'b', 'c', 'd'])
print(arr)

arr = array(['Delhi', 'Hyderabad', 'Mumbai', 'Ahmedabad'], dtype=str)
print(arr)

arr = array([1,2,3,4,5])
print(arr)

#Creating Arrays using linspace

from numpy import *
a = linspace(0, 10, 5) 
print(a)

#Creating Arrays using logspace

from numpy import *
a = logspace(1, 4, 5)
print(a)

#Creating Arrays using arange() Function

from numpy import *
a = arange(1, 10, 3)
print(a)

a = arange(10)
print(a)

a = arange(5, 10)
print(a)

#Creating Arrays using zeros() and ones() Functions

from numpy import *
a = zeros(5)
print(a)

a = zeros(5, int)
print(a)

a = ones(5, float)
print(a)




