# Quiz 011

## Paper Solution
![image](https://github.com/user-attachments/assets/70e2fd9d-1be1-40d7-8595-1ffa3f38a74a)

## Flow Chart
![image](https://github.com/user-attachments/assets/2c9d258a-4c79-46b1-b900-cc9f1dd0127c)
![image](https://github.com/user-attachments/assets/6b9da864-f7e5-4cf3-88ec-1bb9c902c3f4)

## Code
```.py
def show_days_in_month(month_name):
    month_days = {
        "January": 31,
        "February": 29, #2024 is a leap yr
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    starting_weekday = 0  # Monday
    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    weekday_map = {0: "Mo", 1: "Tu", 2: "We", 3: "Th", 4: "Fr", 5: "Sa", 6: "Su"}

    if month_name not in month_days:
        return "Invalid month name."
    month_index = month_order.index(month_name)
    current_starting_day = starting_weekday
    for i in range(month_index):
        current_starting_day = (current_starting_day + month_days[month_order[i]]) % 7

    num_days = month_days[month_name]
    output = []
    for day in range(1, num_days + 1):
        current_weekday = (current_starting_day + (day - 1)) % 7
        output.append(f"{weekday_map[current_weekday]} {day}")


    return '  '.join(output)

#Test
print(show_days_in_month("October"))

```
## Proof of work
![image](https://github.com/user-attachments/assets/4de9475a-614f-493a-8b22-b0c8282b6033)

