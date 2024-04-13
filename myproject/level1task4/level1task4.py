## Simple Calculator ##

num1= int(input("Enter the num value : "))
num2= int(input("Enter the num value : "))
operator = input("Enter the operator +,-,*,/,% : ")
match operator:
    case "+":
        print(num1 +num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case "%":
        print(num1%num2)
    case _:
        print("not a valid key")

