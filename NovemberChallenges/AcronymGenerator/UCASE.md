# Challenge Overview
Generate an acronym by taking the first letter of each word in a phrase and returning the uppercase result.

* Prompt the user for a phrase or sentence.
* Split the phrase into words (ignore blank segments or punctuation).
* Collect the first letter of each word, uppercase it, and join into the final acronym.
* Handle edge cases such as empty input or single-word phrases gracefully.

# U | Understand
Create a string using the first character from each word.

# C | Clue Detection
* Input: String
* Output: String
* Edge Cases:
    * Empty input
    * Single-word
    * Number at start of word?

# A | Assemble
1) Create function signature
2) Remove invalid inputs
3) Use split() to extract words into a list based on a seperator.
4) Loop through each element in list and retrieve the first character.
5) Print the retrieved characters as one string.

# S | Solve
The program in Acronym.py takes in a phrase and returns the appropriate acronym. It accounts for edge cases, including invalid input and capitilization, to deliver correct results.

# E | Examine
To imporve the program, unittest could be implemented to automatically provide different phrases to test.