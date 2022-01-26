class Car:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.__speed = 0

    def accelerate(self, speed_increase):  # setters
        self.__speed = min(self.max_speed, self.__speed + speed_increase)

    def brake(self, speed_decrease):
        self.__speed = max(0, self.__speed - speed_decrease)

    def get_speed(self):  # getters
        return self.__speed


something_else = "This"

if __name__ == "__main__":
    car = Car(180)
    car.__speed = 30000
    print(car.get_speed())
    print(car)

print("Car Class __name__ is: " + __name__)
