from def_temperature import convert_temperature

number_value = int(input('Enter temperature value: '))
unit_value = input('Select unit of measurement (C/F): ')
print(convert_temperature(temp_value=number_value, unit=unit_value))
