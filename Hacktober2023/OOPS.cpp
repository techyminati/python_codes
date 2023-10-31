#include <iostream>
#include <string>

// Encapsulation: Using classes to encapsulate data and methods
class Animal {
protected:
    std::string name;

public:
    Animal(const std::string& n) : name(n) {}

    virtual void speak() const {
        std::cout << "Animal speaks!" << std::endl;
    }

    void printName() const {
        std::cout << "Name: " << name << std::endl;
    }
};

// Inheritance: Creating a subclass to inherit properties from a base class
class Dog : public Animal {
public:
    Dog(const std::string& n) : Animal(n) {}

    void speak() const override {
        std::cout << "Dog barks!" << std::endl;
    }
};

// Polymorphism: Demonstrating method overriding and dynamic binding
void animalSpeak(const Animal& animal) {
    animal.speak();
}

int main() {
    // Abstraction: Creating objects and using them without needing to know their internal details
    Animal genericAnimal("Generic Animal");
    Dog myDog("Buddy");

    std::cout << "Using the Animal class:" << std::endl;
    genericAnimal.printName();
    animalSpeak(genericAnimal);

    std::cout << "\nUsing the Dog class:" << std::endl;
    myDog.printName();
    animalSpeak(myDog);

    return 0;
}
