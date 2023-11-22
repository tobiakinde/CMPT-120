class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    def __innit__(self, carrot, vanilla, strawberry):
        self.carrot = carrot
        self.vanilla = vanilla
        self.strawberry = strawberry


class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        
    #create your own function! what do you want it to do?
    def carGuess(self):
        if self.model == "fancy":
            return("Range Rover")
        else:
            return("Hondo")

   
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    newDog = Dog("clearance" , 5)
    print(newDog.name, newDog.age)

    newEmployee = Employee("richard", "Head Manager")
    # Print out each variable from newEmployee
    print(newEmployee.name, newEmployee.position)

    # Create and print out a cake
    myCake = Cake("vanilla", 2)
    print(f"Cake flavor: {myCake.flavor}, Layers: {myCake.layers}")

    # Create another cake and print it out
    anotherCake = Cake("chocolate", 3)
    print(f"Cake flavor: {anotherCake.flavor}, Layers: {anotherCake.layers}")

    # Create a cat
    cat1 = Cat("melissa")
    # Create another cat
    cat2 = Cat("lucian")

    # Print out the result of breedGuess for cat1
    print(cat1.breed)

    # Create a car
    myCar = Car("tesla", "model y")
    # Print out the make and model of the car
    print(f"Car: {myCar.make} {myCar.model}")



    main()

