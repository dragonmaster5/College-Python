#Problem 1
'''
Indicate whether the expression evaluates to True or False. x = 7, y = 9.
'''
#1) True
#2)True
#3)False
#4)True
#5)False
#6)True
#7)True
#Problem 2
'''
What is the printed value of y in each of the following cases?
'''
#1) Prints: 99
#2) Prints: 5
#3) Prints: 2
#Problem 3
import math
'''
A student is taking a course with a Pass/Fail option. Their final grade is
determined by the final exam score and any bonus points they receive. The passing criteria
are as follows:
• The student passes if the total score, which is the sum of the exam score and bonus
points, is 80 or above.
• If the total score is below 80, the student fails.
Define variables that represent the final score and the bonus points of a student. Based on
these values, determine whether this student passes or fails the course.
'''

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
'''
A university classifies its size based on the number of students enrolled. The
rule for its classification system is as follows
• A university is classified as “Medium-sized” if the number of students enrolled is
between 3,000 and 16,000 inclusive.
• If the number of students enrolled is outside this range, it is classified as not
medium-sized.'''
def SchoolSize(size):
    if(int(size) >= 3000 and int(size) <= 16000) :
        print("This University is medium sized")
    else :
        print("This University is not considered medium sized")

SchoolSize(input("How many students does the school have? "))
#Problem 5
'''
A small company in Madison Wisconsin offers benefits based on employee
work hours and tenure. The eligibility criteria for benefits are as follows: An employee is
eligible for benefits if at least one of the following conditions is satisfied
(1) They have worked at least 40 hours per week and have been with the company for
2 years or more.
(2) Or, if they have worked at least 30 hours per week and have been with the company
for 5 years or more.
'''
def willRecieveBenefits(Hours,Years):
    if((int(Hours)>=40 and int(Years)>=2) or (int(Hours)>=35 and int(Years)>=5)) :
            print("you receive benefits")
    else :
        print("you do not recieve benefits")

willRecieveBenefits(input("how many hours did you work: "), input("How many years have you been at the company: "))

#problem 6
'''
Write a Python program that takes a password as input and prints:
• “Strong” if the password length is greater than 12 characters.
• “Moderate” if the password length is between 8 and 12 characters (inclusive).
• “Weak” if the password length is less than 8 characters.
'''
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
'''
You are organizing an event where ticket prices vary based on the attendee’s
age. Write a program that takes the age of an attendee as input and determines the ticket
price according to the following rules.
'''
age=int(input("how old are you?"))
bounds= cBoundsInput([0,3,13,20,65])
results = [8,20,15,10,"free"]
 #check for returning none and sets result equal to the final payment value
result=results[dynamicConditionalStatements(bounds,age)]
print("you will pay ", result)

#problem 7
'''
 A clothing store offers a discount based on the amount spent by a customer.
The discounts are applied as follows.
• If the total amount spent is greater than $200, the customer gets a 20 % discount.
• If the total amount spent is between $120 and $200, the customer gets a 15 %
discount.
• If the total amount spent is between $80 and $120, the customer gets a 10 %
discount.
• Otherwise, there’s no discount.'''
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
'''
Amazon offers different shipping rates based on the weight of a package and
whether the customer has an Amazon Prime membership. It uses the following rules to
calculate shipping costs:
• Amazon Prime Members: All packages, regardless of weight, ship for free.
• Non-Prime Members:
(1) Zone 1 (Local): Packages up to 10 lb: $10. Packages over 10 lb: $20.
(2) Zone 2 (International): Packages up to 10 lb: $30, Packages over 10 lb: $50'''
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
'''
A childcare center provides financial assistance based on family income. The
assistance categories are:
• “Full Assistance” if the family income is $40,000 or less.
• “Partial Assistance” if the family income is between $40,001 and $70,000.
• “No Assistance” if the family income is above $70,000.
Write a Python program to ask the user to enter the family income. Based on their
answer, determine the type of a'''
income=int(input("how much money do you make?"))
assistanceBounds=cBoundsInput([-2147483647,40001,70000])
resultsIncome=["No Assistance","Partial Assistance","Full Assistance"]
try:
    resultIncome=resultsIncome[dynamicConditionalStatements(assistanceBounds,income)]
except:print("please enter a real number")
print(f"you'll recieve {resultIncome}")
#problem 11 Was i supposed to write that myself?
'''. Write a function that takes a number n and prints out its square root √
n.
'''
def sqrt(n):
   print(math.sqrt(n))
#Problem 12
'''
Write a function that takes a number of minutes as input, converts it to
seconds, and prints out the result.'''
def minToSec(n) :
    print(n*60)
#Problem 13
'''Write a function that takes the total bill amount and the tip percentage as
inputs, and print out the total amount including the tip.
'''
def billCalc(tip,bill):
    return bill+(bill*tip)
#Problem 14
'''
Write a function that takes the speed and speed limit as inputs, and prints
out the speeding fine. Here are the rules
3
• If the driver is within the speed limit, there is no fine.
• If the driver exceeds the speed limit by up to 10 km/h, the fine is $50.
• If the driver exceeds the limit by more than 10 km/h, the fine is $100.
Here are two examples to demonstrate this problem. If the speed limit is 60 km/h and
the driver is going 65 km/h, the fine is $50. If the driver is going 82 km/h, the fine is $100'''
def speedLimitFineCalc(speedLimit,speed):
    if(speed>speedLimit+10):
        print("you have been fined $100")
    elif(speed>speedLimit) :
        print("you have been fined $50")
    else :
        print("no Fine")
#Problem 14
'''
Write a function to process price at a movie theater. The function should
take age as an input and print out the price of a movie ticket based on a person’s age. The
ticket prices are as follows:
• Below 5: Free.
• 6-12: $15
• 12 to 64: $20
• 65 and older: $10
'''
def movieTheaterTickets(age):
    TheaterBounds = cBoundsInput([0, 6, 12, 65])
    results = [10, 20, 15, "free"]
    result = results[dynamicConditionalStatements(TheaterBounds, int(age))]
    print("To enter you must pay: ", result)
movieTheaterTickets(input("how old are you? (Problem 15 prompt) "))
#Problem 16
'''Write a function to process a bank withdrawal. The function should take
two inputs: the balance and the withdrawal amount. The function should do the following
• If there are enough funds, subtract the withdrawn amount from the balance, and
print out the remaining balance.
• If the withdrawal amount is greater than the balance, the function should print
“Insufficient funds” instead of reducing the balance'''
def BankWithdrawl(balance, ammount):
    if(balance>ammount):
        print("remaining balance: ",balance-ammount)
    else :
        print("Insufficient funds")

BankWithdrawl(0, 1000)
