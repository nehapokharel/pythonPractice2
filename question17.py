num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
operator = input("Enter operator: ")




if operator == '+':
    result = num1 + num2
    print(result)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 == 0:
        print("Can't divide by zero")
    else:
        print(int(num1/num2))
else:
    print("Sorry cannot perform operation!!")