#I created a library with words and made the program randomly choose a word for each game of the game,
#and I also added some time.sleep to make the game look like it was loading

#library
import random 
import time

#variable to calculate how many attempts the user had
tentativas = 1

#random list
random_list = ('basquete', 'chiclete', 'chuveiro', 'oftalmologista', 'reportagem', 'temperatura', 'amendoim', 'cachorro', 'elefante', 'limonada')
random_word = random.choice(random_list)

#first hint
list_random_word = list(random_word)
initial_hint = "_" * len(list_random_word)
len_random_word = len(list_random_word)

#start
print('\nWelcome to the Word Game: \n')
time.sleep(2)

#initial hint
print("Your hint is:", initial_hint)

#the enter of the user
guess = input('What is your guess? ')

while guess.lower() != random_word:
    while len(guess) != len(random_word):
        print('Sorry, the guess must have the same number of letters as the secret word.')
        print("Your hint is:", initial_hint)
        guess = input('What is your guess? ')
        tentativas = tentativas + 1

    count = 0

    for i in range(len_random_word):
        letter_guess = guess[i]
        letter_word = list_random_word[i]
        lower_guess = letter_guess.lower()
        lower_word = letter_word.lower()

        if lower_guess == lower_word:
            if count == 0:
                print(f"Your hint is: {lower_guess.capitalize()}", end="")
                count = 1
            else:
                print(f" {lower_guess.capitalize()}", end="")
        elif lower_guess in list_random_word:
            if count == 0:
                print(f"Your hint is: {lower_guess.lower()}", end="")
                count = 1
            else:
                print(f" {lower_guess.lower()}", end="")
        else:
            if count == 0:
                print("Your hint is: _", end="")
                count = 1
            else:
                print("_", end="")

    print()
    guess = input('\nWhat is your guess? ')
    tentativas += 1

print(f"Congratulations! You guessed it!\nIt took you {tentativas} guesses.")