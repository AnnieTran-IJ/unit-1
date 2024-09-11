![image](https://github.com/user-attachments/assets/6bc8eb26-f29e-44d6-8b63-f7faf99e50cf)# Quiz 008

## Paper Solution
![image](https://github.com/user-attachments/assets/3fd266e5-4e99-4a2e-aff6-b0c4d7c45ca7)


## Flow Chart
## Code
```.py
def room_name(room_order):
    floor = (room_order - 1) // 10 + 1  # Determine which floor the room is on
    room_on_floor = (room_order - 1) % 10 + 1  # Determine the room number on that floor
    return f"{floor}F{room_on_floor:02d}"  # :02d ensures room number is two digits


# Test
for i in range(3):
    room_order = int(input("What is the order of your room: "))
    print(room_name(room_order))
```
## Proof of work
![image](https://github.com/user-attachments/assets/f3da1c6b-2798-4299-8e21-0a55784f9d01)

