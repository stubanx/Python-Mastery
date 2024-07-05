num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
op= input("""
          '+': Addition
          '-': Subtraction
          '/': Division
          '*': Multiplication
          '%': Get remainder
          Enter the operation to perform: 
          """)
match(op):
    case '+':
        print(f'The Addition of {num1} and {num2} is {num1+num2}.')
    case '-':
        print(f'The Subtraction of {num1} and {num2} is {num1-num2}.')
    case '*':
        print(f'The Multiplication of {num1} and {num2} is {num1*num2}.')
    case '/':
        print(f'The Quotient of {num1} and {num2} is {num1/num2}.')
    case '%':
        print(f'The Remainder of {num1} when divided by {num2} is {num1%num2}.')
    case _:
        print(f"'{op}' entered is Invalid")
