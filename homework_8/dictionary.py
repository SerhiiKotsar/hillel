"""
Задача 1: Є система, де є списки користувачів.
roles = { 'admin' : [...], 'maintainer' : [...], 'manager' : [...], 'developer': [...]}
В цих списках треба понаписувати імена користувачів.
При введенні імені необхідно перевірити, до якої ролі належить ця людина та вивести повідомлення виду: "Hello, <role>"
Якщо імені немає у списках, вивести: "Hello, Guest"
"""

roles = {'admin': ['Sergey', 'Ethan'], 'manager': ['Anna', 'Helen'], 'developer': ['Sasha', 'Den']}
user_name = input('Print your name here: ').title()

for role, name in roles.items():
    if user_name in name:
        print(f'Hello, {user_name}. You are {role}\n')
        break
else:
    print(f'Hello, {user_name}. You are a guest\n')

"""
Задача 2: 
Є словник : params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
Є стрінга: initial_str = 'https://www.youtube.com/watch?'
Треба написати програму , яка додасть до стінги всі елементи словника, результат має бути такий:
result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
"""

params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'
result_link = initial_str

for key, value in params.items():
    result_link += f'{key}={value}&'

result_link = result_link.rstrip('&')

print(f'Your result link is : {result_link}\n')

"""
Задача 3: 
Взяти Ваш результат:
result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'

Та вивести сільки разів кожен елемент повторюється в стрінг (результатом роботи скріпта має бути словник, 
де ключ - це елемент стрінги, а значення - кількість повторень)
Наприклад:
{'h': 2, 't': 7, 'p': 1} ........
"""

char_count = {}

for char in result_link:
    if char not in char_count:
        char_count[char] = result_link.count(char)

for char, count in char_count.items():
    print(f'Symbol "{char}" meets {count} time(s) in string: {result_link}')
