import random
import time

# --- Function definitions ---

def number_guessing_game():
    # Intro text
    print("--> Alright, let's play a guessing game.")
    print("--> Enter two numbers or the guessing machine.")

    # Lower bound integer variable with safety for ValueError
    while True:
        try:
            lower_bound = int(input("Lower bound integer: "))
            break  # input was valid, break out of loop
        except ValueError:
            print("--> Not a valid integer. Try again.")

    # Upper bound integer variable with safety for ValueError
    while True:
        try:
            upper_bound = int(input("Upper bound integer: "))
            break  # input was valid, break out of loop
        except ValueError:
            print("--> Not a valid integer. Try again.")

    # Generate a random integer and assign it to num variable
    num = random.randint(lower_bound, upper_bound)

    # Display lower and upper bounds
    print("--> Alright! Time to guess.")
    print("--> Lower bound: " + str(lower_bound))
    print("--> Upper bound: " + str(upper_bound))

    # Assigning user input to guess variable with safety for ValueError
    while True:
        try:
            guess = int(input("Your guess: "))
            break
        except ValueError:
            print("--> Not a valid guess. Try an integer.")

    # Checking if the guess variable is the same as the num variable
    if guess == num:
        print("--> Correct! The number was " + str(num))
    else:
        print("--> Unlucky guess... the number was actually " + str(num))

def simple_calculator():
    pass

def dice_roller():
    pass

def quiz_game():
    pass

def password_generator():
    pass

def rock_paper_scissors():
    pass

def countdown_timer():
    pass


# --- Start-up Logo ---
def display_ascii_art():
    ascii_art = """
  ___          _ _                _    
 | __|__ _ ___| | |_ ___ _ _ _ __( )___
 | _|/ _` / -_) |  _/ _ \ '_| '_ \/(_-<
 |___\__, \___|_|\__\___/_| | .__/ /__/
     |___/                  |_|        
         _____         _ _             
        |_   _|__  ___| | |__  _____ __
          | |/ _ \/ _ \ | '_ \/ _ \ \ /
          |_|\___/\___/_|_.__/\___/_\_\                                                                              
"""
    print(ascii_art)

# --- Show the tool select screen ---
def show_menu():
    print("\nSelect a program to run from the toolbox:")
    print("0. Show this menu.")
    print("1. Number Guessing Game")
    print("2. Simple Calculator")
    print("3. Dice Roller")
    print("4. Quiz Game")
    print("5. Password Generator")
    print("6. Rock, Paper, Scissors!")
    print("7. Countdown Timer")
    print("8. Exit")

def main():
    display_ascii_art() # Show ASCII-art on Start-up
    show_menu() # Show the Menu Interface

    while True:

        choice = input("Enter your choice of game (1-8): ")

        if choice == "0":
            show_menu()
        elif choice == "1":
            number_guessing_game()
        elif choice == "2":
            simple_calculator()
        elif choice == "3":
            dice_roller()
        elif choice == "4":
            quiz_game()
        elif choice == "5":
            password_generator()
        elif choice == "6":
            rock_paper_scissors()
        elif choice == "7":
            countdown_timer()
        elif choice == "8":
            print("--> See you later, I guess.")
            time.sleep(0.5)
            exit()
        else:
            print("--> Invalid choice. Please choose between 1-8.")

if __name__ == "__main__":
    main()