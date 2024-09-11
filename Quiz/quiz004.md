# Quiz 004

## Paper Solution
![Uploading image.png…]()

## Code
```.py
def factorial(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            print(f"{i} is the factor of {num}")
            sum += i
    if sum == num:
        print(f"{num} is a perfect number")
        print(" ")
    else:
        print(f"{num} is not a perfect number")
        print(" ")

num = [21, 55, 10, 90, 6]
for i in num:
    factorial(i)
```
## Proof of work
![image](https://github.com/user-attachments/assets/5994733c-b48f-4997-80ac-5ec74cb512b8)
![image](https://github.com/user-attachments/assets/13c28767-acec-43af-b4d1-83d133ecc1a8)


