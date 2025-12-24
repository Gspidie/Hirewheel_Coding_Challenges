# Challenge Overview
Create a program that checks whether a given string is a palindrome for curious users.

* Ignore spaces, punctuation, and capitalization when determining if the string reads the same forward and backward.
* Handle edge cases, including empty strings and mixed characters.
* Follow the UCASE strategy to structure your approach.
* Limit your focused effort to about one hour.

*Examples*

Input: "Racecar" → The string is a palindrome.
Input: "Hello" → The string is not a palindrome.



# U | Understand
* A function that determines if a string is the same forwards and backwards.

# C | Clue Detection
* Input: String
* Output: String
* Clues:
    * "Ignore Spaces": remove " " from string.
    * "Ignore Punctuation": remove punctuation. Determine if isalpha() == true. Determine if integers == true.
    * "Ignore Capitalization": lower()
* Edge Cases:
    * Empty String
    * Punctuation

# A | Assemble
1. Function Decleration: def PalindromeChecker(String)
2. Define Output variables: stringIsPalindrome = "The string is a palindrome." and stringIsNotPalindrome = "The string is not a palindrome."
3. Return false to obvious not Palindromes: e.g. empty strings.
4. Alter the string: Lower case string. Then loop through each index and remove any spaces/punctuation by determining if character at the index isalnum() == true.
5. Take first index and reverse it as the last index. Assign characters to new index values.
6. Compare old string to new string.
7. Return comparison.

# S | Solution
See Palindrome.py

# E | Examine
The solution works as I provided strings that were palindromes and strings that were not palindromes, observing that the message outputted was correct. Alternatively, for improvement, I could have included a unittest class to automatically check if a string is a palindrome. Lastly, the solution I came up with for reversing the string seems to work fine and is quite simple.


[15 minutes setting up Repository and IDE] [15 minutes using UCASE] [20 minutes coding] [10 minutes testing and pushing to Github]