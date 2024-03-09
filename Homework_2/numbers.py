# 1. Порахувати площу прямокутного трикутника Формула: 1/2*k1*k2, де k1,k2 – катети.
first_side = 4
second_side = 6
triangle_square = 0.5 * first_side * second_side
print(f'The area of a right triangle: {triangle_square}')


# 2. n школярів ділять k яблук порівну, залишок, що не ділиться, залишається в кошику.
# Скільки яблук дістанеться кожному школяру? Скільки яблук залишиться у кошику? Вивести 2 числа

children_amount = 3
apple_amount = 2

apples_per_student = apple_amount // children_amount  # Количество яблок каждому школьнику
remaining_apples_in_basket = apple_amount % children_amount  # Остаток яблок в корзине

print(f'The number of apples for each student: {apples_per_student}')
print(f'The rest of the apples in the basket: {remaining_apples_in_basket}')


# 3. Написати програму, яка виводить попереднє та наступне число від заданого
# Наприклад: задане число 567, наступне буде 568, попереднє 565

current_number = 567
previous_number = current_number - 1
next_number = current_number + 1

print(f'A number is set: {current_number}')
print(f'Previous number: {previous_number}')
print(f'Next number: {next_number}')
