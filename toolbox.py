import random
import time
import sys

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
    print("-> Lower bound: " + str(lower_bound))
    print("-> Upper bound: " + str(upper_bound))

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

def even_or_odd():
    # Intro text
    print("--> Even or Odd Checker")

    # Integer variable with safety for ValueError
    while True:
        try:
            integer_to_check = int(input("Enter an integer: "))
            break  # input was valid, break out of loop
        except ValueError:
            print("--> Not a valid integer. Try again.")

    # Check if there is any remainder when dividing by 2, to see if even
    # Then display result with an added bias string
    if integer_to_check % 2 == 0:
        print("The number " + str(integer_to_check) + " is luckily Even!")
    else:
        print("The number " + str(integer_to_check) + " is unfortunately Odd :(")

    # For the "memelord" Elon Musk fans who can't understand actual humor
    if integer_to_check == 69 or integer_to_check == 420:
        print("Also: you're not funny boy!")

def dice_roller():
    # Loop for rolling dice and quitting loop
    print("--> Time to gamble! Or maybe not, but we can roll some dice I guess.")
    while True:
        choice = input("[R] to Roll / [Q] to Quit: ").lower()

        if choice == "r":
            print("Rolling...")
            for _ in range(15): # Simulate 10 rolls for cool effect
                dice_roll = random.randint(1, 6)
                sys.stdout.write(f"\r{dice_roll}   ")
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.flush()
            print(f"\nBoom! You rolled a {dice_roll}!")  # Print the final result
        elif choice == "q":
            break
        else:
            print("--> Really...? That is NOT a valid choice. Rethink!")

def quiz_game():
    print("Not done yet.")
    pass

def password_generator():
    print("Not done yet.")
    pass

def rock_paper_scissors():
    print("Not done yet.")
    pass

def countdown_timer():
    print("Not done yet.")
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
    print("\n--> Select a program to run from the toolbox:")
    print()
    print("0. Show this list")
    print()
    print("1. Number Guessing Game")
    print("2. Even or Odd")
    print("3. Dice Roller")
    print("4. Quiz Game")
    print("5. Password Generator")
    print("6. Rock, Paper, Scissors!")
    print("7. Countdown Timer")
    print("8. Exit")

def main():
    display_ascii_art() # Show ASCII-art on Start-up

    while True:
        show_menu() # Show the Menu Interface
        print()
        choice = input("Enter your choice of game (0 - 8): ")
        print()

        if choice == "0":
            show_menu()
        elif choice == "1":
            number_guessing_game()
        elif choice == "2":
            even_or_odd()
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
            print("--> Invalid choice. Please choose between 0 - 8.")
            print("Help: Choose 0 for the list of choices.")

if __name__ == "__main__":
    main()

#   _____   _____       ___   ____   ____  ________                               
#  |_   _| |_   _|    .'   `.|_  _| |_  _||_   __  |                              
#    | |     | |     /  .-.  \ \ \   / /    | |_ \_|                              
#    | |     | |   _ | |   | |  \ \ / /     |  _| _                               
#   _| |_   _| |__/ |\  `-'  /   \ ' /     _| |__/ |                              
#  |_____| |________| `.___.'     \_/     |________|                              
#   ____    ____   ___   ____  _____  ___  ____   ________  ____  ____   ______   
#  |_   \  /   _|.'   `.|_   \|_   _||_  ||_  _| |_   __  ||_  _||_  _|.' ____ \  
#    |   \/   | /  .-.  \ |   \ | |    | |_/ /     | |_ \_|  \ \  / /  | (___ \_| 
#    | |\  /| | | |   | | | |\ \| |    |  __'.     |  _| _    \ \/ /    _.____`.  
#   _| |_\/_| |_\  `-'  /_| |_\   |_  _| |  \ \_  _| |__/ |   _|  |_   | \____) | 
#  |_____||_____|`.___.'|_____|\____||____||____||________|  |______|   \______.' 
#                                                                                 