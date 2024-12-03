from abc import ABC, abstractmethod

class Professore:

    def __init__(self, nome, cognome, età):

        self.nome = nome
        self.cognome = cognome
        self.età = età

class Scienza(ABC):

    pass


class Storia(ABC):

    pass
