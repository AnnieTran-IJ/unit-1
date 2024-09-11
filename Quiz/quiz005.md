# Quiz 005

## Paper Solution
![image](https://github.com/user-attachments/assets/6af01a65-82fa-4873-b57d-e1ed49859bb4)

## Code
```.py
# ASCII value of 'A' is 65.
# ASCII value of 'a' is 97.
# ASCII value of '0' is 48.
def sum_sl(input_string_sl):
    value_map = {
        'A': 1, 'a': 1, 'B': 2, 'b': 2, 'C': 3, 'c': 3, 'D': 4, 'd': 4, 'E': 5, 'e': 5, 'F': 6, 'f': 6, 'G': 7, 'g': 7,
        'H': 8, 'h': 8, 'I': 9, 'i': 9, 'J': 10, 'j': 10, 'K': 11, 'k': 11, 'L': 12, 'l': 12, 'M': 13, 'm': 13, 'N': 14,
        'n': 14, 'O': 15, 'o': 15, 'P': 16, 'p': 16, 'Q': 17, 'q': 17, 'R': 18, 'r': 18, 'S': 19, 's': 19, 'T': 20,
        't': 20, 'U': 21, 'u': 21, 'V': 22, 'v': 22, 'W': 23, 'w': 23, 'X': 24, 'x': 24, 'Y': 25, 'y': 25, 'Z': 26, 'z': 26
    }

    total = 0
    for char in input_string_sl:
        if char in value_map:
            total += value_map[char]
        else: #for spaces or comma,...
            total += 0
    return total


def sum_of_char_hl(input_string_hl):
    value = {
        'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74,
        'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84,
        'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90,
        'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105,
        'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114,
        's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122
    }
    total = 0
    for char in input_string_hl:
        if char in value:
            total += value[char]
        else: #for spaces or comma,...
            total += 0
    return total

#test
input_string_sl = ["Math", "maTH", "Hello world", "Computer SCIENCE"]
for i in input_string_sl:
    print(f"The sum of the {i} is {sum_sl(i)}")


input_string_hl = "Math"
print(f"The sum of the {input_string_hl} is {sum_of_char_hl(input_string_hl)}")

```
## Proof of work
![image](https://github.com/user-attachments/assets/7f590dd5-b63c-4dcd-9385-89f2ab03bbd8)

