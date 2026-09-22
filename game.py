import random
from words import WORDS
from stages import STAGES

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_word_with_guesses(secret_word, guessed_letters):
    """Displays the word with underscores for unguessed letters."""
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current game state: ASCII art, word, and status."""
    print("\n" + STAGES[mistakes])
    print("Word: " + display_word_with_guesses(secret_word, guessed_letters))
    print(f"Wrong attempts: {mistakes}")
    if guessed_letters:
        print(f"Guessed letters: {', '.join(guessed_letters)}")


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    # print("Secret word: " + secret_word)  # For testing only

    mistakes = 0
    max_attempts = len(STAGES) - 1
    guessed_letters = []

    # Game loop
    while mistakes < max_attempts:
        # Display current game state
        display_game_state(mistakes, secret_word, guessed_letters)

        # Get player input
        guess = input("Guess a letter: ").lower()

        # Check guess (basic implementation)
        if guess in secret_word:
            if guess not in guessed_letters:
                guessed_letters.append(guess)
                print("Correct!")
            else:
                print("You already guessed that letter.")
        else:
            mistakes += 1
            print("Wrong! The snowman is melting...")

    # Game over
    print("\n" + STAGES[mistakes])
    print(f"Game Over! The word was '{secret_word}'")