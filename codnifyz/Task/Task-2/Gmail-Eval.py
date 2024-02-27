import string

def evaluate_password_strength(password):

    min_length = 8
    min_uppercase = 1
    min_lowercase = 1
    min_digits = 1
    min_special_characters = 1
    special_characters = string.punctuation
  
    if len(password) < min_length:
        return "Weak: Password should be at least 8 characters long."

    if sum(1 for char in password if char.isupper()) < min_uppercase:
        return "Weak: Password should contain at least 1 uppercase letter."

    if sum(1 for char in password if char.islower()) < min_lowercase:
        return "Weak: Password should contain at least 1 lowercase letter."

    if sum(1 for char in password if char.isdigit()) < min_digits:
        return "Weak: Password should contain at least 1 digit."

    if sum(1 for char in password if char in special_characters) < min_special_characters:
        return "Weak: Password should contain at least 1 special character."

    return "Strong: Password meets the criteria."

password_to_check = input("Enter a password to evaluate its strength: ")
result = evaluate_password_strength(password_to_check)
print(result)
