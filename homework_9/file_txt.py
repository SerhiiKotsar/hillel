# 1. Вам потрібно створити текстовий файл(.txt) з текстом і написати програму, яка зкопіює дані з вашого файлу в інший текстовий файл

my_str = """
Some information for testing work with txt-files.
Another line with some words here!
"""

with open('first.txt', 'w') as first_file:
    first_file.write(my_str)

with open('first.txt', 'r') as first_file:
    data = first_file.read()

with open('second.txt', 'w') as second_file:
    second_file.write(data)
