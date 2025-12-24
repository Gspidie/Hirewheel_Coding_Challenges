def PalindromeChecker(OriginalString):
    stringIsPalindrome = "The string is a palindrome."
    stringIsNotPalindrome = "The string is not a palindrome."
    correctedString = ""
    backwardsString = ""

    if OriginalString == " " or OriginalString == "":
        return stringIsNotPalindrome

    for character in OriginalString:
        if character.isalnum() == True:
            correctedString += character.lower()

    counter = len(correctedString) - 1

    for character in correctedString:
        backwardsString += correctedString[counter]

        counter -= 1

    if correctedString == backwardsString:
        return stringIsPalindrome
    else:
        return stringIsNotPalindrome

print(PalindromeChecker("RaceCar")) # The string is a palindrome.
print(PalindromeChecker(" ^R&A*cE C. A r")) # The string is a palindrome.
print(PalindromeChecker("aa1b1335tt5331b1aa")) # The string is a palindrome.
print(PalindromeChecker("fkwf--fwr3442fwkfewf")) # The string is not a palindrome.
print(PalindromeChecker("Raeecar")) # The string is not a palindrome.
print(PalindromeChecker("")) # The string is not a palindrome.
print(PalindromeChecker(" ")) # The string is not a palindrome.

