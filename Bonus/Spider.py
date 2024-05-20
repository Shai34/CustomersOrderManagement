from Bonus.Animal import Animal
from overrides import overrides


class Spider(Animal):
    def __init__(self):
        super().__init__(8)

    @overrides
    def eat(self):
        print("Spider eating")
