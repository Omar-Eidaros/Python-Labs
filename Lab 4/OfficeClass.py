import json
import re

from PersonClass import Person
from CarClass import Car
from Employee import Employee
import ValidationMethods as vm

class Office():
    employeesNumber = 0
    def __init__(self,name:str,worktime:int):
        self.name = name
        self.worktime = worktime

    def hire(self):

        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        mail = vm.checkmail(input("Enter Mail: "))
        money = int(input("Enter Money: "))
        mode = input("Enter Mode: ")
        hrate = vm.checkhealthpoints(int(input("Enter HealthRate: ")))
        salary = vm.checksalary(int(input("Enter Salary: ")))
        carName = input("Enter Car Name: ")
        frate = vm.checkfuelrate(int(input("Enter Car's Fuelrate: ")))
        dis = int(input("Enter Distance to Work in KM: "))

        Emp = Employee(id,name,mail,money,mode,hrate,salary,Car(carName,frate),dis)

        filename = "OfficeDB.json"
        global odata
        odata = []
        with open(filename,'r') as file:
            odata = json.load(file)

        odata.append(Emp.to_dict())

        with open(filename,'w') as file:
            json.dump(odata,file)

        Office.employeesNumber += 1

    def get_all_employees(self):
        filename = "OfficeDB.json"
        with open(filename, 'r') as file:
            data = json.load(file)
        print("----------------------- Employees -----------------------")
        for i in range(len(data)):
            print(f"        Employee No.{i + 1}")
            for j in data[i]:
                print(f"{j}:", data[i][j])
            print("")

    def get_employee(self,id:int):
        filename = "OfficeDB.json"
        with open(filename, 'r') as file:
            data = json.load(file)
        for i in range(len(data)):
            if re.match(str(id),str(data[i]["id"])):
                for j in data[i]:
                    print(f"{j}:", data[i][j])

    def fire(self,id:int):
        filename = "OfficeDB.json"
        global odata
        odata = []
        with open(filename, 'r') as file:
            odata = json.load(file)
        print(len(odata))

        for i in range(len(odata)):
            if re.match(str(id),str(odata[i]["id"])):
                odata.pop(i)
                with open(filename, 'w') as file:
                    json.dump(odata, file)
            else:
                print("No Employee with this ID had founded")
        Office.employeesNumber -= 1

    def calculate_lateness(self,move_hour:float,velocity:float,dis:int):
        if dis != 0:
            time = dis / velocity
        else:
            raise Exception("Can't Divide on Zero ")

        arriving_hour = move_hour + time

        if (arriving_hour > self.worktime):
            print("Arrived late")
            return 0
        elif (arriving_hour == self.worktime):
            print("Arrived In Time ")
            return 2
        elif(arriving_hour < self.worktime):
            print("Arrived Early")
            return 1

    def deduct(self,id:int,deduction:int):
        filename = "OfficeDB.json"
        global odata
        odata = []
        with open(filename, 'r') as file:
            odata = json.load(file)

        for i in range(len(odata)):
            if re.match(str(id), str(odata[i]["id"])):
                odata[i]["salary"] -= deduction
                with open(filename, 'w') as file:
                    json.dump(odata, file)
                print("Deduction Done")
            else:
                print("No Employee with this ID had founded")

    def reward(self,id:int,reward:int):
        filename = "OfficeDB.json"
        global odata
        odata = []
        with open(filename, 'r') as file:
            odata = json.load(file)

        for i in range(len(odata)):
            if re.match(str(id), str(odata[i]["id"])):
                odata[i]["salary"] += reward
                with open(filename, 'w') as file:
                    json.dump(odata, file)
                print("Rewarding Done")
            else:
                print("No Employee with this ID had founded")

    def check_lateness(self,id:int,move_hour:float,velocity:float):

        filename = "OfficeDB.json"
        global odata
        odata = []
        with open(filename, 'r') as file:
            odata = json.load(file)

        for i in range(len(odata)):
            if re.match(str(id), str(odata[i]["id"])):
                Emp = Employee(odata[i]["id"],odata[i]["name"],odata[i]["email"],odata[i]["money"],odata[i]["mood"],odata[i]["health_rate"],odata[i]["salary"],Car(odata[i]["carname"],odata[i]["fuelrate"]),odata[i]["distanceToWork"])

        check = self.calculate_lateness(move_hour,velocity,Emp.distanceToWork)

        if check == 0:
            self.deduct(Emp.id,10)
        elif check == 1:
            self.reward(Emp.id,10)
        else:
            print("No Change Happened")

    @classmethod
    def change_emps_num(cls,num:int):
        cls.employeesNumber = num

ITI = Office("ITI",9)

ITI.check_lateness(1010,8.45,20)
print(Office.employeesNumber)