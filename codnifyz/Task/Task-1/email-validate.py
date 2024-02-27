import re

def is_valid_email(email):
    # Define a regular expression pattern for a basic email validation
    email_pattern = re.compile(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')

    # Use the pattern to match the email address
    match = email_pattern.match(email)

    # Return True if the email is valid, False otherwise
    return bool(match)

# Example usage:
email_to_check = input("Enter an email address to validate: ")

if is_valid_email(email_to_check):
    print(f"{email_to_check} is a valid email address.")
else:
    print(f"{email_to_check} is not a valid email address.")
