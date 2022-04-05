from PersonClass import Person
from CarClass import Car
import ValidationMethods as vm

class Employee(Person):
    work_behavour = ("Happy","Tired","Lazy")
    def __init__(self,id:int,name:str,email:str,money:int,mood:str,health_rate:int,salary:int,car:Car,dis_to_work:int):
        super(Employee,self).__init__(name,money,health_rate,mood)
        self.id = id
        self.email = vm.checkmail(email)
        self.salary = vm.checksalary(salary)
        self.car = car
        self.distanceToWork = dis_to_work
        self.evaluation = ""

    def work(self,num:int):
        global work_behavour
        if num > 8 and num < 24:
            self.evaluation = work_behavour[1]
            print("Tired")
        elif num == 8:
            self.evaluation = work_behavour[0]
            print("Happy")
        elif num < 8:
            self.evaluation = work_behavour[2]
            print("Lazy")
        else:
            print("Invalid Value")

    def to_dict(emp):
        if isinstance(emp,Employee):
            dict = {
                "id": emp.id,
                "name": emp.name,
                "email": emp.email,
                "money": emp.money,
                "mood": emp.mood,
                "health_rate": emp.h_rate,
                "salary": emp.salary,
                "carname": emp.car.name,
                "fuelrate": emp.car.fuelRate,
                "distanceToWork": emp.distanceToWork
            }
            return dict
        else:
            type_name = emp.__class__.__name__
            raise TypeError("Unexpected type {0}".format(type_name))

    def sendemail(self):
        email = self.email
        send_to = vm.checkmail(input("Send To: "))
        subject = input("Subject: ")
        rx_name = input("Recepiant Name: ")
        mail_body = input("Mail Body: ")
        final_mail = f"From:{email} \n" \
                     f"To:{send_to}\n" \
                     f"Subject: {subject} \n\n" \
                     f"Hi {rx_name},\n" \
                     f"{mail_body}\n" \
                     f"Thanks"

        mailfile = f"Mails\{rx_name}_mail_{subject}.txt"

        with open(mailfile, 'w') as mail:
            mail.write(final_mail)

    def refuel(self,amount:int):
        if (amount > 0) and (amount < 100):
            self.car.fuelRate += amount
            if self.car.fuelRate > 100:
                self.car.fuelRate = 100
            else:
                pass
        elif amount < 0:
            print("Invalid Input")
        elif amount > 100:
            self.car.fuelRate = 100

    def drive(self,dis:float,time:float):
        if time != 0:
            vel = dis / time
        else:
            raise Exception("Can't Divide on Zero ")
        self.car.run(vel,dis)

emp1 = Employee(1001,"Samir","samir@yahoo.com",1000,'Tired',90,6000,Car("Kia",100),60)