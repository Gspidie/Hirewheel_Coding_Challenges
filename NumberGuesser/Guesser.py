import random

# A guessing game that responds Too High or Too Low based on user guesses.
def numberGuesser():
    # Generate random number from 1 to 100.
    number = random.randint(1, 100)

    # Store the game state.
    userHasNotGuessedNumber = True

    # While loop to excute as long as the user has not guessed the number
    while userHasNotGuessedNumber:
        # try/except to account for invalid inputs.
        try:
            # Collect string input from user and convert it to an integer.
            guess = int(input("\nGuess a integer from 1 to 100: "))

            # Respond to user's guess
            if guess == number:
                userHasNotGuessedNumber = False
            elif 1 <= guess < number:
                print("\nToo Low!")
            elif number < guess <= 100:
                print("\nToo High!")
            else: 
                print(f"\n{guess} is not between 1 and 100.")

        except:
            print("\nOops. Please enter an integer for your guess!")

    # Congratulate the user if they exit the loop and their guess is correct.
    print(f"\nCongratulations! The number was indeed {number}")

numberGuesser()
