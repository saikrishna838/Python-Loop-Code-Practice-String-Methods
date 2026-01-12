string = input()

upper_case_letters = ""

for character in string:
    is_upper = (character == character.upper())
    if is_upper:
        upper_case_letters = upper_case_letters + character
print(upper_case_letters)