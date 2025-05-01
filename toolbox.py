import random
import time
import sys

#     __                  _   _                 
#    / _|                | | (_)                
#   | |_ _   _ _ __   ___| |_ _  ___  _ __  ___ 
#   |  _| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
#   | | | |_| | | | | (__| |_| | (_) | | | \__ \
#   |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#
                                                                                         
def number_guessing_game():
    # Intro text
    print_box("Number Guessing Game")
    print("Alright, let's play a guessing game.")
    print("Enter two numbers for the guessing machine.")

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

    wait_before_menu()

def even_or_odd():
    # Intro text
    print_box("Even or Odd Checker")

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

    wait_before_menu()


def dice_roller():
    # Loop for rolling dice and quitting loop
    print_box("Dice Roller")
    print("--> Time to gamble! Or maybe not, but we can roll some dice I guess.")
    while True:
        choice = input("[R] to Roll / [Q] to Quit: ").lower()

        if choice == "r":
            print("Rolling...")
            for _ in range(15): # Simulate rolls for cool effect
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

    wait_before_menu()


def quiz_game():
    # Sounds boring so I'm procrastinating it
    print_box("Not done yet.")
    wait_before_menu()


def password_generator():
    # Define letters manually and count
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_count = sum(1 for char in letters if char.isalpha())

    # Define special characters and count
    chars = "!#%&"
    char_count = sum(1 for char in chars)

    # Combine both sets into a singular set to later choose from
    # 
    # Also multiply char set to spread out the odds of 
    # letters vs chars in final password generated 
    # (sloppy but works for now)
    #
    pick_set = chars * int((letter_count / char_count)/2) + letters

    # Intro
    print_box("Password Generator")

    # Get the Minimum length for the password
    while True:
        try:
            min_length = int(input("Minimum length: "))
            break
        except ValueError:
            print("! Not an integer. Try again.")

    # Get the Maximum length for the password
    # +++ Make sure it is longer than Minimum length
    while True:
        try:
            max_length = int(input("Maximum length: "))

            if max_length < min_length:
                print("! MAXIMUM length CAN NOT be smaller than MINIMUM length! Try again.")
            else:
                break
        except ValueError:
            print("! Not an integer. Try again.")

    # Generate a random length for the password
    # based on the min/max values
    #
    random_length = random.randint(min_length, max_length)

    # Generate a new password by picking [random_length]
    # amount of random characters from the pick_set
    #
    new_password = random.choices(pick_set, k=random_length)

    # Shuffle the password
    #
    random.shuffle(new_password)

    # 1. Cool effect when generating 
    # 2. Joining string and formatting
    # 3. Printing final password
    print("| ")
    for _ in range(10): # Simulate mutliple generations for cool effect
        new_password = random.choices(pick_set, k=random_length)
        random.shuffle(new_password)
        password_string = ''.join(new_password)
        sys.stdout.write(f"\r| Password: {password_string}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.flush()

    print()
    print("| ")
    print("| Length: " + str(random_length) + " characters")
    print("| ")

    # Animated second countdown
    wait_before_menu(9)
    print()


def rock_paper_scissors():
    print_box("Not done yet.")
    wait_before_menu()


def countdown_timer():
    print_box("Not done yet.")
    wait_before_menu()


# --- Start-up Logo ---
def display_ascii_art():
    ascii_art = """
 _____           _ _               
|_   _|__   ___ | | |__   _____  __
  | |/ _ \ / _ \| | '_ \ / _ \ \/ /
  | | (_) | (_) | | |_) | (_) >  < 
  |_|\___/ \___/|_|_.__/ \___/_/\_\                                                                                                   
"""
    print(ascii_art)


# --- Show the tool select screen ---
def show_menu():
    #print("\n--> Select a program to run from the toolbox:")
    print_box("Available Tools")
    print()
    print("1. [DONE] Number Guessing Game")
    print("2. [DONE] Even or Odd")
    print("3. [DONE] Dice Roller")
    print("4. [....] Quiz Game")
    print("5. [WORK] Password Generator")
    print("6. [....] Rock, Paper, Scissors!")
    print("7. [....] Countdown Timer")
    print()
    print("Q. Exit")
    print()

def main():
    display_ascii_art() # Show ASCII-art on Start-up

    while True:
        # Show the Menu Interface
        show_menu() 
        print()

        # Ask for choice input
        choice = input("Enter your choice of program (1 - 7): ")
        print()

        if choice == "1":
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

        elif choice == "Q" or choice == "q":
            print_box("Toolbox.py made by @egeltorp")
            time.sleep(1)
            exit()
            
        else:
            print("! Invalid choice. Please choose between 1 - 7.")
            time.sleep(2)
            print("\n \n \n ")

def print_box(content):
    width = 20 + len(content)

    #Top border
    print("+" + "-" * (width - 2) + "+")

    #Content line
    padding = (width - 2 - len(content)) // 2
    line = "|" + " " * padding + content + " " * (width - 2 - len(content) - padding) + "|"
    print(line)

    #Bottom border
    print("+" + "-" * (width - 2) + "+")

def wait_before_menu(delay_seconds=3):
    print()
    for _ in range(delay_seconds + 1):
        sys.stdout.write(f"\r| Showing Toolbox in {delay_seconds} seconds")
        sys.stdout.flush()
        time.sleep(1)
        delay_seconds -= 1
    sys.stdout.flush()
    print("\n \n \n ")
    

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