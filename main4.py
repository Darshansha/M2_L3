string = input("Please enter a word:")
char = input("PLease enter a character:")
i = 0
count = 0
while (i < len(string)):
    if(string[i] == char):
        count = count + 1
    i = i + 1

print("\nThe total number of times", char, "has occured is", count)