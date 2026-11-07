
import random

WORDS = ["python", "keyboard", "internship", "variable", "function"]
MAX_WRONG = 6


def display_word(word, guessed_letters):
    """Return the word with unguessed letters shown as underscores."""
    shown = []
    for letter in word:
        if letter in guessed_letters:
            shown.append(letter)
        else:
            shown.append("_")
    return " ".join(shown)


def play_game():
    word = random.choice(WORDS)
    guessed_letters = []   # every letter the player has tried
    wrong_guesses = 0

    print("\n=== HANGMAN ===")
    print(f"Guess the word one letter at a time. You can miss {MAX_WRONG} times.\n")

    while wrong_guesses < MAX_WRONG:
        print("Word:", display_word(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG - wrong_guesses}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)) or "none")

        guess = input("Enter a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

        # Win check: every letter in the word has been guessed
        if all(letter in guessed_letters for letter in word):
            print("Word:", display_word(word, guessed_letters))
            print(f"Congratulations, you won! The word was '{word}'.")
            return

    print(f"Game over! You ran out of guesses. The word was '{word}'.")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()