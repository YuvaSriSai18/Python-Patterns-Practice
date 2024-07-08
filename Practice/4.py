import math
def Roots_Nature(discriminant):
    if(discriminant > 0):
        return 'Real and Unequal'
    elif(discriminant < 0):
        return 'Imaginary and Unequal'
    elif(discriminant == 0):
        return 'Real and Equal'
def plus_root(a,b,c):
    D = math.sqrt(((b**2) - (4 * a * c)))
    root_1 = ( -b + D ) / (a * 2)
    return int(root_1)
def minus_root(a,b,c):
    D = math.sqrt(((b**2) - (4 * a * c)))
    root_2 = ( -b - D ) / (a * 2)
    return int(root_2)


a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))
D = math.sqrt(((b**2) - (4 * a * c)))
root_nature = Roots_Nature(D)
root_1 = plus_root(a,b,c)
root_2 = minus_root(a,b,c)

print(f'Roots of the given Equation {a}x^2 + {b}x + {c} are {root_1} and {root_2} . The Nature of the roots is {root_nature}')

