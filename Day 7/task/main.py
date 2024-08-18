import random
from colorama import Fore
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"You have " + Fore.GREEN + f"{lives}" + Fore.RESET + " lives remaining")
    guess = input("Guess a letter: ").lower()

    display = ""
    if guess in correct_letters:
        print(f"you've already guessed: " + Fore.GREEN + f"{guess}" + Fore.RESET)

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        if lives == 0:
            game_over = True

            print(f"The word was " + Fore.GREEN + f"{chosen_word}" + Fore.RESET + "\n You lose!")

    if "_" not in display:
        game_over = True
        print(f"You win!!\n You correctly guessed: " + Fore.GREEN + f"{chosen_word}" + Fore.RESET + "\n Well done!")

    print(stages[lives])