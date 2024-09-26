import time
from font import welcome_sign
import pygame
from secret_mode import password_mode, password_management,clear_screen
from todolist import *
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

welcome_sign()
# play the sound
file_path = r"D:\XiMuoi\Coding\ComputerScience\Project_1\audio\drumroll.wav"
pygame.mixer.init()
pygame.mixer.music.load(file_path)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue


def task_management():
    while True:
        print(f"{bold_white}What would you like to do today? Please select one of the following options.{end_code}")
        time.sleep(1)
        print("------------------------------------------")
        print("1. Add a new task.")
        print("2. Mark a task as done.")
        print("3. View all tasks.")
        print("4. Exit program.")
        print("------------------------------------------")
        time.sleep(1)
        choice = input(f"{underline_start}Enter a number for your according choice:{underline_end} ")
        if choice == "1":
            add_task()
            view_task()
        elif choice == "2":
            mark_as_done()
        elif choice == "3":
            view_task()
        elif choice == "4":
            clear_screen()
            break
        elif choice == "thesecretcode123":
            time.sleep(1)
            password_mode()
            password_management()
            pass

        else:
            print(f"{red}Invalid input. Please try again.{end_code}\n")



task_management()




