print("\n #1 Variables")

#1.Create variable to store name, age, and city and display them.
name="Rushita"
age=21
city="Rajkot"
print(name)
print(age)
print(city)

#2.swap the values of two variable.
a = 10
b = 20
print("Before swapping:")
print("a =", a)
print("b =", b)
a,b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)

#3.Calculate the area of a rectangle using variables.
length = 10
width = 5
area = length * width
print("Length =", length)
print("Width =", width)
print("Area of Rectangle =", area)

#4.Calculate simple interest using variables.
P = 10000
R = 5
N = 2
SI = (P * R * N) / 100
print("Principal =", P)
print("Rate =", R)
print("Time =", N)
print("Simple Interest =", SI)

#5.Convert celsius temperature to Fahrenheit.
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
print("Celsius =", celsius)
print("Fahrenheit =", fahrenheit)

print("\n #2. Data types")

#1.Demonstrate int, float, str, bool, and complex.
a=10
b=10.92
c="Welcome to Atmiya University"
d=True
e=3+4j
print(a)
print(b)
print(c)
print(d)
print(e)

#2.Accept two numbers and display their data types.
n1 = input("Enter first number: ")
n2 = input("Enter second number: ")
print("First number:", n1)
print("Data type:", type(n1))
print("Second number:", n2)
print("Data type:", type(n2))

#3.convert a string number into an integer and float.
num = "25"
integer_num = int(num)
float_num = float(num)

print("Original value:", num)
print("Integer value:", integer_num)
print("Float value:", float_num)

#4.find the length of a string.
a="hello world"
print(len(a))

#5.Create a list,tuple,set and dictionary and display their types.
my_list = [10, 20, 30, 40]
my_tuple = (10, 20, 30, 40)
my_set = {10, 20, 30, 40}
my_dict = {
    "name": "Rahul",
    "age": 20
}

print("List:", my_list)
print("Type:", type(my_list))

print("Tuple:", my_tuple)
print("Type:", type(my_tuple))

print("Set:", my_set)
print("Type:", type(my_set))

print("Dictionary:", my_dict)
print("Type:", type(my_dict))

print("\n #3.operators")

#1. Perform addition, subtraction, multiplication, and division.
a=10
b=40

print(a+b)
print(a-b)
print(a*b)
print(a/b)
#2. Find the remainder and quotient of two numbers.
n1=34
n2=5
quotient = n1 // n2
remainder = n1 % n2

print("Quotient:", quotient)
print("Remainder:", remainder)
#3. Check whether a number is even or odd.
a=9
if(a%2==0):
    print("even")
else:
    print("odd")
#4. Compare two numbers using relational operators.
a=4
b=8

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
    
#5. Demonstrate logical operators (and, or, not).
a = True
b = False
print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)

#6. Demonstrate assignment operators (+=, -=, *=, /=).
num = 10
num += 5
print("After += 5:", num)
num -= 3
print("After -= 3:", num)
num *= 2
print("After *= 2:", num)
num /= 4
print("After /= 4:", num)

#7. Find the largest of two numbers using comparison operators.
a=10
b=3

if(a>b):
    print(a)
elif(b>a):
    print(b)
else:
    print('both number are equal')
    
print(" \n #4. Conditions")

#1. Check whether a number is positive, negative, or zero.
a=5

if(a>0):
    print("positive")
elif(a<0):
    print("negative")
else:
    print("zero")
#2. Check whether a person is eligible to vote.
a=19
if(a>18):
    print("person is eligible to vote")
else:
    print("person are not eligible to vote")
#3. Find the largest of three numbers.
a=8
b=4
c=1
if(a>b):
    if(a>c):
        print("a is max")
    else:
        print("c is max")
else:
    if(b>c):
        print("b is max")
    else:
        print("c is max")
        
#4. Check whether a year is a leap year
year = int(input("Enter a year: "))
if year % 4==0:
    print("Leap Year")
else:
    print("Not a Leap Year")
#5. Create a grade system based on marks.
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")
    
#6. Check whether a number is divisible by 5 and 11.
n=7
if n % 5 == 0 and n % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible by 5 and 11")
    
#7. Create a simple calculator using if-elif-else.
a1 = float(input("Enter first number: "))
a2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result =", a1 + a2)

elif operator == "-":
    print("Result =", a1 - a2)

elif operator == "*":
    print("Result =", a1 * a2)

elif operator == "/":
    if a2 != 0:
        print("Result =", a1 / a2)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")

print("\n #5. Loops")

#1. Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)
    
#2. Print numbers from 10 to 1 using a while loop.
i = 10
while i >= 1:
    print(i)
    i -= 1
    
#3. Print the multiplication table of a number.
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
#4. Find the sum of numbers from 1 to n.
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum =", sum)

#5. Find the factorial of a number.
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)

#6. Print all even numbers between 1 and 100.
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
        
#7. Reverse a number using a loop.
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number =", reverse)

#8. Count the digits of a number.
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Number of digits =", count)

#9. Check whether a number is prime.
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print("Prime number")
    else:
        print("Not a prime number")
        
#10. Print Fibonacci series up to n terms.
n = int(input("Enter number of terms: "))
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

print("\n #6. Function")

#1. Write a function to print "Hello, World!".

def hello():
     print("Hello, World!")
hello()
    
# 2. Write a function that takes a name and prints a greeting.

def greet(name):
    print("Hello,", name)
greet("Rushita")

#3. Write a function to add two numbers.

def add(a,b):
    return a + b
result = add(10,20)
print("Sum =", result)

#4. Write a function to find the square of a number.
def square(num):
    return num * num
result = square(5)
print("Square =", result)

#5. Write a function to check whether a number is even or odd.
def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_even_odd(10)
        
#6.Write a function to find the maximum of two numbers.
def check_max(no1,no2):
    if(no1>no2):
        print("No1 is maximum")
    else:
        print("No2 is maximum")
check_max(8,5)

#7. Write a function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
result = celsius_to_fahrenheit(25)
print("Fahrenheit =", result)

#8. Write a function to calculate the area of a circle.

def area_circle(radius):
    return 3.14 * radius * radius

result = area_circle(6)
print("Area of Circle =", result)

#9. Write a function to calculate the factorial of a number.
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

num = 5
print("Factorial =", factorial(num))

#10. Write a function to check whether a number is positive, negative, or zero.

def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

check_number(10)

#11. Write a function to find the maximum of three numbers.

def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
result = maximum(10, 25, 15)
print("Maximum =", result)

#12. Write a function to count vowels in a string.

def count_vowels(text):
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return count

string = "Hello World"
print("Number of vowels =", count_vowels(string))

#13. Write a function to reverse a string.

def reverse_string(text):
    return text[::-1]

string = "Hello"
print("Reversed string =", reverse_string(string))

#14. Write a function to check whether a string is a palindrome.

def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

string = "madam"

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not Palindrome")

#15. Write a function to find the sum of all elements in a list.

def list_sum(numbers):
    total = 0

    for num in numbers:
        total += num
    return total

numbers = [10, 20, 30, 40, 50]
print("Sum =", list_sum(numbers))

#16. Write a function to find the largest element in a list.

def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [10, 25, 15, 40, 30]
print("Largest element =", find_largest(numbers))

#17. Write a function to remove duplicate elements from a list.

def remove_duplicates(numbers):
    return list(set(numbers))

numbers = [10, 20, 10, 30, 20, 40]
result = remove_duplicates(numbers)
print("List after removing duplicates:", result)

#18. Write a function to count how many times an element appears in a list.

def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count += 1
    return count

numbers = [10, 20, 10, 30, 10, 40]
result = count_element(numbers, 10)
print("Element appears", result, "times")

#19. Write a function to check whether a number is prime.

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number = 7
if is_prime(number):
    print("Prime")
else:
    print("Not Prime")

#20. Write a function to return all prime numbers between two numbers.

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_numbers(start, end):
    primes = []

    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes
result = prime_numbers(10, 30)
print("Prime numbers:", result)

#21. Write a function to calculate Fibonacci numbers.

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("Enter number of terms: "))
fibonacci(n)

#22. Write a function to find the second-largest number in a list.

def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]

numbers = [10, 25, 5, 40, 30]
result = second_largest(numbers)
print("Second largest number:", result)

#23. Write a function to sort a list without using sort().

def sort_list(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

numbers = [5, 2, 8, 1, 3]
result = sort_list(numbers)
print("Sorted list:", result)

#24. Write a function to merge two lists and remove duplicates.

def merge_remove_duplicates(list1, list2):
    merged = list1 + list2
    result = []

    for item in merged:
        if item not in result:
            result.append(item)
    return result

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result = merge_remove_duplicates(list1, list2)
print("Merged list without duplicates:", result)
