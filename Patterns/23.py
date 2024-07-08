rows = int(input('Enter rows : '))
cols = (2 * rows) - 1
count = 1 
number = 0
for i in range(rows): 
    row = ""
    spaces = rows - count
    count += 1
    hollow = (2 * i) - 1
    if i == 0 : 
        row = row + chr(65)
        print(" " * spaces + row )
    else:
        number += 1
        row = row + chr(number + 65)
        number += 1 
        row = row + " " * hollow + chr(number + 65)
        print(" " * spaces + row )
number = number - 2 
for i in reversed(range(rows - 1)):
    row = ""
    spaces = rows - i 
    hollow = (2 * i ) - 1 
    if i == 0 :
        row = row + chr(65)
        print(" " * spaces + row)
    else:
        row = row + chr(number)
        number -= 1
        row = row + " " * hollow + chr(number)
        number -= 1
        #row = row[::-1] 
        print(" " * spaces + row)
