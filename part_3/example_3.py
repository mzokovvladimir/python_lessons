class Car:
    count = 0

    def __init__(self, speed: int, color: str, weight: int) -> None:
        self.speed = speed
        self.color = color
        self.weight = weight
        Car.count += 1

    def __str__(self) -> str:
        return f'{self.color} {self.weight} {self.speed}'

    def __repr__(self):
        return self.__str__()


my_car1 = Car(50, 'red', 1700)
my_car2 = Car(100, 'white', 2100)
print(my_car1)
my_list = []
my_list.append(my_car1)
my_list.append(my_car2)
print(my_list)
print(Car.count)
