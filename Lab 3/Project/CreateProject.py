from Project import Validationmethods as vm
import json

def createproject(usermail:str):
    project = {}

    project.update({"Owner": usermail})
    title = input("Enter Project Title: ")
    project.update({"Title": title})
    decs = input("Enter Project Details: ")
    project.update({"Details": decs})
    fund = input("Enter Total Target: ")
    project.update({"Total Target": fund})
    sdate = input("Enter Start Date: ")
    project.update({"Start Date": vm.checkdate(sdate)})
    edate = input("Enter End Date: ")
    project.update({"End Date": vm.checkdate(edate)})

    filename = "projectsdb.json"

    with open(filename, 'r') as file:
        pdata = json.load(file)

    pdata.append(project)

    with open(filename, 'w') as file:
        json.dump(pdata, file)
        print("Project added Successfuly ^___^")

