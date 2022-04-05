import re

def checkmail(email):
    regex = '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'
    while True:
        if email == "":
            email = input("Empty Input !!, ReEnter your Email: ")
            continue
        elif (re.search(regex,email)):
            break
        else:
            email = input("Invalid Input !!, ReEnter your Email: ")
            continue

    return email




