"""
Write a program which repeatedly reads numbers until the user
enters “done”.
○ Once “done” is entered, print out the total, count, and average of the numbers.
○ If the user enters anything other than a number,
 detect their mistake, print an error message and skip to the next number.
"""

def readinput():
    numbers=[]
    while True:
        userinput = input("Please Enter a Number: ")
        if userinput.isnumeric():
            numbers.append(int(userinput))
        elif userinput == "Done" or userinput == "done":
            break
        else:
            print("Invalid value !!, Enter A New Number")
            continue

    return print(numbers), print(f"Total : {sum(numbers)}"), print(f"Lenght : {len(numbers)}"), print(f"Avrage : {sum(numbers) / len(numbers)}")

readinput()