import random
from PIL import Image
end = 100 
def show_board():
    img = Image.open('snake and Ladders.webp')
    img.show()

def check_ladder(points):
    if(points == 1):
        print('ladder')
        return 38
    elif(points == 4):
        print('ladder')
        return 14
    elif(points == 8):
        print('ladder')
        return 30
    elif(points == 21):
        print('ladder')
        return 42
    elif(points == 28):
        print('ladder')
        return 74
    elif(points == 50):
        print('ladder')
        return 67
    elif(points == 71):
        print('ladder')
        return 92
    elif(points == 80):
        print('ladder')
        return 99
    else:
        return points
def check_snake(points):
    if(points == 32):
        print('Snake')
        return 10
    elif(points == 36):
        print('Snake')
        return 6
    elif(points == 48):
        print('Snake')
        return 26
    elif(points == 62):
        print('Snake')
        return 18
    elif(points == 88):
        print('Snake')
        return 24
    elif(points == 95):
        print('Snake')
        return 56
    elif(points == 97):
        print('Snake')
        return 78
    else:
        return points
def reached_end(points):
    if(points == end):
        return True
    else:
        return False
    
def play():
    p1_name = input('Player 1 , Please enter your name : ')
    p2_name = input('Player 2 , Please enter your name : ')
    #initial points for player1
    pp1 = 0
    #initial points for player1
    pp2 = 0

    turn = 0 

    while(True):
        if(turn % 2 == 0):
            #player 1 turn 
            print(p1_name , ' your turn ')
            #k player 's choice to continue
            c = input('Press 1 to continue  , 0 to Quit : ')
            if(c == 0):
                print(p1_name , ' scored ' , pp1)
                print(p2_name,' scored ',pp2)
                print('Quitting the game , Thanks for playing')
            #generate a random number for (1,6)

            dice = random.randint(1,6)
            print('Dice showed : ',dice)
            pp1 = pp1 + dice

            pp1 = check_ladder(pp1)

            pp1 = check_snake(pp1)

            #check if the player goes beyond the board

            if(pp1 > end):
                pp1 = end
            print(p1_name , ' Your score :  ',pp1)
            if(reached_end(pp1)):
                print(p1_name,' won')
                break
        else:
            #player 1 turn 
            print(p2_name , ' your turn ')
            #k player 's choice to continue
            c = input('Press 1 to continue  , 0 to Quit : ')
            if(c == 0):
                print(p1_name , ' scored ' , pp1)
                print(p2_name,' scored ',pp2)
                print('Quitting the game , Thanks for playing')
            #generate a random number for (1,6)

            dice = random.randint(1,6)
            print('Dice showed : ',dice)
            pp2 = pp2 + dice

            pp2 = check_ladder(pp2)

            pp2 = check_snake(pp2)

            #check if the player goes beyond the board

            if(pp2 > end):
                pp2 = end
            print(p1_name , ' Your score :  ',pp1)
            if(reached_end(pp1)):
                print(p2_name,' won')
                break
        turn = turn + 1
show_board()
play() 
