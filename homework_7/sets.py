"""
Задача 1: Дані списки:
first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
Потрібно повернути список, що складається з унікальних елементів, спільних для цих двох списків.
"""

first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

uniq_set = set(first_list).intersection(set(second_list))
uniq_list = list(uniq_set)
print(f'Unique list looks like: {uniq_list}\n')

# Задача 2: У вас є 2 списка, напишіть програму, яка виводить усі елементи першого, яких немає у другому.

third_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
fourth_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

third_set = set(third_list)
fourth_set = set(fourth_list)
differ_set = third_set.difference(fourth_set)
differ_list = list(differ_set)
print(f'The first list without the elements of the second: {differ_list}\n')

"""
Задача 3: Написати програму, яка на вхід приймає список чисел 
і перевіряє, чи всі числа в цій послідовності є унікальними
"""

numbers_str = input('Type your numbers here: ')
numbers_list = list(map(int, numbers_str.split()))  # convert a list of strings to a list of numbers
count_list = len(numbers_list)
numbers_set = set(numbers_list)
count_set = len(numbers_set)

if count_list == count_set:
    print(f'Numbers in the list: {numbers_list} are unique\n')
else:
    print(f'Numbers in the list: {numbers_list} are not unique\n')

"""
Задача 4: Написати програму, яка знайде мінімальне значення у списку.
Список задати у самій програмі у вигляді: elements = [1, 5, 68, 0]
У ньому може бути скільки завгодно елементів
min() - заборонено для використання
"""

elements_first = [1, 0, -1]
min_value = elements_first[0]

for num in elements_first:
    if num < min_value:
        min_value = num

print(f'Min value is: {min_value}\n')

"""
Задача 5. Написати програму, яка порахує суму всіх елементів у списку
Список задати у самій програмі у вигляді: elements  = [1, 5, 68, 0]
У ньому може бути скільки завгодно елементів
sum() - заборонено для використання
"""

elements_second = [1, 5, 15, 0, -1]
total = 0

for num in elements_second:
    total += num

print(f'Total sum is: {total}\n')
