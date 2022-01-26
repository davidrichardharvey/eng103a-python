# Inheritance and Polymorphism

class Mammal:
    def __init__(self, mammal_name):
        self.warm_blooded = True
        self.name = mammal_name

    def reproduce(self):
        print("Giving birth to live young")


class Platypus(Mammal):
    def __init__(self, name):
        super().__init__(name)
        self.poisonous_barbs = True
        # self.warm_blooded = False

    def reproduce(self):
        print("Laying eggs")


class Horse(Mammal):
    def __init__(self, horse_name, jockey):
        super().__init__(horse_name)
        self.legs = 4
        self.jockey = jockey

    def reproduce(self):  # Method Overriding
        print("Giving birth to live foals")


class Pony(Horse, Mammal):
    def __init__(self, pony_name, cuteness_rating=10):
        super().__init__(pony_name, None)
        self.cuteness_rating = cuteness_rating

    # def give_birth(self):  # Method Overloading
    #     super().reproduce()

    def give_birth(self, number_of_offspring=1):
        for i in range(number_of_offspring):
            super().reproduce()


