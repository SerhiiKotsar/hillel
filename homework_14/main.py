from homework_14.mammal import Mammal
from homework_14.predator import Predator

if __name__ == '__main__':
    lion = Predator(species='Lion', fur_color='yellow', prey='deer')
    print(lion.description())
    print(lion.hunt())
