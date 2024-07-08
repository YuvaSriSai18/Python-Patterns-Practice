def bubble_sort(a):
    n = len(a)

    for i in range(n):
        for j in range(0, n-i-1):
            if( a[j] > a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp

def search(a, x):
    found = False  # Initialize a variable to track whether x is found in the list

    # Check if x is in the list
    for i in a:
        if(i == x):
            found = True
            break  # Exit the loop once x is found

    if found:
        print(x, "is found")
    else:
        print(x, "is not found")

# Input: Ask the user for a list of numbers separated by spaces
input_str = input("Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of integers
a = [int(x) for x in input_str.split()]

# Ask the user for the number to search
search_num = int(input("Enter a number to search: "))

# Call the bubble_sort function to sort the list
bubble_sort(a)

# Call the search function to search for the number
search(a, search_num)
