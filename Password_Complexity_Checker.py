import re
def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return "Strong password!"
    else:
        feedback = "Weak password. Consider the following improvements:\n"
        if not length_criteria:
            feedback += "- Ensure the password is at least 8 characters long.\n"
        if not uppercase_criteria:
            feedback += "- Include at least one uppercase letter.\n"
        if not lowercase_criteria:
            feedback += "- Include at least one lowercase letter.\n"
        if not digit_criteria:
            feedback += "- Include at least one digit.\n"
        if not special_char_criteria:
            feedback += "- Include at least one special character (!@#$%^&*(),.?\":{}|<>).\n"

        return feedback

def main():
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()
