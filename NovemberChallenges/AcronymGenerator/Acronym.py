

def acronym(phrase): 
    wordsSkippedInAcronyms = ["of", "and"]
    acronym = ""

    if type(phrase) != str:
        return ""
    
    if phrase == "":
        return ""
    
    wordList = phrase.split()
    
    for word in wordList:
        if word.lower() not in wordsSkippedInAcronyms:
            acronym += word[0]

    return acronym.upper()

print(acronym("Central Intelligence Agency"))
print(acronym("National Aeronautics and Space Administration"))
print(acronym("Federal Bureau of Investigation"))
print(acronym("Federal Emergency Management Agency"))
