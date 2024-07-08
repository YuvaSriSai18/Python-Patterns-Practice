
"""
1 2 3 4 5 
2     5
3   5
4 5
5
"""

n = int(input('Enter n : '))
for i in range(1,n+1):
    if i == 1 :
        for j in range(1,n+1):
            print(str(j)+" ",end="")
        print("")
    elif i == n:
        print(n)
    else:
        hollow = (n - i) - 1 
        print(str(i) + "  " * hollow + " 5" + "")