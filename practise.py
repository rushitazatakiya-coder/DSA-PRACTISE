Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
a
10
print(a)
10
id(a)
140723647194520
a=20
id(a)
140723647194840
a=10.10
print(a)
10.1
a='z'
print(a)
z
a="Hello Student"
print(a)
Hello Student
a=input()
10
print(a)
10
a=float(input())
10.24
print(a)
10.24
a=str(input())
Hello World
print(a)
Hello World
a=int(input("Enter Age = "))
Enter Age = 21
print(a)
21
a=int(input('Enter Age = '))
Enter Age = 21
print(a)
21

======= RESTART: D:/DSA/temp.py ======
10

======= RESTART: D:/DSA/temp.py ======
10
20
a=10
print(a)
10
a=15.25
print(a)
15.25
a=True
print(a)
True
a=False
print(a)
False
s1 = 'Hello Student'
print(s1)
Hello Student
s1 = "Hello Student"
print(s1)
Hello Student
s2 = 'Atmiya'
print(s2)
Atmiya
s1 + s2
'Hello StudentAtmiya'
s1 * 2
'Hello StudentHello Student'
print(s1)
Hello Student
s1[0]
'H'
s1[5]
' '
s1[6]
'S'
s1[-5]
'u'
s1[-3]
'e'
print(s1)
Hello Student
s1[0:10:2]
'HloSu'
s1[::]
'Hello Student'
s1[0:10]
'Hello Stud'
s1[0:10:2]
'HloSu'
s1[:10]
'Hello Stud'
s1[::2]
'HloSuet'
l=[1,2,3,4,5]
t=(11,22,33,44,55)
print(l)
[1, 2, 3, 4, 5]
print(t)
(11, 22, 33, 44, 55)
a=[11,12,11,13,14,15]
a[0]=100
print(a)
[100, 12, 11, 13, 14, 15]
a.append(50)
print(a)
[100, 12, 11, 13, 14, 15, 50]
>>> a.insert(3,300)
>>> print(a)
[100, 12, 11, 300, 13, 14, 15, 50]
>>> a.remove(50)
>>> print(a)
[100, 12, 11, 300, 13, 14, 15]
>>> a.pop()
15
>>> print(a)
[100, 12, 11, 300, 13, 14]
>>> a.clear()
>>> print(a)
[]
>>> b = [1,2,3,4,3,5,3,6,3]
>>> print(b)
[1, 2, 3, 4, 3, 5, 3, 6, 3]
>>> len(b)
9
>>> b.count(3)
4
>>> b.sort()
>>> print(b)
[1, 2, 3, 3, 3, 3, 4, 5, 6]
>>> b.reverse()
>>> print(b)
[6, 5, 4, 3, 3, 3, 3, 2, 1]
>>> sum(b)
30
min(b)
1
max(b)
6
