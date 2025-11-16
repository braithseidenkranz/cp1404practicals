
from datetime import date


class Project:
    """Represents information about a project"""
    def __init__(self, name, start_date, priority, cost, completion):
        """Initialises a project from the given information"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion


    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        """Returns a string representation of the project"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost}, completion {self.completion}%"

    def is_complete(self):
        """Returns true if the project is complete"""
        return self.completion == 100