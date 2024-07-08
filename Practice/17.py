T = str(input('Enter Time : '))
character = T[len(T) - 1]
T = T[:-1]

if character == 'M' or character == 'm' :
    number = int(T)
    number = number / 60
    print(f'Time in Hours is {round(number,2)}H')
elif character == 'S' or character == 's' :
    number = int(T)
    number = number / 3600
    print(f'Time in Hours is {round(number,2)}H')
else:
    print("Can't be determined")