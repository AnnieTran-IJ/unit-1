# Quiz 014

## Paper Solution
![image](https://github.com/user-attachments/assets/168dcf71-fc6a-47d5-a3f6-6df5cdf9aa04)

## Flow Chart
## Code
```.py
def average_length(words):
    total_chars = 0
    total_words = len(words)

    for word in words:
        total_chars += len(word.replace(" ", ""))
    if total_words > 0:
        return total_chars / total_words
    else:
        return 0.0


#Test:
print(average_length(["hello", "main"]))
print(average_length(["Peru", "France", "Nepal"]))
print(average_length(["Computer Science", "Art"]))
print(average_length(["one", "two"]))
```
## Proof of work
![image](https://github.com/user-attachments/assets/5d88d992-2410-4f48-bd9a-7986deb845af)

