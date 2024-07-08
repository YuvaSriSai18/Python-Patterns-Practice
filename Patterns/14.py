
"""
* * * * *  
 * * * * 
  * * * 
   * * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

"""


n = int(input('Enter n : '))
for i in reversed(range(1,n+1)):
    if i == n :
        for j in range(1,n+1):
            print("* ",end="")
        print(" ")
    else:
        space = n - i 
        print(" " * space + "* " * i)
        
for i in range(1,n+1):
    if i == n :
        for j in range(1,n+1):
            print("* ",end="")
        print(" ")
    else:
        if i != 1 :
            space = n - i 
            print(" " * space + "* " * i)