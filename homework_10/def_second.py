'''
2. Напишіть функцію is_prime, яка приймає 1 аргумент - число від 2 до 1000, і повертає True, якщо це просте число, і False в іншому випадку.
P.S просте число це те, що ділиться без залишку тільки на 1 і на самого себе

Приклад простих чисел: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
Приклад непростих чисел: 4, 6, 8, 9, 10, 12, 15, 21, 25
'''


def is_prime(*, number: int) -> bool:
    if number not in range(2, 1001):
        raise ValueError(f'{number} is not a valid number. Please, try any number in range from 2 to 1000.')
    for element in range(2, int(number ** 0.5) + 1):
        if number % element == 0:
            return False
    return True


print(is_prime(number=3))
