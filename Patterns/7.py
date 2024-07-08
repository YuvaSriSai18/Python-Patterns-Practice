
"""    
    1 
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5 

"""


# n = 7

# rows = int(input('Enter rows : '))
# cols = (rows * 2) - 1

# for i in range(1,rows+1):
#     for j in range(1,cols+1):
#         if(i == 1 and j == rows):
#             print(n)
        
#     print(" ")

s = int(input('Enter starting number : '))
n = int(input('Enter n : '))
for row in range(1, n + 1):
    left_spaces = " " * (n - row)
    each_row = ""
    for column in range(s, row + s):
        each_row = each_row + str(column) + " "
    each_row = left_spaces + each_row   
    print(each_row)