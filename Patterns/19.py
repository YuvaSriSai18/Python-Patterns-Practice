
"""
    * 
   * * 
  *   * 
 *     * 
* * * * * 

"""

n = int(input('Enter n : '))
    
for i in range(1,n+1):
    row = ""
    spaces = n - i
    hollow = i - 2
    if i == 1 or i == n :
        for j in range(1,i+1):
            row = row + "* " 
        print(" " * spaces + row)
    else:
        row = row + "* " +  "  " * hollow + "* " 
        print(" " * spaces + row)