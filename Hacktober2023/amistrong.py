import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."
    elif not re.search("[a-z]", password):
        return "Weak: Password should contain at least one lowercase letter."
    elif not re.search("[A-Z]", password):
        return "Weak: Password should contain at least one uppercase letter."
    elif not re.search("[0-9]", password):
        return "Weak: Password should contain at least one number."
    elif not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password should contain at least one special character."
    else:
        return "Strong: Password is secure."

if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(strength)
