# OOP - Object Oriented Programming


class Dog:
    def __init__(self, breed, hair_length, legs=4,
                 criminal_record=None):  # Initialisation, dunder (double underscore) init
        self.animal_kind = "canine"
        self.legs = legs
        self.breed = breed
        self.criminal_record = criminal_record
        self.hair_length = self.set_hair_length(hair_length)
        print(self.bark())

    def set_hair_length(self, hair_length):
        if hair_length in ("short", "medium", "long"):
            return hair_length
        else:
            print("Hair Length must be short, medium or long.  Defaulting to medium.")
            return "medium"

    def loud_bark(self):
        return self.bark().upper()

    def bark(self):  # method
        return "Woof! I am a " + self.animal_kind


fido = Dog("Dalmatian", "short")  # Instantiation - i.e. creating an INSTANCE of a class
lassie = Dog("Collie", "yes", criminal_record="Arson")

print(lassie.legs)
