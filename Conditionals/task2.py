# A program that prints a descriptive text to show if each character in a string is a vowel or consonant
# prints not a letter if the character is a special letter
# prints empty string if the string is empty

word  = "Hello,planet"


if not word:
    print("Empty string")
else:
    for letter in word.lower():
        if letter in ("a", "e", "i", "o", "u"):
            print(f"{letter} is a vowel")
        elif not letter.isalpha():
            print(f"{letter} is not a letter")
        else:
            print(f"{letter} is a consonant")
