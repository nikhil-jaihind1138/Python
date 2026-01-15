char = input("Enter a character which you want to check whether it's vowel or consonant: ")
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print(f"The character {char} is a vowel.")
else:
    print(f"The character {char} is a consonant.")
    
    
    
    
char = input("Enter a character which you want to check whether it's vowel or consonant: ")
if char in ('a', 'e', 'i', 'o', 'u'):
    print(f"The character {char} is a vowel")
else:
    print(f"The character {char} is consonant.")