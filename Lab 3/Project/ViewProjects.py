import json

def viewprojects():
    filename = "projectsdb.json"
    with open(filename, 'r') as file:
        data = json.load(file)
    print("----------------------- Projects -----------------------")
    for i in range(len(data)):
            print(f"        Project No.{i + 1}")
            for j in data[i]:
                print(f"{j}:", data[i][j])
            print("")