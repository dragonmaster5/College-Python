#Problem 1
hours=int(input(" Enter Hours:"))
rateOfPay=float(input(" Enter Pay Rate:"))
if(hours>40) :
    adjustedHours=hours-40
    overtimepay= adjustedHours*(rateOfPay*1.5)
    print(((hours-adjustedHours)*rateOfPay)+overtimepay)
else:
    print(hours*rateOfPay)
#Problem 2
try :
    hours=int(input(" Enter Hours:"))
    rateOfPay=float(input(" Enter Pay Rate:"))


    if(hours>40) :
        adjustedHours=hours-40
        overtimepay= adjustedHours*(rateOfPay*1.5)
        print(((hours-adjustedHours)*rateOfPay)+overtimepay)
    else:
        print(hours*rateOfPay)
except:
    print("Please Enter a Number")
#problem 3
score = float(input("Please enter a score between 0-1.0: "))
if(score<1) :
    if(score<0.6):
        print("F")
    elif(score<0.7):
        print("D")
    elif(score<0.8):
        print("C")
    elif(score<0.9):
        print("B")
    elif(score<=1):
        print("A")
else:
    print("Bad Score")


