
"""
7 6 5 4 3 2 1 
7           1 
7           1 
7           1 
7           1 
7           1 
7 6 5 4 3 2 1 

"""


n = int(input('Enter n : '))

for i in range(1,n+1):
    row = ""
    if i == 1 or i == n :
        for j in reversed(range(1,n+1)):
            row = row + str(j) + " "
            
        print(row)
    else:
        for j in reversed(range(1,n+1)):
            if j == n:
                row = row + str(n) 
            elif j == 1 :
                row = row + " 1 "
            else:
                row = row + "  " 
        print(row)
