n = int(input('Enter n : '))
L = []
for i in range(n):
    num = int(input())
    L += [num]
new_list =[]
for j in L:
    if j % 5 == 0:
        new_list += [j]
print(f'Numbers that divisible by 5 in the given list are : {new_list}')