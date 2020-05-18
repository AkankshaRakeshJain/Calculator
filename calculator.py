class Calculator:
    def __init__(self,num1,num2,operator):
        if operator == '+':
            print(num1 + num2)
        elif operator == '-':
            print(num1 - num2)
        elif operator == '*':
            print(num1 * num2)
        elif operator == '/':
            print(num1 / num2)

choice = input('Select option\n (1) Addition\n (2) Subtraction\n (3) Multiplication\n (4) Division\n ')
if choice == '1':   operator = '+'
elif choice == '2': operator = '-'
elif choice == '3': operator = '*'
elif choice == '4': operator ='/'

if choice in ('1234'):
    num1,num2 = map(int,input('Enter two number:').split())
    cal = Calculator(num1,num2,operator)
else:
    print('Invalid Input')