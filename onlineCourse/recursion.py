def fact(n):
    if(n == 0):
        return 1 
    else:
        return n * fact(n-1)

num = int(input("Enter number to find it's factorial  : "))
print( 'Factorial of ', num , ' is ', fact(num))

