string = input()

reverse_string = ""

for char in string:
    reverse_string = char + reverse_string
    
if string == reverse_string:
    print("True")
else:
    print("False")