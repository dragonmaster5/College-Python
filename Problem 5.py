
def calculator( x,y,operator) :
        if operator=="+" :
            return x+y
        elif operator=="-" :
            return x-y
        elif operator== "*" :
            return x*y
        elif operator=="/":
            if y>0 :
                return x/y
            else : return "Undefined"





print(calculator(int(input("enter a number: ")), int(input("enter another number: ")),input("Enter an operator: ")))

