import json
from AuthenticationSystem import ValidationMethods as vm

def register():
    user = {}

    fname = input("Enter your First Name: ")
    user.update({"First Name ": fname})
    lname = input("Enter your Last Name: ")
    user.update({"Last Name ": lname})
    mail = input("Enter your E-mail: ")
    user.update({"E-mail" : vm.checkmail(mail)})
    passwd = input("Enter your Password: ")
    password = vm.checkpassword(passwd)
    user.update({"Password" : password})
    cpassword = input("Confirm Password: ")
    vm.confirmpassword(password,cpassword)
    phone = input("Enter your Mobile: ")
    user.update({"Phone":vm.checkphone(phone)})

    filename = "usersdb.json"

    with open(filename,'r') as file:
            data = json.load(file)

    data.append(user)

    with open(filename, 'w') as file:
        json.dump(data,file)
        print("Registeration Done Successfuly ^___^")
