def game_on(num1 , num2 , bit1 , bit2):
    
    p1 = int(num1[bit1]) % 3
    p2 = int(num2[bit2]) % 3
    
    if(player_1[p1] == player_2[p2]):
        print("Draw")
    elif(player_1[p1] == "Rock" and player_2[p2] == "Scissor"):
        print("Player 1 wins")
    elif(player_1[p1] == "Rock" and player_2[p2] == "Paper"):
        print("Player 2 wins")
    elif(player_1[p1] == "Paper" and player_2[p2] == "Scissor"):
        print("Plyer 2 wins")
    elif(player_1[p1] == "Paper" and player_2[p2] == "Rock"):
        print("Player 1 wins")
    elif(player_1[p1] == "Scissor" and player_2[p2] == "Rock"):
        print("Player 2 wins")
    elif(player_1[p1] == "Scissor" and player_2[p2] == "Paper"):
        print("Player 1 wins")

player_1 = {0 : 'Rock' , 1 : 'Paper' , 2 : 'Scissor'}
player_2 = {0 : 'Paper' , 1 : 'Rock' , 2 : 'Scissor'}
while(True):
    num1 = input("Player 1 Enter your choice : ")
    num2 = input("Player 2 Enter your choice : ")
    bit1 = int(input("Player 1 ,Enter secret bit position : "))
    bit2 = int(input("Player 2 ,Enter secret bit position : "))

    game_on(num1 , num2 , bit1 , bit2)

    ch = input("Do you want to continue y/n :   ")
    if(ch == 'n'):
        break