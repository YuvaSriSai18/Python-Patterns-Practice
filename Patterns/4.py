"""
1   
0  1   
1  0  1   
0  1  0  1   
1  0  1  0  1 

"""

n = int(input("Enter n : "))

for i in range(1,n+1):
    if(i % 2 == 1):
        for j in range(1,i+1):
            if(j % 2 == 1):
                print("1 ",end=" ")
            else:
                print("0 ",end=" ")
        print(" ")
    else:
        for j in range(1,i+1):
            if(j % 2 == 0):
                print("1 ",end=" ")
            else:
                print("0 ",end=" ")
        print(" ")

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if((i+j) % 2 == 0):
#             print("1 ",end=" ")
#         else:
#             print("0 ",end=" ")
#     print(" ")