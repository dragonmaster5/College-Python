#Problem 1
#1) True
#2)True
#3)False
#4)True
#5)False
#6)True
#7)True
#Problem 2
#1) Prints: 99
#2) Prints: 5
#3) Prints: 2
#Problem 3
import math


def PassFail(final_score, bonus_points):
    if(int(final_score)+int(bonus_points)>=80) :
        return True
    else :
        return False

if(PassFail(input("Please enter your score on the final exam: "),input("please enter how many bonus points you recieved: "))):
        print("You Passed!")
else:
        print("You Failed...")

#Problem 4
def SchoolSize(size):
    if(int(size) >= 3000 and int(size) <= 16000) :
        print("This University is medium sized")
    else :
        print("This University is not considered medium sized")

SchoolSize(input("How many students does the school have? "))
#Problem 5
def willRecieveBenefits(Hours,Years):
    if((int(Hours)>=40 and int(Years)>=2) or (int(Hours)>=35 and int(Years)>=5)) :
            print("you receive benefits")
    else :
        print("you do not recieve benefits")

willRecieveBenefits(input("how many hours did you work: "), input("How many years have you been at the company: "))

#problem 6
def sequentialSort(bounds): #uses a sequential sort to sort the bounds for conditional ladders in  least to greatest
    i=0
    while i<(len(bounds)-1) : #checks if i is still less than the length of bounds -1
        if bounds[i]>bounds[i+1]: #checks if bounds at index i is greater than bounds at index i + 1
            temp=bounds[i+1] #if true it sets a temporary variable = to bounds at index i+1
            bounds[i+1]=bounds[i] # then sets bounds i to bounds i + 1  and bounds i to temp
            bounds[i]=temp
            i=i-i #resets the sequence to check if the previous number is bigger as well, i know it's not most efficient way to do that
        else :
            i+=1# moves to the next index in the loop
    return bounds

def dynamicConditionalStatements(sortedbounds, n): #returns an i value which corresponds to an index of a result list
    #not super dynamic but these are helper methods so doesn't really matter
    sortedboundslen = len(sortedbounds)-1
    i = 0
    while (i <= sortedboundslen):
            if (n >= sortedbounds[sortedboundslen-i]):

                return i
            i+=1

def cBoundsInput(boundsinput): #input for bounds
    boundsinput=sequentialSort(boundsinput)
    return boundsinput
def passwordStrength(password):
    Passwordbounds = cBoundsInput([0, 8, 12])
    Passwordresults = ["Strong", "Moderate", "Weak"]
    Passwordresult = Passwordresults[dynamicConditionalStatements(Passwordbounds,len(password))]
    print("Password Strength", Passwordresult)
passwordStrength(input("please input a password: "))
#problem 7, I got really tired of writing conditional ladders without switch statements
age=int(input("how old are you?"))
bounds= cBoundsInput([0,3,13,20,65])
results = [8,20,15,10,"free"]
 #check for returning none and sets result equal to the final payment value
result=results[dynamicConditionalStatements(bounds,age)]
print("you will pay ", result)

#problem 7
moneySpent= int(input("How much money did you spend: "))
discountBounds=cBoundsInput([200,120,80])
resultsDiscount=[0.2,0.15,0.1,0]
try:
    resultDiscount=resultsDiscount[dynamicConditionalStatements(discountBounds,moneySpent)]
except:
    resultDiscount=0
discount=moneySpent*resultDiscount
totalPayment= moneySpent-discount
print("you'll pay", totalPayment)
#Problem 9
def shippingCost(amazonPrime,weight,zone ):
   if(amazonPrime.lower()=="yes") :
        return 0
   elif(int(zone)==1):
       if(int(weight)<=10):
           return 10
       else:
           return 20
   elif(int(zone)==2) :
       if (int(weight)<= 10):
           return 30
       else :
           return 50


print(shippingCost(input("do you have amazon prime? "),input("How much does your package weigh? "),input("what Zone are you in? type 1 for national and 2 for international ")))
#problem 10
income=int(input("how much money do you make?"))
assistanceBounds=cBoundsInput([-2147483647,40001,70000])
resultsIncome=["No Assistance","Partial Assistance","Full Assistance"]
try:
    resultIncome=resultsIncome[dynamicConditionalStatements(assistanceBounds,income)]
except:print("please enter a real number")
print(f"you'll recieve {resultIncome}")
#problem 11 Was i supposed to write that myself?
def sqrt(n):
   print(math.sqrt(n))
#Problem 12
def minToSec(n) :
    print(n*60)
#Problem 13
def speedLimitFineCalc(speedLimit,speed):
    if(speed>speedLimit+10):
        print("you have been fined $100")
    elif(speed>speedLimit) :
        print("you have been fined $50")
    else :
        print("no Fine")
#Problem 14
def movieTheaterTickets(age):
    TheaterBounds = cBoundsInput([0, 6, 12, 65])
    results = [10, 20, 15, "free"]
    result = results[dynamicConditionalStatements(TheaterBounds, int(age))]
    print("To enter you must pay: ", result)
movieTheaterTickets(input("how old are you? (Problem 15 prompt) "))
#Problem 16
def BankWithdrawl(balance, ammount):
    if(balance>ammount):
        print("remaining balance: ",balance-ammount)
    else :
        print("Insufficient funds")

BankWithdrawl(0, 1000)
