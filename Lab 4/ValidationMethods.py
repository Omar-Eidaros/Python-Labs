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

def checkhealthpoints(num:int):
    if (num > 0) and (num <= 100):
        return num
    else:
        raise Exception("Invalid Number")

def checksalary(num:int):
    if num >= 1000:
        return num
    else:
        raise Exception("Salary is below the required")

def checkvelocity(num:int):
    if (num >= 0) and (num <= 200):
        return num
    else:
        raise Exception("Invalid Number")

def checkfuelrate(num:int):
    if (num >= 0) and (num <= 100):
        return num
    else:
        raise Exception("Invalid Number")