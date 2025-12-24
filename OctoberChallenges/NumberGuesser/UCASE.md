# Challenge Overview
Create a CLI program that plays a guessing game with the user.

* Randomly select a number between 1 and 100 when the game starts.
* Prompt the user for guesses until they find the number.
* Tell the user whether their guess is too high or too low, and allow repeated attempts.
* Congratulate the player and exit when the guess is correct.
* Handle invalid inputs gracefully (non-numeric values or numbers outside the range).
* Follow the UCASE strategy and limit focused time to about one hour.

# U | Understand
A guessing game that responds Too High or Too Low based on user guesses.

# C | Clue Detection
* Input: Integer (input())
* Output: String (print())
* Edge Cases/Clues/Clarification: 
    * EC: Enters number outside range.
    * EC: Enters ""
    * EC: Enters non-integer
    * Clue: "Randomly select a number between 1 and 100" -> random.randint()
    * Clue: "until" -> While loop
    * Clue: "too high or too low" -> <, >, <=, >=
    * Clue: "invalid" -> try/except

# A | Assemble
1) Function Signature: def numberGuesser():
2) Make while loop to countinue iterating until the guess is found.
3) try/except to handle any errors.
4) Inside the try, ask for a number from 1-100 with input() and use int() to convert string to a integer.
5) Use if/elif/else to account for Too High, Too Low, Correct, and Invalid guesses.
6) Exit loop if guess is correct and congratulate the player.

# S | Solve
The program I made works well and meets the requirements established. It generates a random number, takes a guess, validates it, and responds accordingly.

Refer to Guesser.py for full solution.

# E | Examine
Again, the game works well. However, to improve, the code could be refactored to be unittest applicable. For example, I can move the control flow (if/elif/else) portion into its own function. Then I could easily plug in values and ensure the program delivers the appropiate response using the unittest meathods.


