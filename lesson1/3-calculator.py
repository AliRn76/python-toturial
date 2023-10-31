number1 = int(input())
number2 = int(input())
operator = input()

# +, -, *, /, //, %

if operator == '+':
    number3 = number1 + number2
    print(number3)

elif operator == '-':
    number3 = number1 - number2
    print(number3)

elif operator == '*':
    number3 = number1 * number2
    print(number3)

elif operator == '/':
    number3 = number1 / number2
    print(number3)

else:
    print('operator is wrong')
