
"""
   1 
  1 2 
 1 2 3 
1 2 3 4 

"""    
n = int(input('Enter n : '))

for i in range(1, n+1):
    row = ""
    spaces = n - i
    row = " " * spaces
    for j in range(1, i+1):
        row += str(j) + " "
    print(row.rstrip())  # Use rstrip() to remove the trailing space on each line
