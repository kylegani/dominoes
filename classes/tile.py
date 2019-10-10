class Tile:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def flip(self):
        temp_side2 = self.side1
        self.side1 = self.side2
        self.side2 = temp_side2
        return self

    def tally(self):
        return self.side1 - self.side2

    def eq(self, other):
        return self.side1 == other.side1 and self.side2 == other.side2
