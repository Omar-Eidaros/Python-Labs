import json
import re

def deleteproject(mail:str):
    filename = "projectsdb.json"
    p = 0
    userprojects = []
    required = []
    with open(filename, 'r') as file:
        data = list(json.load(file))

    print("----------------------- Your Projects -----------------------")
    for i in range(len(data)):
        if re.match(mail, data[i]["Owner"]):
            p += 1
            print(f"        Project No.{p}")
            print(f"Title:", data[i]["Title"])
            userprojects.append(data[i])
    print("")
    if len(userprojects):
        protitle = input("Enter project title required to edit: ")
        print("")

        for i in range(len(userprojects)):
            if re.match(protitle, userprojects[i]["Title"]):
               required = dict(userprojects[i])

        for i in range(len(data)):
            if re.match(required["Title"], data[i]["Title"]):
                data.pop(i)

        with open(filename, 'w') as file:
            json.dump(data, file)
    else:
        print("There is no projects for you !!")