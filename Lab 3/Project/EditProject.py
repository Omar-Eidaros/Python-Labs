import re
import json
from Project import Validationmethods as vm

def editproject(mail:str):
    filename = "projectsdb.json"
    p = 0
    userprojects = []
    required = []
    with open(filename, 'r') as file:
        data = json.load(file)
    print("----------------------- Your Projects -----------------------")
    for i in range(len(data)):
        if re.match(mail,data[i]["Owner"]):
            p += 1
            print(f"        Project No.{p}")
            print(f"Title:", data[i]["Title"])
            userprojects.append(data[i])
    print("")
    protitle = input("Enter project title required to edit: ")
    print("")
    for i in range(len(userprojects)):
        if re.match(protitle, userprojects[i]["Title"]):
            for j in userprojects[i]:
                print(f"{j}:", userprojects[i][j])
                required = dict(userprojects[i])

    print("- Press(1) to edit Details")
    print("- Press(2) to edit Total Target")
    print("- Press(3) to edit StartDate")
    print("- Press(4) to edit EndDate")
    print("- Press(0) to Exit")
    while True:
        num = int(input(" --> "))
        if num == 1:
            d = input("Enter The New Details: ")
            required['Details']= d
            print("Updated Successfully!")
            continue
        if num == 2:
            tt = input("Enter The New Total Target: ")
            required["Total Target"] = tt
            print("Updated Successfully!")
            continue
        if num == 3:
            sd = input("Enter The New StartDate: ")
            required["Start Date"] = vm.checkdate(sd)
            print("Updated Successfully!")
            continue
        if num == 4:
            ed = input("Enter The New EndDate: ")
            required["End Date"] = vm.checkdate(ed)
            print("Updated Successfully!")
            continue
        if num == 0:
            break

    print(required)
    for i in range(len(data)):
        if re.match(protitle, data[i]["Title"]):
            data[i] = required
            with open(filename, 'w') as file:
                json.dump(data, file)