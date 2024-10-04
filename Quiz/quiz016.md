# Quiz 016

## Paper Solution
![image](https://github.com/user-attachments/assets/a119eaae-d67c-4375-8b49-8a75c79d7f17)
![image](https://github.com/user-attachments/assets/a5cde70b-321b-44d4-8657-2b343411c8f6)

## Flow Chart
## Code
```.py
def get_l3tt3r(msg):
    word = []
    for char in msg:
        if char == "a":
            word.append("4")
        elif char == "e":
            word.append("3")
        elif char == "i":
            word.append("1")
        elif char == "o":
            word.append("0")
        elif char == " ":
            word.append("_")
        else:
            word.append(char)

    return ''.join(word)
# Test
print(get_l3tt3r("Hello World"))
print(get_l3tt3r("Why did I choose CS?"))
print(get_l3tt3r("Remember the Figure Caption"))

```
## Proof of work
![image](https://github.com/user-attachments/assets/365bf033-9b2f-4d94-b970-e14b415c18b2)


