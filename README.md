# CodeAlpha - Hangman Game

## Task 1: Hangman Game

### Description

This project is a simple text-based Hangman Game developed using Python as part of the **CodeAlpha Python Programming Internship**.

The game randomly selects a word from a predefined list, and the player has to guess the word one letter at a time. The player is allowed a maximum of **6 incorrect guesses** before the game ends.

---

## Features

* Randomly selects a word from a predefined list.
* Player guesses one letter at a time.
* Maximum of 6 incorrect attempts.
* Displays the current progress of the word.
* Validates user input.
* Prevents duplicate letter guesses.
* Displays win or game-over messages.
* Console-based Python application.

---

## Technologies Used

* Python 3
* Random Module

---

## Project Structure

```text
CodeAlpha_HangmanGame/
│── hangman.py
│── README.md
```

---

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code or any Python IDE.
3. Open the terminal.
4. Run the following command:

```bash
python hangman.py
```

---

## Sample Output

```text
===================================
      WELCOME TO HANGMAN GAME
===================================
Guess the word one letter at a time.
You have 6 incorrect attempts.

Word: _ _ _ _ _
Attempts Left: 6

Enter a letter: a
✅ Correct!

Word: _ a _ _ _
Attempts Left: 6

Enter a letter: x
❌ Wrong!

Attempts Left: 5
```

---

## Learning Outcomes

* Python fundamentals
* Random module
* Lists and strings
* Loops
* Conditional statements
* Functions
* User input handling
* Basic game logic

---

## Author

**Aarthitheivaraj**

CodeAlpha Python Programming Internship
