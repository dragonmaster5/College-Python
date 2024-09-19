import math
#Problem 1
def polyPerimeter(numSides,lenSide):
    return numSides*lenSide
#Problem 2
def getHypotenous(a,b):
    return math.sqrt(a**2+b**2)

#Problem 3
def  distance(x1,x2,y1,y2):
    return math.sqrt(((x1-x2)**2)+((y1-y1)**2))
#p4
def  TotalStringLength(str1,str2):
    return len(str1+str2)
#p5
def address(city,state,zipcode):
    return f" {city}, {state},{zip}"
#p6
def applyDiscount(price,isMember):
    if(isMember):

        return price-(price*0.1)
    else :
        return price
#p7
def shippingCost(weight,express):
    if(express):
        if(weight<2):
            return 5
        else :
            return 10
    else :
        if (weight < 2):
            return 10
        else:
            return 20
#p8
def finalPrice(price,weight,express):
    if(price>=100):
        return 0
    else:
        return shippingCost(weight,express)
#p9
def countDownToFinal(start):
    if(start>0):
        while(start>0):
            print(start)
            start-=1
    else:
        print("please enter a postitive number")

countDownToFinal(10)

#p10
def Buzz(n):
    for i in range(1,n+1):
        if(i%3==0):
            print("Buzz")
        else:
            print(i)
print(Buzz(10))
#p11
def negativeSum(aList):
    suma=0
    for i in aList:
        if i<0:
            suma+=i
    return suma
print(negativeSum([-10,20,30,50,-20]))
#p12`
def evenPositiveSum(aList):
    suma=0
    for i in aList:
        if i>0 and i%2==0:
            suma+=i
#p13
'''
Write a function called maximal element(a list) that takes a list as an input.
The function will return the maximal element in the list. For example
'''
def Maximum(aList):
    maxi=0
    for i in aList:
        if(i>maxi):
            maxi=i
    return maxi
#p14
'''Write a function called is prime(n) that checks whether a number is a prime
number or not. A prime number is a number whose divisors are 1 and itself. For example:
2, 5, 7, and 11 are prime numbers while 6 is not.'''
def isPrime(n):
    num=n

    while n>1 :

        if num%n==0:
            return False
        n-=1
    return True
print(isPrime(2))
print(isPrime(6))

#p?
def sumOfDivsors(n):
    suma=0
    divisor=n
    while n>0:
        if divisor%n==0:
            suma+=n
        n-=1
    return suma

print(sumOfDivsors(10))
#p11
def sumOfSquares(n):
    if n==0:
        return n
    else :
        return math.sqrt(n)+math.sqrt(sumOfDivsors(n-1))

print(sumOfSquares(5))
#p12
def isSquare(n):
    return math.sqrt(n)>1 and math.sqrt(n)==int(math.sqrt(n))

print(isSquare(36))
#p13
def perfectSquare():
     i=0
     while i<100:
        if isSquare(i):
            print(i)
