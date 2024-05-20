from Bonus.Animal import Animal
from Bonus.Pet import Pet
from overrides import overrides


class Cat(Animal, Pet):
    def __init__(self, name):
        super().__init__(4)
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def play(self):
        print("Cat playing")

    @overrides
    def eat(self):
        print("Cat walking")
