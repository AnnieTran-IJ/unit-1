# Quiz 001

## Paper Solution
![image](https://github.com/user-attachments/assets/111d36fd-ce4b-453c-b8d9-5b227c3022e3)

## Code
```.py
def processandcount(i):
    if len(i) <= 2:
        return i
    else:
        first_char = i[0]
        middle_count = len(i) - 2
        last_char = i[-1]
        return f"{first_char}{middle_count}{last_char}"

def split_sentence(sentence):
    words = sentence.split()
    join_words = [processandcount(i) for i in words] #loop the process through each of the splitted word in a sentence
    return " ".join(join_words)

# Test
for x in range(5):
    input_sentence = input("Enter a sentence: ")
    output = split_sentence(input_sentence)
    print(output)

```
## Proof of work
![image](https://github.com/user-attachments/assets/cfb0b210-b1a8-4fde-bf79-e50525151968)

