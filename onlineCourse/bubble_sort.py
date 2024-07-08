def bubble_sort(a):
    n = len(a)

    for i in range(n):
        for j in range(0, n-i-1):
            if(a[j] > a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp

# Input: Ask the user for a list of numbers separated by spaces
input_str = input("Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of integers
a = [int(x) for x in input_str.split()]

# Call the bubble_sort function to sort the list
bubble_sort(a)

# Print the sorted list
for i in a:
    print(i)
