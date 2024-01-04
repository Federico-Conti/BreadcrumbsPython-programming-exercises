class Person:
    first_name = "Name" # class field

    def int_cast(self,variable): #Exception
        try:
            return int(variable)
        except ValueError as e:
            print(f"The string {variable} is not numerical")


    def __init__(self, first_name, last_name, age): #constructor
        self.last_name = last_name # class field definitio and initialization
        self.age = self.int_cast(age) # call int_cast method
        Person.first_name = first_name # it is possible update for every class istance
        
    def printPersonInfo(self): #class method - self is the reference to the current instance
            print(f'First Name:{self.first_name} - Last Name:{self.last_name} - Age: {self.age}')
            
    def info(self):
            self.printPersonInfo()

                
person = Person("Federico","Conti","22") #call constructor
person.info()