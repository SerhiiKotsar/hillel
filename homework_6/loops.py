"""
Задача 1.Напишіть програму, яка виведе всі числа зі списку, які поділяються на задане число
Число задавати з клавіатури
"""
first_list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
divide_list_of_numbers = []
users_number = int(input('Print your number here: '))

for number_first in first_list_of_numbers:
    if number_first % users_number == 0:
        divide_list_of_numbers.append(number_first)

print(f'{users_number} is divisible by a list: {divide_list_of_numbers} without a remainder')

"""
Задача 2.Написати програму, яка знайде перше непослідовне число у списку
Список задати у самій програмі у вигляді: list = [1, 5, 68, 0]
У ньому може бути скільки завгодно елементів
Наприклад, дано список [1,2,3,4,6,7,8]
Відповіддю буде число 6. Якщо список послідовний, вивести відповідне повідомлення
"""
second_list_of_numbers = [1, 2, 3, 4, 5, 6, 8]

for index in range(1, len(second_list_of_numbers)):
    if second_list_of_numbers[index] != second_list_of_numbers[index-1] + 1:
        print(f'\nNon-consecutive number in the list: {second_list_of_numbers[index]}\n')
        break
else:
    print('\nThe list contains consecutive numbers!\n')

"""
Задача 3.Написати цикл, який виведе
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

for line in range(1, 6):
    for number_third in range(1, line + 1):
        print(number_third, end=' ')
    print()
