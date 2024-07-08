def sum_of_odd(n):
    sum = 0
    for i in range(1,n):
        if(i % 2 != 0):
            sum += i
    return sum
n = int(input('Enter n : '))
print(f'The sum of odd numbers between 1 and {n} is {sum_of_odd(n)}')