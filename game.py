# game.py
import random
from words import WORDS
from stages import STAGES


def get_random_word():
    return random.choice(WORDS)


def display_word_with_guesses(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def display_game_state(mistakes, secret_word, guessed_letters):
    print("\n" + STAGES[mistakes])
    print("Word: " + display_word_with_guesses(secret_word, guessed_letters))
    print(f"Wrong attempts: {mistakes}/{len(STAGES) - 1}")
    if guessed_letters:
        # Sortiert die Ausgabe für eine klarere Darstellung
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")


def is_valid_guess(guess):
    """Input Validation: Checks if the input is a single alphabetical character."""
    return len(guess) == 1 and guess.isalpha()


def play_round():
    """Plays a single round of the game."""
    secret_word = get_random_word()
    print("\n--- New Round ---")

    mistakes = 0
    max_attempts = len(STAGES) - 1
    guessed_letters = []
    won = False

    while mistakes < max_attempts:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        # 1. Input Validation
        if not is_valid_guess(guess):
            print("Invalid input! Please enter a single letter (a-z).")
            continue

        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        # Check guess
        if guess in secret_word:
            guessed_letters.append(guess)
            print("Correct!")

            # Check win condition
            if all(letter in guessed_letters for letter in secret_word):
                won = True
                break
        else:
            mistakes += 1
            print("Wrong! The snowman is melting...")

    # End of round
    if won:
        print(f"\nCongratulations! You saved the snowman! The word was '{secret_word}'.")
    else:
        print("\n" + STAGES[mistakes])
        print(f"Game Over! The snowman melted. The word was '{secret_word}'.")


def play_game():
    """Main game loop with Replay Option."""
    print("Welcome to Snowman Meltdown!")

    while True:
        play_round()

        # Replay Option
        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay not in ['yes', 'y', 'ja', 'j']:
            print("Thanks for playing! Goodbye.")
            break