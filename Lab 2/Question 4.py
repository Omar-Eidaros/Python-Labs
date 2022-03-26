"""
Ask the user for his name then confirm that he has entered his
name(not an empty string/integers). then proceed to ask him for
his email and print all this data
(Bonus) check if it is a valid emailor not
"""
import re

def infoaskfunction():
    info = {}
    regex = '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'
    name = input("Enter your Name: ")
    while True:
        if name == "" or name.isnumeric():
            print("Invalid Name !!")
            name = input("ReEnter you Name: ")
        else:
            print("Valid Name")
            break
    email = input("Enter your Email: ")
    while True:
        if (re.search(regex,email)):
            print("Valid Email ")
            break
        else:
            print("Invalid Email !!")
            email = input("ReEnter you Email: ")
    info["name"] = name
    info["E-mail"] = email
    return print(f"Your Info : {info}")

infoaskfunction()


