first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
action = input('Choose one of these operations (+, -, *, /): ')

if action in ('+', '-', '*', '/'):
    if action == '+':
        result_value = first_number + second_number
        print(f'The sum of two numbers is equal: {result_value}')
    elif action == '-':
        result_value = first_number - second_number
        print(f'The difference between the two numbers is equal: {result_value}')
    elif action == '*':
        result_value = first_number * second_number
        print(f'The multiplication of two numbers equals: {result_value}')
    elif action == '/':
        if not second_number == 0:
            result_value = first_number / second_number
            print(f'The division of two numbers equals: {result_value}')
        else:
            print('You cannot divide by 0')
else:
    print('You should choose one of these symbols (+, -, *, /). Try again')
