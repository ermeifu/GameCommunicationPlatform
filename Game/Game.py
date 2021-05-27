from abc import ABCMeta, abstractmethod

class Game(metaclass=ABCMeta):

    @abstractmethod
    def play(self, command):
        pass


class Chess(Game):

    def __init__(self):
        self.name = 'Chess'

    def play(self, command):
        print(self.name + command)

class ChineseChess(Game):

    def __init__(self):
        self.name = 'ChineseChess'

    def play(self, command):
        print(self.name + command)

class FiveChess(Game):

    def __init__(self):
        self.name = 'FiveChess'

    def play(self, command):
        print(self.name + command)


class Mahjong(Game):

    def __init__(self):
        self.name = 'Mahjong'

    def play(self, command):
        print(self.name + command)

class Poker(Game):

    def __init__(self):
        self.name = 'Poker'

    def play(self, command):
        print(self.name + command)


class GameFactory(metaclass=ABCMeta):

    @abstractmethod
    def create(self):
        pass

class ChessFactory(GameFactory):

    def create(self):
        return Chess()

class ChineseChessFactory(GameFactory):

    def create(self):
        return ChineseChess()

class FiveChessFactory(GameFactory):

    def create(self):
        return FiveChess()

class MahjongFactory(GameFactory):

    def create(self):
        return Mahjong()

class PokerFactory(GameFactory):

    def create(self):
        return Poker()


if __name__ == '__main__':
    i = PokerFactory()
    j = i.create()
    j.play('poker')
