#Game Frog World

class Frog:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self,obstacle):
        act = obstacle.action()

        msg = f'żaba {self} spotyka {obstacle} i {act}!'
        print(msg)

class Bug:
    def __str__(self):
        return 'robaka'

    def action(self):
        return 'zjada go'

class FrogWorld:
    def __init__(self,name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t ________________ Frog World ________________'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


# Game Warlock World

class Warlock:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        act = obstacle.action()

        msg = f'Czarnoksiężnik {self} spotyka {obstacle} i {act}!'
        print(msg)


class Ork:
    def __str__(self):
        return 'złego orka'

    def action(self):
        return 'masakruje go'


class WarlockWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t ________________ Warlock World ________________'

    def make_character(self):
        return Warlock(self.player_name)

    def make_obstacle(self):
        return Ork()

#Game environmemnt

class GameEnvironment:
    def __init__(self,factory):
        self.hero  = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input(f'Witaj {name}. Ile masz lat? ')
        age = int(age)
    except ValueError as err:
        print(f'Wiek {age} jest niewłaściwy. proszę spróbuj ponownie....')
        return (False,age)
    return (True,age)

def main():
    name = input("Witaj! Jak masz na imię? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)

    game = FrogWorld if age < 14 else WarlockWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()

