import random


def play():
    wordlist = ['python', 'java', 'kotlin', 'javascript']
    chosen_word = (random.choice(wordlist))
    masked_word = ("-" * len(chosen_word))
    number_guesses = 8
    already_guessed = []
    while number_guesses > 0:
        guess_letter = input(f'\n{masked_word}\nInput a letter: ')
        if len(guess_letter) > 1:
            print('You should input a single letter')
        elif guess_letter.isupper() or not guess_letter.isalpha():
            print('It is not an ASCII lowercase letter')
        elif guess_letter in chosen_word:
            index = chosen_word.find(guess_letter)
            index2 = chosen_word.rfind(guess_letter)
            masked_word = masked_word[:index] + guess_letter + masked_word[index + 1:]
            masked_word = masked_word[:index2] + guess_letter + masked_word[index2 + 1:]
            if guess_letter not in set(already_guessed):
                already_guessed.append(guess_letter)
            elif guess_letter in set(already_guessed):
                print("You already typed this letter")
        elif guess_letter not in chosen_word:
            if guess_letter in set(already_guessed):
                print("You already typed this letter")
            elif guess_letter not in set(already_guessed):
                print("No such letter in the word")
                already_guessed.append(guess_letter)
                number_guesses -= 1
        elif masked_word == chosen_word:
            print(masked_word)
            print('You guessed the word!\nYou survived!')
        if number_guesses == 0:
            print('You lost!')


while True:
    option = input('H A N G M A N\nType "play" to play the game, "exit" to quit: ')
    if option == 'play':
        play()
        break
    elif option == 'exit':
        break
    else:
        continue
