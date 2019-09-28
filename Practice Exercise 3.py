# Write a code that will look for a vowel letter.
def isVowel(char):
    return char.lower() in 'aeiou'
    
letter = str(input("Please enter a letter "))
print(isVowel(letter))