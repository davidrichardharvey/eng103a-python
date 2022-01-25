# OOP - Object Oriented Programming

class Dog:

    animal_kind = "canine"  # class variable

    def loud_bark(self):
        return self.bark().upper()

    def bark(self):  # method
        return "Woof! I am a " + self.animal_kind


fido = Dog()  # Instantiation - i.e. creating an INSTANCE of a class
lassie = Dog()
fido.animal_kind = "giraffe"
print(fido.animal_kind)
Dog.animal_kind = "arachnid"
print(fido.animal_kind)