#Textbook problem #1
print("hello", input("what is your name "))

#Textbook problem #2
hours=int(input(" Enter Hours:"))
rateOfPay=float(input(" Enter Pay Rate:"))
print(hours*rateOfPay)

#Textbook Problem #3
#1) Int
#2) Float
#3) Float
#4) Int

#Textbook Problem #5
celsius=int(input("enter temperature in celsius:"))
print((celsius*(9/5)+32))


#Problem 1
# 1) Prints:10
#2) Prints: 9
#3) Prints:10
#Problem 2
#x=9, y=8, z=6
import math

#Problem 3
# 1) x=12
# 2) x=18
# 3) x=33

#Problem 4
x = 21
y = 4
sum = x + y
difference = x - y
product = x * y
quotient = x / y
IntQuotient = x // y
print("Sum =", sum, "\n", "Difference =", difference, "\n", "Product =", product, "\n", "the quotient is", quotient,
      "\n", "the Int quotient is", IntQuotient)
#Problem 5
length = 10
width = 6
print("the area is", length * width)
print("the circumference", 2 * (length + width))

#Problem 6
#1)
a = 2
b = 5
c = 1
result = 3 * ((a ** 2) + (2 * b ** 3)) - (2 ** c)
print(result)
#Type is an int since every value given is an int
#2)
a = 3
b = 1
c = 2
result = 2 ** (a - b * c) - (a / c)
print(result)
#type is a float because integer division doesn't exist naturally in python, does not truncate
#3)
a=3
b=5
c=-2
result= (b%a-c)*c**2
print(result)
#type is int because there is no division

#Problem 7
First_Name="William"
Midde_Name=" Henry"
Last_Name=" Draper"
Full_Name=First_Name+Midde_Name+Last_Name
print(Full_Name)
#then middle name would just be an empty space/ conditional to print something else if middle name is null

#Problem 8
age=18
Name ="Billy"
print("Billy is ", str(age),"years old.")


#print("hi", input("what is your name?"))
#int = int(input('what is the radius'))
#print(math.pi * int ** 2)
