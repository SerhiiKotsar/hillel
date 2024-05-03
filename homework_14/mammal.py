from homework_14.animal import Animal


class Mammal(Animal):

    def __init__(self, species, fur_color):
        super().__init__(species)
        self._fur_color = fur_color

    def description(self):
        return f'I am a {self._species} mammal with {self._fur_color} fur'
