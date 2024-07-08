n = int(input('Enter n : '))

for i in range(65,65+n):
    row = ""
    spaces = (65 + n) - (i + 1)
    hollow = i - 65 
    if i == 65:
        row = row + chr(i)
        print(" " * spaces + row)
    else:
        row = row + chr(i) + "  " * hollow + chr(i)
        print(" " * spaces + row)

for i in reversed(range(65,(65+n)-1)):
    row = ""
    spaces = (65 + n) - (i + 1)
    hollow = i - 65 
    if i == 65:
        row = row + chr(i)
        print(" " * spaces + row)
    else:
        row = row + chr(i) + "  " * hollow + chr(i)
        print(" " * spaces + row)