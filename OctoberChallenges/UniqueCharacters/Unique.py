
# Function to determine if the entered String contains only unique characters.
def unique(String):
    # Variable list to store unique characters.
    uniqueCharacters = []

    # If condition to avoid evaluating empty strings.
    if String == "":
        return False

    # Loop through each character in the string. 
    # If the character is already in uniqueCharacters then return False. 
    # Else add it to uniqueCharacters.
    for character in str(String):

        if character in uniqueCharacters:
            return False
        else:
            uniqueCharacters.append(character)

    # If the loop completed without returning False, 
    # then all the characters the loop iterated through are unique.
    return True

print(unique("Hello")) # False
print(unique("abcdefg")) # True
print(unique("oafergfd")) # False
print(unique("Biasfb")) # True
print(unique("afjiwer")) # True
print(unique("563421")) # True
print(unique("5635421")) # False
print(unique("56a3!42b1")) # True
print(unique("!@#$(*&^)")) # True
print(unique("!@#$%@^!")) # False
print(unique("")) # False
