
"""
    1 
   1 2 
  1   3 
 1     4 
1 2 3 4 5 

"""


n = int(input('Enter n : '))
    
for i in range(1,n+1):
    row = ""
    spaces = n - i
    hollow = i - 2
    if i == 1 or i == n :
        for j in range(1,i+1):
            row = row + str(j) + " "
        print(" " * spaces + row)
    else:
        row = row + "1 " +  "  " * hollow + str(i) + " "
        print(" " * spaces + row)