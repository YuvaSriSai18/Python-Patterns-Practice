n = int(input())
L = []
if n >= 4:
    for i in range(n):
        num = int(input())
        L = L + [num]
new_list = [L[0],L[1],L[len(L)-2],L[len(L)-1]]
print(new_list)

