# Задача 1. Написати програму, в якій необхідно видалити всі вказані літери з стрінги(string)
# Стрінгу(string) і літеру ввести з клавіатури.

users_string_first = input('Write here your first string, please: ')
users_letter = input('Choose letter to delete from your string: ')
after_format_first = users_string_first.replace(users_letter, '')
print(f'You wrote: {users_string_first}, then chose letter: {users_letter}. After update you string is: {after_format_first}')

# Задача 2. Написати програму, яка візьме string і в кожному слові замінить першу літеру на велику.
# string ввести з клавіатури
# Приклад: "This is some test STRING"
# Відповідь: "This Is Some Test String"

users_string_second = input('\nWrite here your second string, please: ')
after_format_second = users_string_second.title()
print(f'You wrote: {users_string_second}. After update you string is: {after_format_second}')

# Задача 3. Напишіть програму яка перевертає стрінгу

before_overturn = 'hillel it school'
after_overturn = before_overturn[::-1]
print(f'\nYour string was: {before_overturn}, but now it is: {after_overturn}')

# Задача 4. Напишіть програму яка приймає на вхід 2 стрінги та порівнює їх

first_string_for_compare = input('\nWrite here your first string for compare, please: ')
second_string_for_compare = input('Write here your second string for compare, please: ')

if first_string_for_compare == second_string_for_compare:
    print(f'Your strings: {first_string_for_compare} and {second_string_for_compare} are the same')
else:
    print(f'Your strings: {first_string_for_compare} and {second_string_for_compare} are different')

# Задача 5.Напишіть програму яка візьме стрінг та повторить її задану кількість раз.
# До прикладу ми маємо стрінгу 'abc' та число 3. Результатом роботи програми має бути "abcabcabc"

test_string = 'abc'
test_number = 3
our_final_string = test_string * test_number
print(f'\nOur 3 times string is: {our_final_string}')

# Задача 6. Написати програму для підрахунку конвертації валюти:
# UAH --> USD
# доларів США --> грн
# UAH --> EUR
# євро --> грн

usd_per_uah = 38.32
eur_per_uah = 42.46

# user_uah_amount = int(input('Write here how much uah do you have: '))
user_currency_choice = input('\nChoose currency for exchange: write like one of these USD or EUR: ')

if user_currency_choice == 'USD':
    user_usd_amount = float(input('Write here how much USD do you want to get: '))
    user_usd_cost = user_usd_amount * usd_per_uah
    print(f'Your choice is {user_currency_choice} and it will be cost {user_usd_cost} UAH for you')
elif user_currency_choice == 'EUR':
    user_eur_amount = float(input('Write here how much EUR do you want to get: '))
    user_eur_cost = user_eur_amount * eur_per_uah
    print(f'Your choice is {user_currency_choice} and it will be cost {user_eur_cost} UAH for you')
else:
    print('Please choose one of these currencies and try again: USD or EUR')
