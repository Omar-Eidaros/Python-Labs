from AuthenticationSystem import ValidationMethods as vm

def login():
    Mail = input("Enter your E-mail: ")
    mail = vm.checkmail(Mail)
    passwd = input("Enter your Password: ")

    if vm.checklogin(mail,passwd):
        print("Successfully Login ^__^ \n")
        return True,mail
    else:
        print("\n Login Faild !!, Try again \n")
        return False,mail
