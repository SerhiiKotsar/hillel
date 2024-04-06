# 1. Перепишіть наш калькулятор (який ми робили  в іншій домашці) за допомогою функцій.
def add_numbers(num_1, num_2):
    return num_1 + num_2


def subtract_numbers(num_1, num_2):
    return num_1 - num_2


def multiply_numbers(num_1, num_2):
    return num_1 * num_2


def divide_numbers(num_1, num_2):
    return num_1 / num_2


first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))
operator = input('Choose one of these operators: (+, -, *, /): ')

if operator == '+':
    result = add_numbers(num_1=first_number, num_2=second_number)
    print(f'The sum of two numbers is equal: {result}')
elif operator == '-':
    result = subtract_numbers(num_1=first_number, num_2=second_number)
    print(f'The difference between the two numbers is equal: {result}')
elif operator == '*':
    result = multiply_numbers(num_1=first_number, num_2=second_number)
    print(f'The multiplication of two numbers equals: {result}')
elif operator == '/':
    try:
        result = divide_numbers(num_1=first_number, num_2=second_number)
        print(f'The division of two numbers equals: {result}')
    except ZeroDivisionError:
        print('You cannot divide by 0')
else:
    print('You should choose one of these symbols (+, -, *, /). Try again')
