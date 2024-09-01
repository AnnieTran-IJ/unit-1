num_unsafe = input("Enter a number: ")
#validate that the user a number. If not, it is a bad program!!
for letter in num_unsafe:
    if letter not in "0123456789":
        print("Please enter a number.")
        exit()
num = int(num_unsafe)

for i in range(2, num-1):
    if num % i == 0:
        print(f"{i} is the factor of {num}")


