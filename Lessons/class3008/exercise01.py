base = input("Enter a number from 2 -> 10: ")

for digit in base:
    if digit not in '0123456789':
        print("Please enter a number from 2 -> 10")
        exit()

base_safe = int(base)
#1st attempt (it works)
# for i in range(101):
#     lst = []
#     for i in range(0,base_safe+1):
#         lst.append(str(i))
#     print(",".join(lst))

#2nd attempt(kind of similar to the first attempt):
# count=0
# for num in range(0,99):
#     print(count)
#     count += 1
#     if count == base_safe:
#         count = 0

for num in range(0,99):
    print(num%base_safe)


