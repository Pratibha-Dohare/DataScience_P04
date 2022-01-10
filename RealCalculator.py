def add(a,b):
    addition=a+b
    print(f"The sum of {a} and {b} is {c} ".format(a=number1,b=number2,c=addition)) #formatted strings

def subtract(a,b):
    subtraction=a-b
    print(f"The result of subtracting {b} from {a} is {d}".format(a=number1,b=number2,d=subtraction))

def multiply(a,b):
    multiplication=a*b
    print(f"The multiplication of {a} and {b} is {e}".format(a=number1,b=number2,e=multiplication))

def division(a,b):
    divide=a/b
    print(f"The division of {a} and {b} is {g}".format(a=number1,b=number2,g=divide))
    
def mod(a,b):                            # add a function here which accepts the modulus operator '%' - 10%3 == 1
    modulo=a%b
    print(f"The modulo of {a} and {b} is {h}".format(a=number1,b=number2,h=modulo))

# accepting multiple inputs in a single
number1,operator,number2 = map(str, input("Enter your equation: ").split()) # 2 +4
number1 = int(number1)
number2 = int(number2)

# shift+alt+down

if operator =="+":
    add(number1,number2)
    
elif operator == "-":
    subtract(number1,number2)
    
elif operator == "*":
    multiply(number1,number2)
    
elif operator == "/":
    division(number1,number2)
    
elif operator=="%":
    mod(number1,number2)
    
else:
    print("Invalid Typo Error! Type something like - 8 / 4")
    


