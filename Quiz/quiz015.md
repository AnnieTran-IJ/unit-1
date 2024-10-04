# Quiz 015

## Paper Solution
![image](https://github.com/user-attachments/assets/ba45fbe8-0b35-4772-a19c-8972761deaf2)

## Flow Chart
## Code
```.py

def doors_after_N_students(num_doors):
    open_doors = []
    count = 0
    for door in range(1, num_doors + 1):
        sqrt = 1
        while sqrt * sqrt < door:
            sqrt += 1
        if sqrt * sqrt == door:
            open_doors.append(door)
            count += 1

    return open_doors, count


#Test:
num_doors = 100
open_doors_after_N, count = doors_after_N_students(num_doors)
print(f"The number of open doors: {count}. Open doors after {num_doors} students: {open_doors_after_N}")

```
## Proof of work
![image](https://github.com/user-attachments/assets/c478b2e1-9c25-4fb7-9d81-1ee085763332)

