a = int(input('Enter n : '))
for i in range(0,a):
    stars="* "*(a-i)
    hollow_spaces=2*i 
    if(i==0):
        print(stars+stars)
    else:
        print(stars+"  "*hollow_spaces+stars)
for i in reversed(range(0,a)):
    stars="* "*(a-i)
    hollow_spaces=2*i 
    if(i==0):
        print(stars+stars)
    else:
        print(stars+"  "*hollow_spaces+stars)
    