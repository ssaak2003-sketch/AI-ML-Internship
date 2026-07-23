password = input("Enter your password: ")

if len(password) < 8:
    print("Weak Password! Password must be at least 8 characters long.")

elif not any(char.isdigit() for char in password):
    print("Weak Password! Add at least one number.")

elif not any(char.isupper() for char in password):
    print("Weak Password! Add at least one uppercase letter.")

elif not any(char.islower() for char in password):
    print("Weak Password! Add at least one lowercase letter.")

else:
    print("Strong Password!")