"""
3. У вас є словник
course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}
Юзер вводить з консолі ключ, за яким треба отримати значення.
Написати програму, яка імплементує дану задачу з використанням блоку try/except (Треба обробити помилку якщо ключа не існує).
"""
course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}
user_key = input('Write a key from a dictionary: ').lower()

try:
    print(f'The value key \'{user_key}\' is: {course[user_key]}')
except KeyError:
    print(f'There is no key \'{user_key}\' in a dictionary')
