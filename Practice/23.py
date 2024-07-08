def list_sum(list_a):
    list_a = list_a.split() 
    sum = 0 
    for i in list_a:
        sum += int(i)
    print(f'The sum of Numbers in list given is {sum}')

def divisible_by_3(list_a):
    list_b =[] 
    for i in list_a:
        if int(i) % 3 == 0 :
            list_b += [int(i)]
    print(f'Numbers that divisible by 3 in List_a are : {list_b}')

def list_small(list_1):
    for i in range(len(list_1)):
        list_1[i] = int(list_1[i])
    small_num = list_1[0]
    for j in range(len(list_1)):
        if small_num > list_1[j] :
            small_num = list_1[j] 
    return small_num


# Input a string of space-separated numbers
list_1 = input().split()
print(list_small(list_1))

