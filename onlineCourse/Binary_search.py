def binary_search(arr, x):
    first_pos = 0
    last_pos = len(arr) - 1
    flag = 0  # Flag means that the element has not been found yet
    count = 0

    while first_pos <= last_pos and flag == 0:
        count = count + 1
        mid = (first_pos + last_pos) // 2
        if x == arr[mid]:
            flag = 1
            print("The element is present at pos", str(mid))
            #print("The number of iterations are", str(count))
            return
        else:
            if x < arr[mid]:
                last_pos = mid - 1
            else:
                first_pos = mid + 1
    print("The number is not present")

# Populate the sorted list
arr = []
for i in range(1, 21):
    arr.append(i)
x = int(input("Enter element to search : "))
# Call binary_search to find the element
binary_search(arr, x)
