"""
Задача: Реалізуйте функцію, яка конвертує температуру з градусів Цельсія в градуси Фаренгейта і навпаки.
Функція повинна приймати два аргументи: значення температури і одиницю виміру ('C' або 'F') і повертати перетворене значення.

Фарингейт = (градус Цельсий * 1.8) + 32
"""
FAHRENHEIT_COEFFICIENT = 1.8
CELSIUS_COEFFICIENT = 0.5556


def convert_temperature(*, temp_value: int, unit: str) -> str:
    # From Celsius to Fahrenheit
    if unit.upper() == 'C':
        result_fahrenheit = (temp_value * FAHRENHEIT_COEFFICIENT) + 32
        return f'{temp_value} celsius is equal {result_fahrenheit} fahrenheit'
    # From Fahrenheit to Celsius
    elif unit.upper() == 'F':
        result_celsius = CELSIUS_COEFFICIENT * (temp_value - 32)
        return f'{temp_value} fahrenheit is equal {result_celsius} celsius'
    else:
        raise ValueError(f'\'{unit}\' is not a valid unit. You should choose one of these \'C\' or \'F\'')


number_value = int(input('Enter temperature value: '))
unit_value = input('Select unit of measurement (C/F): ')
print(convert_temperature(temp_value=number_value, unit=unit_value))
