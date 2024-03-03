from abc import ABCMeta, abstractmethod

class Ghost(metaclass=ABCMeta):
    
    def __init__(self) -> None:
        print("Why not?")
    
    @abstractmethod
    def boo(self):
        print("Boo!")

class Poltergeist(Ghost):

    def boo(self):
        super().boo()


if __name__ == "__main__":
    casper = Poltergeist()
    casper.boo()
    ghost = Ghost()
    ghost.boo()
