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
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return 2025 - self.year

    def is_vintage(self):
        return self.get_age() >= 50