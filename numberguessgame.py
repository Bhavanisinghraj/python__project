def guess_number(secret_number):
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print(f"I've picked a number between 1 and 100. Try to guess it. You chose {secret_number}.")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    chosen_number = int(input("Enter the number you want to guess (between 1 and 100): "))
    guess_number(chosen_number)
