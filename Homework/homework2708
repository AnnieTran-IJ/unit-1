#1. Create a program that organizes from largest to smallest three heights in cms entered by the user.
height_1 = int(input("Please enter the height of student A: "))
height_2 = int(input("Please enter the height of student B: "))
height_3 = int(input("Please enter the height of student C: "))

if height_1 >= height_2 and height_1 >= height_3:
    if height_2 >= height_3:
        print(f"Heights in order from highest to lowest: {height_1}, {height_2}, {height_3}")
    else:
        print(f"Heights in order from highest to lowest: {height_1}, {height_3}, {height_2}")

if height_2 >= height_1 and height_2 >= height_3:
    if height_1 >= height_3:
        print(f"Heights in order from highest to lowest: {height_2}, {height_1}, {height_3}")
    else:
        print(f"Heights in order from highest to lowest: {height_2}, {height_3}, {height_1}")

if height_3 >= height_1 and height_3 >= height_2:
    if height_1 >= height_2:
        print(f"Heights in order from highest to lowest: {height_3}, {height_1}, {height_2}")
    else:
        print(f"Heights in order from highest to lowest: {height_3}, {height_2}, {height_1}")


#2. Create a program that calculates the tax for a salary entered by the user following the table below
salary = int(input("Enter your salary: "))
if  0 <= salary >= 10000:
    print(f"Your tax rate is: 5%, which is ${salary*0.05}")
if  10001 <= salary >= 50000:
    print(f"Your tax rate is: 10%, which is ${salary*0.1}")
if  50001 <= salary >= 50000:
    print(f"Your tax rate is: 10%, which is ${salary*0.15}")
else: print(f"Your tax rate is: 10%, which is ${salary*0.25}")

#3. Write a program to sort alphabetically three names entered by the user. Note: Assume that only the first letter of names are the same.
name_1 = input("Please enter the 1st name: ")
name_2 = input("Please enter the 2nd name: ")
name_3 = input("Please enter the 3rd name: ")

if name_1 <= name_2 and name_1 <= name_3:
    if name_2 <= name_3:
        print(f"Names in alphabetical order: {name_1}, {name_2}, {name_3}")
    else:
        print(f"Names in alphabetical order: {name_1}, {name_3}, {name_2}")
elif name_2 <= name_1 and name_2 <= name_3:
    if name_1 <= name_3:
        print(f"Names in alphabetical order: {name_2}, {name_1}, {name_3}")
    else:
        print(f"Names in alphabetical order: {name_2}, {name_3}, {name_1}")
else:
    if name_1 <= name_2:
        print(f"Names in alphabetical order: {name_3}, {name_1}, {name_2}")
    else:
        print(f"Names in alphabetical order: {name_3}, {name_2}, {name_1}")
#4. Create a program that calculates the median for a series of scores entered by the user. The user enters either 4 or 5 scores.
score = list(map(int, input("Enter your 4-5 scores: ").split()))
# map(function, range): it will apply the same function for every element of a list/set.
# -> in this case, I'm trying to make every scores into an integer
score.sort() #highest to lowest
if len(score) == 5:
    print(f"The median of the score is: {score[2]}")
elif len(score) == 4:
    print(f"The median of the score is: {(score[1]+score[2])/2}")


