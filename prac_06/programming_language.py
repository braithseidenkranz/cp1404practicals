
class ProgrammingLanguage:
    """Represents a Programming Language"""
    def __init__(self, name = "", typing = "", reflection = False, year = 0):
        """Initialises a ProgrammingLanguage instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns True if the language is dynamically typed"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"