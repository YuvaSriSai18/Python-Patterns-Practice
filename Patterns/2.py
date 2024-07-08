
"""

*     *     *     *      
*     *     *      
*     *      
*     

"""


n = int(input("Enter n : "))
temp = n
for i in range(1,n+1):
    for j in range(1,temp+1):
        print("*    ",end=" ")
    temp = temp - 1
    print(" ")