
"""
1 2 3 4 5 
 1     4
  1   3
   1 2
    1


"""

n = int(input('Enter n : '))

for i in reversed(range(1,n+1)):
    row = "" 
    spaces = n - i 
    hollow = i - 2
    if i == n :
        for j in range(1,n+1):
            row = row + str(j) + " "
        print(row)
    elif i  == 1:
        row = row + str(i) 
        print(" " * spaces + row) 
    else:
        row = row + "1 " + "  " * hollow + str(i) 
        print(" " * spaces + row)