import random

def choose():
    # You should implement this function to choose a word from a dictionary.
    # For now, let's assume you have a list of words and choose one randomly.
    word_list = ["rainbow", "computer", "science", "programming", "mathematics","player","condition","reverse","water","board"]
    return random.choice(word_list)

def jumble(word):
    # You should implement this function to jumble the letters of the word.
    # For now, let's just shuffle the letters randomly.
    jumbled_word = ''.join(random.sample(word, len(word)))
    return jumbled_word

def thank(player1, player2, pp1, pp2):
    print("Game over!")
    print(f"Thank you {player1} and {player2} for playing.")
    print(f"Final scores:")
    print(f"{player1}: {pp1} points")
    print(f"{player2}: {pp2} points")

def play():
    print("Hello world")

    player1 = input("Player1, Enter your name: ")
    player2 = input("Player2, Enter your name: ")
    pp1 = 0
    pp2 = 0
    turn = 0

    while True:
        picked_word = choose()
        qn = jumble(picked_word)
        print("Jumbled word:", qn)

        if turn % 2 == 0:
            print(player1, "your turn")
        else:
            print(player2, "your turn")

        ans = input("Guess the word: ")


        if ans == picked_word:
            if turn % 2 == 0:
                pp1 += 1
                print(f"Your score is {pp1}")
            else:
                pp2 += 1
                print(f"Your score is {pp2}")
        else:
            print("Better luck next time. I thought:", picked_word)

        c = int(input("Press 1 to continue or 0 to exit: "))
        if c == 0:
            thank(player1, player2, pp1, pp2)
            break

        turn += 1

play()
#conda create -c conda-forge -n spyder-env spyder numpy scipy pandas matplotlib sympy cython
