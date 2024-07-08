"""
7 8 9  
7 8 9  

"""

rows = int(input('Enter rows : '))
columns = int(input('Enter columns : '))
start_number = int(input('Enter start_number : '))
for  i in range(1,rows+1):
    for j in range(start_number,columns+start_number):
        print(j,end=" ")
    print(" ")
