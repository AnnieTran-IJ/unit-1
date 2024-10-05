# Quiz 009

## Paper Solution
![image](https://github.com/user-attachments/assets/2d12b8ed-4a09-4cd5-ae6f-8c9e49eb4bf7)

## Flow Chart
![image](https://github.com/user-attachments/assets/3b58475a-3fc0-4d13-ac81-b5af49b8c2a3)

## Code
```.py
def cypher_code(shift, new_password):
    result = []
    for char in new_password:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

print(cypher_code(13,"hello world"))
print(cypher_code(13,"abcdefghijklmnopqrstuvwxyz"))
print(cypher_code(-10,"secret"))


```
## Proof of work
![image](https://github.com/user-attachments/assets/262f458f-4726-4c55-b01f-0e940d8c6901)

