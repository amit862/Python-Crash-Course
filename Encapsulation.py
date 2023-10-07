# ### Access Modifier --> Implement Encapsulation
#private

# class Person:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age


#     def display_info(self):
#         print(f"the person name is {self.__name} and the age is {self.__age}")

# person = Person("Amit",23)
# person.display_info()
        

### Access Modifier --> Implement Encapsulation
#protected

class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age


    def display_info(self):
        print(f"the person name is {self._name} and the age is {self._age}")

class Student:
    def __init__(self,name,age):
        super.__init__(name,age)

person = Person("Amit",23)
print(person._age)
# person.display_info()

student1 = Student("Amit",21)
print(student1._name)        