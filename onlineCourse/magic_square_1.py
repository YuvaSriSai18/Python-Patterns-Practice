def magic_square(n):
    magicSquare = []
    for i in range (n):
        l = []
        for i in range (n):
            l.append(0)
        magicSquare.append(l)
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()
c = input("Enter the number : ")
c = int(c)
magic_square(c)           