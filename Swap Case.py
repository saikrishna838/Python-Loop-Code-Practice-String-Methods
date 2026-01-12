word = input()

modified_word = ""

for character in word:
    upper_char = character.upper()
    if upper_char == character:
        modified_word = modified_word + character.lower()
    else:
         modified_word = modified_word + character.upper()
print(modified_word)
