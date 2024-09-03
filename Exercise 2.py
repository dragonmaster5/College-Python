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
