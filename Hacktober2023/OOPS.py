# Encapsulation
class Car:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def display_info(self):
        print(f"Car: {self.__make} {self.__model}")


# Inheritance
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")


# Polymorphism
def car_information(car):
    car.display_info()


# Abstraction
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating objects and demonstrating OOP principles
my_car = Car("Toyota", "Camry")
my_electric_car = ElectricCar("Tesla", "Model S", 100)

print("Encapsulation:")
print(f"Car Make: {my_car.get_make()}")
print(f"Car Model: {my_car.get_model()}")

print("\nInheritance:")
my_electric_car.display_info()

print("\nPolymorphism:")
car_information(my_car)
car_information(my_electric_car)

print("\nAbstraction:")
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
