string = input()
string = string.lower()

reversed_string = ""

for char in string:
    reversed_string =  char + reversed_string 
    
if string == reversed_string:
    print("True")
else:
    print("False")
    
    