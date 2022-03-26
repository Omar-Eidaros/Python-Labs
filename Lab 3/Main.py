import AuthenticationSystem as aus
import Project as pro

def main():
    print("============== Welcome to Crowd Funding App ==============")
    while True:
        print("- Press(1) to Register")
        print("- Press(2) to Login")
        print("- Press(3) to Exit")
        choice = int(input("Enter a Number: "))
        if choice == 1:
            aus.register()
            continue
        elif choice == 2:
            ret = aus.login()
            if ret[0]:
                while True:
                    print(" ")
                    print("- Press(1) to Create New Project")
                    print("- Press(2) to Edit your Projects")
                    print("- Press(3) to View All Projects")
                    print("- Press(4) to Search in your Projects by Date")
                    print("- Press(5) to Delete a Project")
                    print("- Press(6) Exit")
                    print(" ")
                    num = int(input("Enter a Number: "))
                    print(" ")
                    if num == 1:
                        pro.createproject(ret[1])
                        continue
                    elif num == 2:
                        pro.editproject(ret[1])
                        continue
                    elif num == 3:
                        pro.viewprojects()
                        continue
                    elif num == 4:
                        pro.search(ret[1])
                        continue
                    elif num == 5:
                        pro.deleteproject(ret[1])
                        continue
                    elif num == 6:
                        break
                    else:
                        print("Wrong Entry!!, Try Again")
            else:
                continue
        elif choice == 3:
            print("See you Next Time ^__^")
            break
        else:
            print("Wrong Entry!!, Try Again")


main()