class Vehicle:
    def __init__(self, name, speed, avg, capacity):
        self.name=name
        self.speed=speed
        self.avg=avg
        self.capacity = capacity

    def fare(self):
        return self.capacity*100

class Bus(Vehicle):
    pass

n=Vehicle('SchoolVolvo',200,8,11)

print('Fare is: ', n.fare())
print(f"The {n.name} has mileage of {n.avg} km/l runs with max speed of {n.speed} km/h. \nHas capacity of {n.capacity} passsenger!")


