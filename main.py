# Make sure hangman_art.py and hangman_words.py are in the same directory with this

import random
import hangman_words
import hangman_art

lives = 6

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
list_of_entered_letters = []
while not game_over:

    print(f"You have {lives} lives left")
    print("****************************<???>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""
    if guess in list_of_entered_letters:
        print("You already guessed this letter")
    else:
        list_of_entered_letters.append(guess)
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
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"The correct word was [chosen_word]")
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
