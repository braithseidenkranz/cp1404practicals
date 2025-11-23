from prac_09.car import Car
from random import randint

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with reliability."""
        return f"{super().__str__()}, reliability={self.reliability}%"

    def drive(self, distance):
        """Drive like parent Car if random number is below reliability."""
        random_number = randint(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven