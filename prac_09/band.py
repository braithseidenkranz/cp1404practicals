
class Band:
    """Band Class"""
    def __init__(self, name=""):
        """Construct a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musicians_string = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing."""
        return "\n".join(musician.play() for musician in self.musicians)