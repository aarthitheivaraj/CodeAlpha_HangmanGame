"""
CodeAlpha - Python Programming Internship
Task 1: Hangman Game
"""

import random

WORDS = ["python", "hangman", "coding", "internship", "developer"]
MAX_ATTEMPTS = 6


def choose_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"You have {MAX_ATTEMPTS} incorrect guesses allowed.\n")

    while wrong_guesses < MAX_ATTEMPTS:
        print(display_word(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_ATTEMPTS}")

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                return
        else:
            wrong_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.\n")

    print(f"Game over! You've used all {MAX_ATTEMPTS} incorrect guesses.")
    print(f"The word was: {word}")


def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing!")
            break
        print()


if __name__ == "__main__":
    main()