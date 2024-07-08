list_a = input().split(",")
list_b = input().split(",")
len_of_list_a = len(list_a)
n = len_of_list_a - 1 
for i in range(len(list_a)):
    num_1 = list_a[i]
    num_2 = list_b[n]
    n -= 1
    print(str(num_1) +  " " + str(num_2))