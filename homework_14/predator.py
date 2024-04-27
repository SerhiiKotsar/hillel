from homework_14.mammal import Mammal


class Predator(Mammal):

    def __init__(self, species, fur_color, prey):
        super().__init__(species, fur_color)
        self._prey = prey

    def hunt(self):
        return f'I am a {self._species} predator hunting {self._prey}'
