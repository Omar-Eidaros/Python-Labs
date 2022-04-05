import ValidationMethods as vm

class Person:
    moods = ("Happy","Tired","Lazy")
    def __init__(self,name:str,money:int,healthRate:int,mood=""):
        self.name = name
        self.mood = mood
        self.money = money
        self.h_rate = vm.checkhealthpoints(int(healthRate))

    def sleep(cls,num:int):
        global moods
        if num > 7 and num < 24:
            cls.mood = moods[2]
            print("Lazy")
        elif num == 7:
            cls.mood = moods[0]
            print("Happy")
        elif num < 7 and num < 24:
            cls.mood = moods[1]
            print("Tired")
        else:
            print("Invalid Value")

    def buy(cls,num:int):
        cls.money -= (num*10)
        if cls.money > 0:
            print("Still have a Credit")
        elif cls.money < 0:
            print("You Excced The Credit Limit")

    def eat(self,num:int):
        if num == 1 or num < 1:
            self.h_rate = 50
        elif num == 2:
            self.h_rate = 75
        elif num == 3 or (num > 3 and num < 6):
            self.h_rate = 100
        else:
            print("Invalid Number")
