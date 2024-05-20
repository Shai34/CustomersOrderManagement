from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def __init__(self, legs: int):
        self.__legs = legs

    @property
    def legs(self):
        return self.__legs

    def walk(self):
        print("Animal walking")

    def eat(self):
        print("Animal eating")
