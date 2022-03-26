import re
import json

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

def checkpassword(passwd):
    while True:
        if 4 <= len(passwd) <= 16:
            break
        elif len(passwd) < 4:
            print("Too Short Password !!")
            passwd = input("ReEnter your Password: ")
            continue
        elif len(passwd) > 16:
            print("Too Long Password !!")
            passwd = input("ReEnter your Password: ")
            continue

    return passwd

def confirmpassword(passwd,cpasswd):
    if re.match(passwd,cpasswd):
        return cpasswd
    else:
        print("Not Matched !!")
        cpasswd = input("Confirm your Password: ")
        confirmpassword(passwd, cpasswd)

def checkphone(num:str):
    regex = "^01[0125][0-9]{8}$"
    while True:
        if num.isnumeric():
            if len(num) == 11:
                if re.match(regex,num):
                    break
                else:
                    print("Not an Egyption Number !!")
                    num = input("ReEnter your Mobile: ")
                    continue
            elif len(num) < 11 or len(num) > 11:
                print("Invalid Number !!")
                num = input("ReEnter your Mobile: ")
                continue
        else:
            print("Invalid Input !!, Number shouldn't contain characters !")
            num = input("ReEnter your Mobile: ")
            continue
    return num

def checklogin(mail:str,password:str):
    filename = "usersdb.json"
    with open(filename, 'r') as file:
        data = json.load(file)
    for lindex in range(len(data)):
        m = data[lindex]["E-mail"]
        p = data[lindex]["Password"]
        if re.match(mail,m) and re.match(password,p):
            return True
        else:
            continue
    print("Not Exist !!")
    return False
