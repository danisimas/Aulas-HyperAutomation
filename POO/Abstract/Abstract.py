from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(cls):
        pass



class Dog(Animal):
   
    def make_sound(cls):
        return "Woof!"

class Cat(Animal):
    def make_sound(cls):
        return "Meow!"

# Create instances of Dog and Cat

dog = Dog()
cat = Cat()

# Call the make_sound method for each animal

print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
