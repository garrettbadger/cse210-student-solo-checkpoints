import random

# TODO: Define the Hider class here

class Hider:


    def __init__(self):
        self.location = random.randint(1, 1000)
        self.distance = [0, 0]

    def get_hint(self):
        hint = "Come and find me!"
        if self.distance[-1] == 0:
            hint = "You found me!"
        elif self.distance[-1] > self.distance[-2]:
            hint = "You are getting colder!"
        elif self.distance[-1] < self.distance[-2]:
            hint = "You are getting warmer!"
        
        return hint


    def watch(self, location):
        distance = abs(self.location - location)
        self.distance.append(distance)

