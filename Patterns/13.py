"""
5 5 5 5 5  
  4 4 4 4 
    3 3 3 
      2 2 
        1

"""



n = int(input('Enter n : '))
for i in reversed(range(1,n+1)):
    if i == n :
        for j in range(1,n+1):
            print(str(i)+" ",end="")
        print(" ")
    else:
        space = n - i 
        print("  " * space +  (str(i) + " ") * i)