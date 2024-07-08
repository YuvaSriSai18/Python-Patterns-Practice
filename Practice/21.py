S = str(input())
L = [] 
unicode_1 = []
for i in range(len(S)):
    L += [S[i]]
for i in L:
    if i == " ":
        continue
    unicode_1 += [ord(i)]
for j in unicode_1:
    print(chr(j-1))