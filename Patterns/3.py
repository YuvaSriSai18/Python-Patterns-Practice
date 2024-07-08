"""

1     0     1     0     1     
0     1     0     1     0      
1     0     1     0     1     
0     1     0     1     0      
1     0     1     0     1


"""


n = int(input('Enter n : '))

for i in range(n):
    if(i % 2 == 0):
        for j in range(n):
            if(j % 2 == 0):
                print("1    ",end=" ")
            else:
                print("0    ",end=" ")
        print(" ")
    else:
        for j in range(n):
            if (j % 2 != 0):
                print("1    ",end=" ")
            else:
                print("0    ",end=" ")
        print(" ")