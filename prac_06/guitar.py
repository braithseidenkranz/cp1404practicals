"""
Estimate: 5 mins
Actual: 5 mins
"""

class Guitar:
    """Represents a Guitar object"""
    def __init__(self, name ="", year: int = 0, cost: float = 0):
        """Initialises a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar based off the year 2025"""
        current_year = 2025
        return current_year - self.year

    def is_vintage(self):
        """Return True if the Guitar is vintage"""
        vintage_age = 50
        return self.get_age() >= vintage_age