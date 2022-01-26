# class Location:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#
#     def __repr__(self):
#         return f"Location(latitude={self.latitude}, longitude={self.longitude})"
#
#     def __str__(self):
#         return f"({self.latitude}, {self.longitude})"
#
#
# bham_academy = Location(latitude=52.488647, longitude=-1.887249)
# print(repr(bham_academy))
# print(bham_academy)
#
# print(f"The Sparta Global Birmingham academy is located at co-ordinates {bham_academy}")


class Dog:
    def __init__(self, age):
        self.age = age

    def __repr__(self):
        return f"Dog(age={self.age})"

    def __str__(self):
        return f"A {self.age} year old Dog"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age * 7} dog-years old Dog"
        else:
            return self.__str__()


fido = Dog(5)
print(fido)
print(f"Fido is a {fido:dog}")

