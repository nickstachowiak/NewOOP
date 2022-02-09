import random

class Insect:

    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.length = 0

    def flight(self):
        self.wings = 2
        self.legs = 4
        self.length = 0
        self.length = random.randint(1,10)

    def get_length(self):
        return self.length



