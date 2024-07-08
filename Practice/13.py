# import math

# m = int(input('Enter m: '))
# n = int(input('Enter n: '))

# def isPrime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True

# primes = []
# for i in range(m, n + 1):  # Corrected the range
#     if isPrime(i):
#         primes.append(i)
# print(primes)

import math

m = int(input('Enter m: '))
n = int(input('Enter n: '))

primes = []
for num in range(m, n + 1):
    if num <= 1:
        continue
    if num == 2:
        primes.append(num)
        continue
    if num % 2 == 0:
        continue
    is_prime = True
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print(primes)
   