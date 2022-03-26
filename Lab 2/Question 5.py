"""
Write a function that takes a string and prints the
longest alphabetical ordered substring occurred For example, if
the string is ' abdulrahman ' then the output Longest substring in
alphabetical order is: abdu

"""

def longeststring():
    text = input("Enter the text: ")
    longest = text[0]
    current = text[0]
    for x in text[1:]:
        if x >= current[-1]:
            current += x
            if len(current) > len(longest):
                longest = current
        else:
            current = x
    print(text)
    print (f"Longest substring in alphabetical order is: {longest}")

longeststring()