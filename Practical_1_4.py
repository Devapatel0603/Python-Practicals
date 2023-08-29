a = float(input("Enter first number : "))
b = float(input("Enter second number : "))
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
print("Enter 5 for Modulo")
print("Enter 6 for Exit")
while(True):
    ch = int(input("Enter your choice : "))
    match(ch):
        case 1:
            print("Addition : ",a+b)
        case 2:
            print("Subtraction : ",a-b)
        case 3:
            print("Multiplication : ",a*b)
        case 4:
            print("Division : ",a/b)
        case 5:
            print("Modulo : ",a%b)
        case 6:
            exit()
        case _:
            print("Please, enter valid choice...")