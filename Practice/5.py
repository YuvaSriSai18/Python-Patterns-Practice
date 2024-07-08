def check_triangle(a,b,c):
    if((a+b+c > 180)):
        return 'It is not a triangle'
    else:
        return 'It is a triangle'
a = int(input('Enter A : '))
b = int(input('Enter B : '))
c = int(input('Enter C : '))
print(check_triangle(a,b,c))