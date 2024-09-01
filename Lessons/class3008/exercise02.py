width = int(input("Enter a number:"))
word = input("Enter a word:")
fill_character = input("Enter a character:")

n = len(word)
p = width - n
def justify():
    if p > 0:
        s = word
        for i in range(0,p-1):
            s = fill_character + s

        return s
    else:
        return word

# output = word.rjust(width, fill_character)
justify()
