# Challenge Overview
Create a function that checks whether all characters in a string are unique.

* Return True if the string contains only unique characters; otherwise return False.
* Think about how to handle empty strings, whitespace, different cases, or non-alphabetic characters.
* Consider time and space trade-offs (e.g., set-based checks vs. sorting).
* Follow the UCASE strategy and limit focused time to about one hour.

*Examples*

Input: "abcdef" → True
Input: "hello" → False

# U | Understand
A function that checks if a character is not repeated.

# C | Clue Detection
* Input: String
* Output: Boolean
* Clues:
    * "if the string contains...": if/else
* Edge Cases/Clarifying questions:
    The decisions defined below were made by myself. These edge cases would need clarification during an interview.
    * Empty Strings: "" will not be evaluated and will return False
    * Whitespaces: " " will be considerd a character and, like the other characters, the string may only include one.
    * Cases: "a" and "A" will be considerd unique characters.
    * Non-alphabetic characters: "1" and "?" will be considerd a character and, like the other characters, the string may only include one.

# A | Assemble
1) Function definition: def unique(String):
2) if String == "" then the program must return False
3) Create a list variable to store unique characters
4) Loop through each character in the string using a For Loop. Add unique characters to the list, if the character is in the list then return False.
5) return True as finishing the loop means all values in the String are unique.

# S | Solve
I defined the function signature. Then I added a variable to keep track of unique characters and an if to return False if the string is "". I implemented the loop, returning False if the character is in the variable tracking unique characters and, if not, then added the else to append new unique characters. Lastly I returned a True if the program successfully exited the For Loop.

# E | Examine
I know my solution works because I tested the function with different Strings. To improve, I could attempt to simply the for loop using list comprehension. I am not as familiar with the technique but I know list comprehension is capable of a lot and their is many solutions to apparoach this challenge from.

