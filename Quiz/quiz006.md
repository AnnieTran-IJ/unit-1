# Quiz 005

## Paper Solution

## Flow Chart
## Code
```.py
import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits
    passwords_list = []
    for i in range(length):
        char = random.choice(characters)
        passwords_list.append(char)
    password = ''.join(passwords_list)
    return password

#test:
for time in range(10):
    print(generate_password(20))

```
## Proof of work
![image](https://github.com/user-attachments/assets/06d604c9-f3e0-4c8e-ac9f-041b7317af25)
