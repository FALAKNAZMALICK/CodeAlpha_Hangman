import random           # For choosing a random word

def play_hangman():
    # Friendly word list
    words = ["apple", "random", "fun", "study", "civic"]
    secret_word = random.choice(words)

    guessed_letters = []
    attempts = 6                # Player has 6 wrong tries

    print(" Welcome to Hangman!")
    print("Guess the secret word, one letter at a time...")

    while attempts > 0:
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print(f"\n Word: {display}")
        print(f" Attempts left: {attempts}")

        # Ask player for a guess
        guess = input(" Your guess: ").lower().strip()

        # Check if input is valid
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        # Check if letter was already guessed
        if guess in guessed_letters:
            print(" You already tried that one!")
            continue

        # Add guess to list
        guessed_letters.append(guess)

        # Correct or wrong guess
        if guess in secret_word:
            print(f" Nice! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word.")

        # Check if player has guessed all letters
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\n CONGRATULATIONS! You guessed it: {secret_word}")
            break
    else:
        print(f"\n Game Over! The word was: {secret_word}")
        print("Better luck next time!")

# Start the game
if __name__ == "__main__":
    play_hangman()
