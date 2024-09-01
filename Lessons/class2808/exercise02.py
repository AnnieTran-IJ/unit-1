from numpy import number

print("Welcome to KidsMath!")
print("Menu: \n1. Show a multiplication table\n2. Show the factors\n3. Count up to a number by steps\n4. Find the interations to reduce a number")

lesson = input("Choose one activity you want to do: ")
if lesson not in "01234":
    print("Please enter a number from 1 - 4.")
    exit()

if lesson == "1":
    multiplication = int(input("Enter a number: "))
    for i in range(1, 10):
        print(f"{multiplication} x {i} = {i*multiplication}")

if lesson == "2":
    number_to_factor = int(input("Enter a number: "))
    for i in range(2, number_to_factor - 1):
        if number_to_factor % i == 0:
            print(f"{i} is the factor of {number_to_factor}")

if lesson == "3":
    end_number = int(input("Enter a ending number: "))
    step = int(input("Enter a step for your sequence: "))
    for i in range(1, end_number + 1,step):
        print(i)

if lesson == "4":
    count = 0
    number_for_iteration = input("Enter a number: ")
    if number_for_iteration < 10:
        print(number_for_iteration)
        count = 1
        print(count)
    if "0" in number_for_iteration:
        print("0")
        count = 1
        print(count)
    else:
        while number_for_iteration != "0" and len (number_for_iteration) != 1:
            print(f"{iteration*}")
            count += 1
        print 0


    # iteration = 0
    # while number_for_iteration > 0:
    #     iteration += number_for_iteration % 10
    #     number_for_iteration /= 10 #i = i/10 -> i \n


