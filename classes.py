"""
#from cereal import car
class Car:
    def __init__(self, brand, colour, gearbox="manual"):
        self.brand = brand
        self.colour = colour
        self.gearbox = gearbox
        self.turned_on = False
        self.gear = "N"
    
    def start_engine(self):
        print("Starting the engine...")
        self.turned_on = True
    
    def stop_engine(self):
        print("Stopping the engine...")
        self.turned_on = False
        
    def select_gear(self, gear):
        self.gear = gear
        print("Changing gear to {}...".format(gear))
        
    def get_parameters(self):
        return {
            "brand": self.brand, 
            "colour": self.colour, 
            "gearbox": self.gearbox, 
            "engine": self.turned_on, 
            "gear": self.gear
        }    
    
first_car = Car(brand="Fiat", colour="Red", gearbox="automatic")
second_car = Car(brand="Ferrary", colour="White", gearbox="automatic")

print(first_car)
print("Brand:", first_car.brand)
print("Gearbox:", first_car.gearbox)
first_car.start_engine()
print("Running:", first_car.turned_on)
first_car.select_gear("1")
first_car.stop_engine()
print("Running:", first_car.turned_on)

car_parameters = first_car.get_parameters()
print(car_parameters)

#print(second_car)
#print("Brand:", second_car.brand)
#print("Gearbox:", second_car.gearbox)
"""

# EMPLOYEE CLASSES:
#print()
#print("*" * 50)
#print()

class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
        
    def describe(self):
        print(f"{self.name} earns {self.salary} and works as a {self.position}")
        
list_of_employees = []

while True:
    selection = input("Enter 'a' to add a new employee or 'q' to quit: ")
    if selection == "q":
        break
    elif selection == "a":
        name = input("Enter the name of the employee: ")
        salary = input("Enter the salary of the employee: ")
        position = input("Enter the position of the employee: ")
        
        new_employee = Employee(name=name, salary=salary, position=position)
        list_of_employees.append(new_employee)
        print("New employee added!")

        
print(list_of_employees)
print()
print()

for employee in list_of_employees:
    employee.describe()
        
# on terminal to execute this EMPLOYEE CLASSES and get the inputs from a text file "employees.txt"
# type on terminal: Get-Content employee.txt | python classes.py 