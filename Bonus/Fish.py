from Bonus.Animal import Animal
from Bonus.Pet import Pet
from overrides import overrides


class Fish(Animal, Pet):
    def __init__(self):
        super().__init__(0)
        self.name = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def play(self):
        print("Fish playing")

    @overrides
    def walk(self):
        print("Fish walking")

    @overrides
    def eat(self):
        print("Fish eating")
