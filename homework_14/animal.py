from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def description(self):
        pass

    def __init__(self, species):
        self._species = species
