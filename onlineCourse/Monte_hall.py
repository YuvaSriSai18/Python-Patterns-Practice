"""import random
doors = [0] * 3
goat_door = [0] * 2
swap = 0    #No of swap wins
dont_swap = 0   #No of dont swap wins
j = 0
while(j < 10):
    x = random.randint(0,2) #xth door will comprise of BMW
    doors[x] = "BMW"
    for i in range(0,3):
        if(i == x):
            continue
        else:
            doors[i] = "Goat"
            goat_door.append(i)
    choice = int(input("Enter your choice : "))
    door_open = random.choice(goat_door)    #open a door that comprises of a goat
    while(door_open == choice): #door open shouldn't be equal to the choice of the participant
        door_open = random.choice(goat_door)
    ch = input("Do you want to swap ? y/n : ")
    if(ch == 'y'):
        if(doors[choice] == 'Goat'):
            print("Player wins")
            swap = swap + 1
        else:
            print("Player Lost")
    else:
        if(doors[choice] == 'Goat'):
            print("Player lost")
        else:
            print("Player wins")
            dont_swap = dont_swap + 1
    j = j + 1
print(swap)
print(dont_swap)"""

import random

swap = 0  # Number of swap wins
dont_swap = 0  # Number of don't swap wins

for j in range(10):
    # Initialize the doors for each iteration
    doors = ["Goat"] * 3

    # Randomly select one door to have a BMW
    x = random.randint(0, 2)
    doors[x] = "BMW"

    # Player chooses a door
    choice = int(input("Enter your choice (0, 1, or 2): "))

    # Monty Hall opens a door with a goat
    goat_door = [i for i in range(3) if i != choice and doors[i] == "Goat"]
    door_open = random.choice(goat_door)

    print(f"The door {door_open} has a goat behind it.")

    # Ask if the player wants to swap
    ch = input("Do you want to swap? (y/n): ")
    if ch.lower() == 'y':
        choice = [i for i in range(3) if i != choice and i != door_open][0]

    if doors[choice] == 'BMW':
        print("Player wins")
        swap += 1
    else:
        print("Player lost")

print("Swap wins:", swap)
print("Don't swap wins:", 10 - swap)
