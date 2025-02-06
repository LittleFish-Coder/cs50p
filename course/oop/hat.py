# @classmethod

import random

class Hat:
    houses = ["Gryffindoor", "Hufflepuff", "Ravenclas", "Slytherin"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(f"{name} is in {house}")

Hat.sort("Harry")