password = input()
its_all_lower = (password == password.lower())

if its_all_lower:
    print("Invalid Password")
else:
        print("Valid Password")