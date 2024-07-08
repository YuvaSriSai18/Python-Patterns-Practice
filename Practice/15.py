n = int(input('Enter n : '))
sum = float(input('Enter sum : '))
final_sum = 0.0
for i in range(n):
    number = float(input(f'Enter {i+1} : '))
    final_sum += number
if round(final_sum,3) == sum:
    print("True")
else:
    print("False")
