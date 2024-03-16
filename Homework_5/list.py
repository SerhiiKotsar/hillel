# 1. Написати програму, яка перевіряє чи є стрінга паліндромом
palindrome_string_original = input('Write your string here, please: ')  # 'tenet' is a palindrome
palindrome_string_copy = palindrome_string_original[::-1]  # reverse our string

result = palindrome_string_original == palindrome_string_copy

if result:
    print(f'String \'{palindrome_string_original}\' is a palindrome')
else:
    print(f'String \'{palindrome_string_original}\' is not a palindrome')

# 2. Ви маєте список ['Hillel', 'AQA', 'TEST'], переведіть цей список в стрінгу, а потім знову в список
hillel_list = ['Hillel', 'AQA', 'TEST']  # original list of words
hillel_string = ', '.join(hillel_list)  # convert list to string by join() separated by comma and space
hillel_list_again = hillel_string.split(', ')  # convert string to list by split() with comma and space

print(f'\nOriginal list: {hillel_list} become to a string: \'{hillel_string}\'')
print(f'String: \'{hillel_string}\' back to a list is: {hillel_list_again}')

# 3. Ви маєте список ['Tst', 'aBc', 'TEST', 'Hello', 'neW'], відсортуйте його,
# але врахуйте що слова в списку можуть  починатися з великої або малої літери
strings_list = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']  # original list of words
sorted_strings_list = sorted(strings_list, key=str.lower)  # update list of strings to lower case for sorted

print(f'\nOriginal string list is: {strings_list}')
print(f'Sorted string list is: {sorted_strings_list}')

# 4. Ви маєте список [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]], дістаньте з нього значення 'Win'
# та переведіть його у новий список. Результат має бути  ['Win']
win_list = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]
new_win_list = win_list[-1][-1]  # get 'Win' from the list
print(f'\nNew win list: {new_win_list}')

# 5. Створіть будь який список та перевірте чи коректно він відсортований
numbers_list = [3, 1, 4, 1, 5, 9]

is_sorted = numbers_list == sorted(numbers_list)

if is_sorted:
    print(f'\nList {numbers_list} is sorted correct')
else:
    print(f'\nList {numbers_list} is sorted incorrect')
