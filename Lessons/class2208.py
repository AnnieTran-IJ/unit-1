
# name = input("Enter your name: ")
# print("Hi", name)
# print(f"hi {name}") #fstring to add variable without ending the quotation mark

lastname = str(input("Last name:"))
age = int(input("Age: "))
basemoney = int(input("Base money: "))
interest = float(input("Interest: "))

outcome = (1 + interest) ** age * basemoney
print(f"The amount money you have is: {outcome:.2f}") #:.2f to indicate round up to 2 decimal place

if outcome > 2*basemoney:
    print("#"*10)
    print("#"," "*8,"#")
    print(f"# 😊{outcome} #")
    print("#"," "*8,"#")
    print("#"*10)
else:
    print("🥹")


