Temperature = str(input('Enter Temperature : '))
character = Temperature[len(Temperature) - 1]
Temperature = Temperature[:-1]
temp = float(Temperature)
if character == 'C' or character == 'c' :
    print(f'Temperature in Kelvin is {273+temp} K')
    print(f'Temperature in Fahrenheit is {round((((9 * temp) / 5) + 32),2)} F')
elif character == 'F' or character == 'f' :
    print(f'Temperature in Kelvin is {273+round((((temp - 32) * 5)/9),2)} K')
    print(f'Temperature in Celsius is {round((((temp - 32) * 5)/9),2)} C')
elif character == 'K' or character == 'k':
    print(f'Temperature in Celsius : {temp + 273} C')
    print(f'Temperature in Fahrenheit : {round(((((temp - 273)*9)/5) + 32),2)} F')