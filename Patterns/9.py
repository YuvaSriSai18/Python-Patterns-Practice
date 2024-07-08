"""
1 
1 2 
1   3 
1     4 
1 2 3 4 5
"""
n = int(input('Enter n : '))
for i in range(1,n+1):
    if i == 1 or i == 2 or i == n:
        for j in range(1,i+1):
            print(j,end=" ")
        print("")
    else:
        hollow_spaces = int(i - 2)
        print("1 " + "  " * hollow_spaces + str(i) + " ")