import ValidationMethods as vm
class Car:
    def __init__(self,name:str,fuelRate:int,velocity:int =0):
        self.name = name
        self.fuelRate = vm.checkfuelrate(fuelRate)
        self.velocity = vm.checkvelocity(velocity)

    def stop(self,dis:int):
        self.velocity = 0
        print(f"The Remaining Distance = {dis}")

    def run(self,Rvelocity:int,distance:int):
        self.velocity = Rvelocity
        ratio = distance / 10
        expected_distance = self.fuelRate

        if expected_distance > distance:
            self.fuelRate = self.fuelRate - (ratio * 10)
        elif expected_distance < distance:
            self.fuelRate = 0
            remaining_distance = distance - expected_distance
            self.stop(remaining_distance)