# This code demonstrates polymorphism in Python using a base class and multiple subclasses.
# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

# Subclass 1
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

# Subclass 2
class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

# Subclass 3
class Boat(Vehicle):
    def move(self):
        print("Sailing on the water 🚢")

# Test polymorphism
def describe_movement(vehicle):
    vehicle.move()

if __name__ == "__main__":
    car = Car()
    plane = Plane()
    boat = Boat()

    # Polymorphism in action
    describe_movement(car)
    describe_movement(plane)
    describe_movement(boat)
