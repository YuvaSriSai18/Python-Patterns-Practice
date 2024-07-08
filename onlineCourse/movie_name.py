
import random

movies = ['vikram', 'jailer', 'ustaad', 'love you ram', 'oo saathiya', 'lust stories', 'narayana & co.', 'ugram',
          'custody', 'rangabali', 'dj tillu', 'simhadri', 'rrr', 'vakkel saab']

def create_question(movie):
    n = len(movie)
    letters = list(movie)
    temp = []
    for i in range(n):
        if letters[i] == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn = ''.join(temp)
    return qn

def is_present(letter, movie):
    c = movie.count(letter)
    if c == 0:
        return False
    else:
        return True

def unlock(qn, movie, letter):
    ref = list(movie)
    qn_list = list(qn)
    temp = []
    n = len(movie)
    for i in range(n):
        if ref[i] == ' ' or ref[i] == letter:
            temp.append(ref[i])
        else:
            if qn_list[i] == '*':
                temp.append('*')
            else:
                temp.append(ref[i])
    new_qn = ''.join(temp)
    return new_qn

def play():
    player_1_name = input('Player 1! Enter your name: ')
    player_2_name = input('Player 2! Enter your name: ')
    pp1 = 0
    pp2 = 0  # Points of respective players
    turn = 0
    
    while True:
        if turn % 2 == 0:
            # player1
            print(player_1_name, "Your turn")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn

            not_said = True
            while not_said:
                letter = input('Your letter: ')
                if is_present(letter, picked_movie):
                    # unlock
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print(modified_qn)
                    d = input('Press 1 to guess the movie or 2 to unlock another letter ')
                    if d == '1':
                        ans = input('Your answer: ')
                        if ans == picked_movie:
                            pp1 += 1
                            print('Correct')
                            not_said = False
                            print(player_1_name, 'your score is', pp1)
                        else:
                            print('Wrong answer. Try again.')
                else:
                    print(letter, "not found!!")
            c = int(input('Press 1 to continue or 0 to quit '))
            if c == 0:
                print(player_1_name, 'score is', pp1)
                print(player_2_name, 'score is', pp2)
                print("Thanks for playing! Have a nice day.")
        else:
            # player2
            print(player_2_name, "Your turn")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn

            not_said = True
            while not_said:
                letter = input('Your letter: ')
                if is_present(letter, picked_movie):
                    # unlock
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print(modified_qn)
                    d = input('Press 1 to guess the movie or 2 to unlock another letter ')
                    if d == '1':
                        ans = input('Your answer: ')
                        if ans == picked_movie:
                            pp2 += 1
                            print('Correct')
                            not_said = False
                            print(player_2_name, 'your score is', pp2)
                        else:
                            print('Wrong answer. Try again.')
                else:
                    print(letter, "not found!!")
            c = int(input('Press 1 to continue or 0 to quit '))
            if c == 0:
                print(player_1_name, 'score is', pp1)
                print(player_2_name, 'score is', pp2)
                print("Thanks for playing! Have a nice day.")

        turn += 1

play()


"""
import random
movies = ['vikram' , 'jailer' , 'ustaad' , 'love you ram' , 'oo saathiya' , 'lust stories' , 'narayana & co.' , 'ugram' , 'custody' , 'rangabali' , 'dj tillu' , 'simhadri' , 'rrr' , 'vakkel saab']

def create_question(movie):
    n = len(movie)
    letters = list(movie)
    temp = []
    for i in range(n):
        if(letters[i] == ' '):
            temp.append(' ')
        else:
            temp.append('*')
    qn = ''.join(str(x) for x in temp)
    return qn

def is_present(letter , movie):
    c = movie.count(letter)
    if(c == 0):
        return False
    else:
        return True         



def unlock(qn , movie , letter):
    ref = list(movie)
    qn_list = list(qn)
    temp = []
    n = len(movie)
    for i in range(n):
        if(ref[i] == ' ' or ref[i] == letter):
            temp.append(ref[i])
        else:
            if(qn_list[i] == '*'):
                temp.append('*')
            else:
                temp.append(ref[i])
    new_qn = ''.join(str(x) for x in temp)
    return new_qn

def play():
    player_1_name = input('Player 1 ! Enter your name   ')
    player_2_name = input('Player 2 ! Enter your name   ')
    pp1 = 0 
    pp2 = 0 #Points of respective players
    turn = 0
    #willing = True
    while(True):
        if(turn % 2 == 0):
            #player1
            print(player_1_name , "Your turn ")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn 

            not_said = True
            while(not_said):
                letter = input('Your letter: ')
                if(is_present(letter , picked_movie)):
                    #unlock
                    modified_qn = unlock(modified_qn , picked_movie , letter)
                    print(modified_qn)
                    d = input('Press 1 to guess the movie or 2 to unlock another letter ')
                    if(d == 1):
                        ans = input('Youe answer :  ')
                        if(ans == picked_movie):
                            pp1 = pp1 + 1
                            print('Correct')
                            not_said = False
                            print(player_1_name , 'your score is ',pp1)
                        else:
                            print('Wrong answer . Try again.')
                else:
                    print(letter , "not found !!")
            c = int(input('Press 1 to continue or 0 to quit '))
            if(c == 0):
                print(player_1_name , 'score is ',pp1)
                print(player_2_name , 'score is ',pp2)
                print("Thanks for playing ! Have a nice day. ")
        else:
            #player2
            print(player_1_name , "Your turn ")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn 

            not_said = True
            while(not_said):
                letter = input('Your letter: ')
                if(is_present(letter , picked_movie)):
                    #unlock
                    modified_qn = unlock(modified_qn , picked_movie , letter)
                    print(modified_qn)
                    d = input('Press 1 to guess the movie or 2 to unlock another letter ')
                    if(d == 1):
                        ans = input('Youe answer :  ')
                        if(ans == picked_movie):
                            pp1 = pp1 + 1
                            print('Correct')
                            not_said = False
                            print(player_1_name , 'your score is ',pp1)
                        else:
                            print('Wrong answer . Try again.')
                else:
                    print(letter , "not found !!")
            c = int(input('Press 1 to continue or 0 to quit '))
            if(c == 0):
                print(player_1_name , 'score is ',pp1)
                print(player_2_name , 'score is ',pp2)
                print("Thanks for playing ! Have a nice day. ")
            
            turn = turn + 1

play()          
         """