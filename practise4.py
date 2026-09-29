#The ndim Attribute

from numpy import *
arr1 = array([1,2,3,4,5]) 
print(arr1.ndim)

arr2 = array([[1,2,3], [4,5,6]])
print(arr2.ndim)

arr3 = array([[[1,2,3], [4,5,6]]])
print(arr3.ndim)

#The shape Attribute

from numpy import *
arr1 = array([1,2,3,4,5])
print(arr1.shape)

arr2 = array([[1,2,3], [4,5,6]])
print(arr2.shape)

arr3 = array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3.shape)

#The size Attribute

from numpy import *
arr1 = array([1,2,3,4,5])
print(arr1.size)

arr2 = array([[1,2,3], [4,5,6]])
print(arr2.size)

arr3 = array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3.size)

#The Itemsize Attribute

from numpy import *
arr1 = array([1,2,3,4,5])
print(arr1.itemsize)

arr2 = array([[1,2,3],[4,5,6]])
print(arr2.itemsize)

#The Dtype Attribute

from numpy import *
arr1 = array([1,2,3,4,5])
print(arr1.dtype)

arr2 = array([[1,2,3], [4,5,6]])
print(arr2.dtype)

arr3 = array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3.dtype)

#The nbytes Attribute

from numpy import *
arr1 = array([1,2,3,4,5])
print(arr1.nbytes)

arr2 = array([[1,2,3], [4,5,6]])
print(arr2.nbytes)

arr3 = array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3.nbytes)





