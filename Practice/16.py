n = float(input('Enter n : '))
power = int(input('Enter power : '))
sum = 0
for i in range(1,power+1):
    sum = sum + pow(n,i)
print(round(sum,4))