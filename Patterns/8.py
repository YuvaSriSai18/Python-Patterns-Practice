
"""
1 2 3 4 5 
1     4 
1   3 
1 2 
1 
"""

n = int(input('Enter n : '))
for i in range(1,n+1):
    count = n-(i-1)
    hollow_spaces=(n-i)-1
    row=""
    if(i>1 and i<n):
        row=row+"1 "+"  "*hollow_spaces+str(count)+" "
        print(row)
    else:
        for j in range(1,(n-i+1)+1):
            row = row+str(j)+" "
        print(row)