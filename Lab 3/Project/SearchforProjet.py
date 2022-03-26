from Project import Validationmethods as vm
import json
import re

def search(mail:str):
    filename = "projectsdb.json"
    userprojects = []

    with open(filename, 'r') as file:
        data = json.load(file)

    for i in range(len(data)):
        if re.match(mail, data[i]["Owner"]):
            userprojects.append(data[i])
    print("")

    userinput = input("Enter project Start/End Date: ")
    prodate = vm.checkdate(userinput)

    for i in range(len(userprojects)):
        if re.match(prodate,userprojects[i]["Start Date"]) or re.match(prodate,userprojects[i]["End Date"]):
            for j in userprojects[i]:
                print(f"{j}:", data[i][j])
        else:
            print("No projects founded with this date !!")
