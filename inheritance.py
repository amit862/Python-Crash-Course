##inheritance
## car class blueprint

class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype


    def driving(self):
        print("Car is used for driving")

class Audi(Car):
    def __init__(self,windows,doors,enginetype,horsepower):
        super().__init__(windows,doors,enginetype)
        self.horsepower=horsepower

    def selfdriving(self):
        print("It is a self driving car")

audiq7=Audi(4,5,"Diesel",200)

print(audiq7.horsepower)
print(audiq7.windows)
audiq7.driving()
audiq7.selfdriving()