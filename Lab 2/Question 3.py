"""
Write a function which has an input of a string from user then it
will return the same string reversed.
"""
def reverseInputFunction():
    var = input("Please Enter a text: ")
    rev = ""
    for x in var:
        rev = x + rev

    return rev

print(reverseInputFunction())