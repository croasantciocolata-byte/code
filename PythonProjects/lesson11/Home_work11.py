# You are designing a system to manage different types of vehicles. 
# All vehicles have some things in common, like a name and speed, but each type of vehicle behaves a bit differently. 
# For example, a train might run on tracks, while a car drives on roads.

# 1. Create a parent class called Vehicle
# Attributes:
# name (e.g. "Express 2000", "Toyota")
# speed (in km/h)
# Methods:
# describe() – returns a string like: "Vehicle name: Express 2000, Speed: 120 km/h"
# move() – returns "Moving..." (this will be overridden later)

# 2. Create two child classes: Car and Train
# Each should:
# Inherit from Vehicle
# Call super().__init__() to reuse the parent constructor. Add a new attribute: fuel_type (e.g. "Petrol", "Electric")
# Override the move() method:
# Car: returns "Driving on roads"
# Train: returns "Running on tracks"
# Add a __str__() method to each class to make it easy to print the object.


# 3. Extension ideas:
# Add a method max_travel_time(distance) to calculate time to travel a given distance.
# Create a method refuel() in Car and schedule() in Train.

class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    def move(self):
        return "Moving: "
    def describe(self):
        return f"Vehicle: {self.name}; Speed: {self.speed}km/h"

class Train(Vehicle):
    def __init__ (self, name, speed, moving):
        super().__init__(name, speed)
        self.moving = moving

    def move(self):
        return "Running on tracks"
    
    def max_travel_time(self, distance):
        return distance / self.speed
    
    def schedule(self):
        return f"{self.name} is on schedule"
    
    def __str__(self):
        return f"Vehicle: {self.name}; Speed: {self.speed}km/h"

    
    
class Car(Vehicle):
    def __init__ (self, name, speed, moving):
        super().__init__(name, speed)
        self.moving = moving

    def move(self):
        return "Driving on roads"
    
    def max_travel_time(self, distance):
        return distance / self.speed
    
    def refuel(self):
        return f"{self.name} is refuiling"
    
    def __str__(self):
        return f"Vehicle: {self.name}; Speed: {self.speed}km/h"
    
vehicle1 = Train("train", 300, "jvfn")
vehicle2 = Car("Lambourghini", 160, "jfvfdjvjf")
print(vehicle1)
print(vehicle1.move())
print("Time: ", vehicle1.max_travel_time(800), "hours")
print(vehicle1.schedule())

print(vehicle2)
print(vehicle2.move())
print("Time: ", vehicle1.max_travel_time(600), "hours")
print(vehicle2.refuel())