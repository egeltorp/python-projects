import random
import time


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

def show_menu():
    print("\nSelect a program to run from the toolbox:")
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
    while True:
        show_menu() # Show the Menu Interface

        choice = input("Enter your choice (1-8): ")

if __name__ == "__main__":
    main()