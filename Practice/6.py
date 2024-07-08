def series(N):
    sum = 0
    for i in range(1,N+1):
        sum += ( 1 / i ) 
    return sum
n = int(input('Enter n : '))
print(series(n))