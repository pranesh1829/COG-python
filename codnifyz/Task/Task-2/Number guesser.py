import random

def number_guessing_game():
 
    lower_limit = 1
    upper_limit = 100
    secret_number = random.randint(lower_limit, upper_limit)

    print(f"I have selected a random number between {lower_limit} and {upper_limit}.")

    attempts = 0

    while True:
      
        user_guess = int(input(f"Enter your guess ({lower_limit}-{upper_limit}): "))
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    number_guessing_game()
