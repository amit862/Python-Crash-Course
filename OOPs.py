class Employee:
    def __int__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        print(self.salary)


rohan = Employee("Rohan", "3455")
# print(rohan.salary)
# print(rohan.name)
rohan.getSalary()

Amit= Employee("Amit", "100000")
# print(rohan.salary)
# print(rohan.name)
Amit.getSalary()