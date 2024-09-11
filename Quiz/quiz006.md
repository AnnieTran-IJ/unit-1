# Quiz 006

## Paper Solution
![image](https://github.com/user-attachments/assets/87d25d48-a3f8-4783-8544-ef19772a32ea)

## Flow Chart
## Code
```.py
import random
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
symbols = "!@#$%^&*"

def generate_password(length, include_symbols):
    if include_symbols:
        character_option = alphabet + symbols
    else:
        character_option= alphabet

    password = ""
    for i in range(length):
        n = random.randint(0, len(character_option) - 1)
        password += character_option[n]

    return password


length = 20
end_code = "\033[00m"
red = "\33[0;31m"
symbol_preference = input("Do you want to include symbols in the passwords? (TRUE/FALSE): ").upper() #upper is to make everything uppercase letters
include_symbols = symbol_preference == "TRUE"
for _ in range(10):
    password = generate_password(length, include_symbols)
    if include_symbols:
        print(f"{red}{password}{end_code}")
    else:
        print(password)

```
## Proof of work
![image](https://github.com/user-attachments/assets/29cf335b-b115-4794-8897-288db7fc9e9e)

