from cfonts import render
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame
import random

import getpass

global home_code

#color indication:
end_code = "\033[00m"
green = "\33[0;32m"
red = "\33[0;31m"
underline_start = "\033[4m"
underline_end = "\033[0m"
bold_purple = "\33[1;35m"
bold_white = "\33[1;37m"
bold_blue = "\33[1;34m"

def validate_home_code(home_code):
    # 3 digits + 1 letter + 3 digits
    if len(home_code) != 7:
        return False

    # Check if the first three characters are digits
    if not home_code[:3].isdigit():
        return False

    # Check if the next character is a letter
    if not home_code[3].isalpha():
        return False

    # Check if the last three characters are digits
    if not home_code[4:].isdigit():
        return False

    return True

def three_attempt():
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        global home_code
        home_code = getpass.getpass("Please enter the code to your assigned house: ")
        # Validate the password format
        if validate_home_code(home_code):
            print(f"{green}Access granted.{end_code}")
            return True
        else:
            attempts += 1
            print(f"{red}Incorrect password format. You have {max_attempts - attempts} attempts left.{end_code}")

    print(f"{bold_purple}Too many incorrect attempts. Program will now exit.{end_code}")
    return False

def password_mode():
    print(render(text='Secret Mode Activated', colors=['red', 'red', 'red'], align='center', font="chrome", letter_spacing=0))
    #play the sound
    file_path = r"D:\XiMuoi\Coding\ComputerScience\Project_1\audio\secretmode.wav"
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    if not three_attempt():  # If access is not granted, exit the program
        exit()

# Encryption and decryption functions
def rot13_encryption(new_password):
    result = []
    for char in new_password:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)


def rot13_decryption(encrypted_password):
    decrypted_password = []
    for char in encrypted_password:
        if 'a' <= char <= 'z':
            decrypted_password.append(chr(((ord(char) - ord('a') + 13) % 26) + ord('a')))
        elif 'A' <= char <= 'Z':
            decrypted_password.append(chr(((ord(char) - ord('A') + 13) % 26) + ord('A')))
        else:
            decrypted_password.append(char)
    return ''.join(decrypted_password)

def generate_password(length, include_symbols):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    symbols = "!@#$%^&*"
    if include_symbols:
        character_option = alphabet + symbols
    else:
        character_option= alphabet

    password = ""
    for i in range(length):
        n = random.randint(0, len(character_option) - 1)
        password += character_option[n]

    return password
# Password management features
global encrypted_username
def add_password():
    new_username = input(f"\nPlease enter a new {underline_start}username{underline_end} for your password: ")
    new_password = input(f"Please enter a new {underline_start}password{underline_end}. If you need a strong suggested password, enter X: ")
    encrypted_username = rot13_encryption(new_username)

    if new_password == "x":
        symbol_preference = input("Do you want to include symbols in the passwords? (TRUE/FALSE): ").upper()  # upper is to make everything uppercase letters
        include_symbols = symbol_preference == "TRUE"
        length = int(input("How many characters do you want your password to be? "))
        suggested_password = generate_password(length, include_symbols)
        encrypted_password = rot13_encryption(suggested_password)
        save_password_or_not = input(f"Your suggested password is {bold_blue}{suggested_password}{end_code}. Do you want to save this (y/n): ")
        if save_password_or_not == "y":
            with open('D:\\XiMuoi\\Coding\\ComputerScience\\Project_1\\database\\passwords.csv', mode='a') as file:
                file.writelines(f"{encrypted_username} - {encrypted_password}\n")
            print(f"{green}Password added and encrypted successfully.\n{end_code}")
        elif save_password_or_not == "n":
            print(f"{red}Password not saved.{end_code}")
        else:
            print(f"{red}Invalid input. Try again. {end_code}")
    else:
        encrypted_password = rot13_encryption(new_password)

        with open('D:\\XiMuoi\\Coding\\ComputerScience\\Project_1\\database\\passwords.csv', mode='a') as file:
            file.writelines(f"\n{encrypted_username} - {encrypted_password}\n")

        print(f"{green}Password added and encrypted successfully.\n{end_code}")

def delete_password():
    password_to_delete = input("Enter the username of the password to delete: ")

    with open('D:\\XiMuoi\\Coding\\ComputerScience\\Project_1\\database\\passwords.csv', mode='r') as file:
        lines = file.readlines()

    found = False
    updated_lines = []

    # Loop through each line to find the matching username
    for line in lines:
        line = line.strip()
        if not line:  # Skip empty lines
            continue
        username, _ = line.split(' - ', 1)  # Split at first " - " to get username
        decrypted_username = rot13_decryption(username)

        if decrypted_username == password_to_delete:
            print(f"{green}Found the password for {password_to_delete}.{end_code}")
            found = True
            confirmation = getpass.getpass(f"{red}You are deleting the password. Please re-enter your home code to confirm your action: {end_code}")
            if confirmation == home_code:
                print(f"{green}Password deleted successfully.{end_code}")
                continue  # Skip adding this line to updated_lines
            else:
                print(f"{red}Invalid home code. Password not deleted.{end_code}")
                updated_lines.append(line)  # Add back the line since deletion failed
        else:
            updated_lines.append(line)  # Keep this line if no match is found

    if not found:
        print(f"No password found for username: {password_to_delete}.")

    # Rewrite the file with the updated lines
    with open('D:\\XiMuoi\\Coding\\ComputerScience\\Project_1\\database\\passwords.csv', mode='w') as file:
        file.writelines(updated_lines)

def view_password():
    with open('D:\\XiMuoi\\Coding\\ComputerScience\\Project_1\\database\\passwords.csv', mode='r') as x:
        data = x.readlines()

    if not data:
        print("No passwords found.")
        return

    print("Stored passwords:")
    for line in data:
        if ' - ' in line:
            parts = line.split(' - ', 1)
            if len(parts) == 2:
                username, encrypted_password = parts
            else:
                print(f"Invalid line format: {line}")
                continue

            decrypted_username = rot13_decryption(username)
            decrypted_password = rot13_decryption(encrypted_password)
            print(f"{decrypted_username} - {decrypted_password}")
def update_password():
    print("This is the current list of passwords: ")
    view_password()

    password_to_update = input("Enter the username of the password to update: ")

    # Open the file and read existing passwords
    with open('D:\\XiMuoi\\Coding\\ComputerScience\\Project_1\\database\\passwords.csv', mode='r') as file:
        lines = file.readlines()

    # Initialize a flag to check if the password was found
    found = False
    updated_lines = []

    # Loop through each line to find the matching username
    for line in lines:
        line = line.strip()  # Remove any leading/trailing whitespaces
        if not line or ' - ' not in line:  # Skip empty or improperly formatted lines
            continue

        try:
            encrypted_username, encrypted_password = line.split(' - ', 1)
        except ValueError:
            print(f"Skipping improperly formatted line: {line}")
            continue

        decrypted_username = rot13_decryption(encrypted_username)

        if decrypted_username == password_to_update:
            print(f"{green}Found the password for username `{password_to_update}`{end_code}.")

            # Prompt for a new password
            new_password = input(f"Enter the new password for {password_to_update}: ")

            # Encrypt the new password
            encrypted_new_password = rot13_encryption(new_password)

            # Replace the line with the updated password
            updated_lines.append(f"{encrypted_username} - {encrypted_new_password}\n")
            found = True
        else:
            updated_lines.append(line + '\n')  # Keep the line unchanged

    if not found:
        print(f"{red}No password found for username: {password_to_update}.{end_code}")
    else:
        # Write the updated lines back to the file
        with open('D:\\XiMuoi\\Coding\\ComputerScience\\Project_1\\database\\passwords.csv', mode='w') as file:
            file.writelines(updated_lines)

        print(f"{green}Password for `{password_to_update}` has been updated successfully.{end_code}")

#others:
def clear_screen():
    print("\n" * 100)

#main:
def password_management():
    while True:
        print(f"{bold_white}\nPlease select one of the following options.{end_code}")
        print("------------------------------------------")
        print("1. Add a new password.")
        print("2. Delete a password.")
        print("3. Update a password.")
        print("4. View all password.")
        print("5. Return to task management program.")
        print("------------------------------------------")
        choice = input("Enter your choice: ")


        if choice == "1":
            add_password()
        elif choice == "2":
            delete_password()
        elif choice == "3":
            update_password()
        elif choice == "4":
            view_password()
        elif choice == "5":
            clear_screen()
            return
        else:
            print(f"{red}Invalid input. Please try again.{end_code}\n")
