# Extra Quiz On 22/08

## Paper Solution


## Code
```.py
def process():
    number = input('Enter an integer number of 1 & 0: ')
    x = number.count('1')
    number_str = ''.join(number)  # Convert the list into a string without brackets
    if x%2 == 0:
        print(f"1{number_str}")
    else:
        print(f"0{number_str}")

for i in range(2):
    process()
```
## Proof of work
![image](https://github.com/user-attachments/assets/cc855ab1-50e6-4a61-8398-6d3c663c41ea)
