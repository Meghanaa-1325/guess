import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 7 attempts to guess it correctly.\n")

    number_to_guess = random.randint(1, 100)
    attempts = 7

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")
            continue

        if guess < 1 or guess > 100:
            print("⛔ Please guess a number between 1 and 100.")
            continue

        if guess == number_to_guess:
            print(f"🎉 Correct! You guessed the number in {attempt} attempt(s).")
            break
        elif guess < number_to_guess:
            print("🔼 Too low! Try again.")
        else:
            print("🔽 Too high! Try again.")

    else:
        print(f"\n😢 You've used all your attempts. The number was {number_to_guess}.")

    play_again = input("🔁 Do you want to play again? (yes/no): ").lower()
    if play_again in ['yes', 'y']:
        number_guessing_game()
    else:
        print("👋 Thanks for playing!")

# Run the game
number_guessing_game()
