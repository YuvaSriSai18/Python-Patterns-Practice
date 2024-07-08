def Max_Number(*args):
    max = 0 
    for i in args:
        if(i > max):
            max = i 
    return max

N = int(input('Enter number of arguments to be passed: '))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(N)]

max_number = Max_Number(*numbers)
print(f'Maximum Number among the given numbers is {max_number}')