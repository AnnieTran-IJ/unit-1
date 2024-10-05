# Quiz 010

## Paper Solution
![image](https://github.com/user-attachments/assets/660e1e48-f50c-459f-bfd0-2b8d67bde9e8)

## Flow Chart
![image](https://github.com/user-attachments/assets/3fba69a2-fef4-4beb-9f2a-053392a7d9f4)

## Code
```.py
def powersTen_final(value):
    if value == 0:
        return "0"

    value_str = f"{value:,.12f}"
    integer_part, decimal_part = value_str.split(".")

    decimal_part = decimal_part.rstrip('0') #rstrip is to remove trailing zero

    if decimal_part:
        return f"{integer_part}." + decimal_part
    else:
        return integer_part


def powers_of_ten(input_value):
    units = [
        (15, "Tera"),
        (12, "Giga"),
        (9, "Mega"),
        (6, "kilo"),
        (3, "unit"),
        (-3, "mili"),
        (-6, "micro"),
        (-9, "nano"),
        (-12, "pico")
    ]

    output_lines = []

    for power, unit in units:
        converted_value = input_value * (10 ** power)

        formatted_value = powersTen_final(converted_value)

        output_lines.append(f"{formatted_value:<20} {unit}")

    return '\n'.join(output_lines)


#Test
input_value = 1
print(powers_of_ten(input_value))
```
## Proof of work
![image](https://github.com/user-attachments/assets/45c8f922-2fa7-4cb3-a525-a09af4f82617)

