m = int(input('Enter starting number : '))
n = int(input('Enter ending number : '))
count = 0 
sum = 0 
for i in range(m,n+1):
    sum = sum + i 
    count += 1

print(f'Average is {sum/count}')