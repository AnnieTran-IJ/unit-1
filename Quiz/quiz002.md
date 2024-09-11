# Quiz 002
![image](https://github.com/user-attachments/assets/53704c7f-0378-4c59-9c34-48b3fbb53c68)
## Paper Solution
![image](https://github.com/user-attachments/assets/ad8e518b-5d9c-46e4-9ed7-a6710dd176e2)

## Code
```.py
#Quiz:
for i in range(4):
    first_num = int(input("Please enter your 1st number: "))
    second_num = int(input("Please enter your 2nd number: "))
    if first_num == 20 or second_num == 20 or first_num + second_num == 20:
        print("True")
    else:
        print("False")


#HL part:
list_A = input("Please enter 4 numbers for list A: ").split(',') #split by a comma
list_B = input("Please enter 4 numbers for list B: ").split(',')

#input by default is in string type -> need to be changed to integers.
list_A_integers = []
for num in list_A: #loop through each of the number
    num_as_int = int(num)
    list_A_integers.append(num_as_int) # temporarily create a new list for storage
list_A = list_A_integers #merge 2 in 1

list_B_integers = []
for num in list_B:
    num_as_int = int(num)
    list_B_integers.append(num_as_int)
list_B = list_B_integers

#processing...
for i in range(len(list_A_integers)):
    num1 = list_A_integers[i] #to pair up the number
    num2 = list_B_integers[i]

    if num1 == 20 or num2 == 20 or num1 + num2 == 20:
        print("True")
    else:
        print("False")
```
## Proof of work
![image](https://github.com/user-attachments/assets/9aa3188f-417d-40a2-8ece-fcc602e24d6e)

