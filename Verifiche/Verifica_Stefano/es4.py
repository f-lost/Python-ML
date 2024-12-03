class Autofficina:

    def __init__(self, nome):

        self.nome = nome

    def ripara(self, oggetto):
        pass

class OfficinaAuto(Autofficina):

    def __init__(self, nome):

        super().__init__(nome)

    def ripara(self, oggetto):
        
        if oggetto.__class__.__name__ == "Auto":

            print("Sto aggiustando la moto")
        
        else:

            print("Vai in un'altra officina!")
    

class OfficinaMoto(Autofficina):

    def __init__(self, nome):

        super().__init__(nome)

    def ripara(self, oggetto):
        
        if oggetto.__class__.__name__ == "Moto":

            print("Sto aggiustando la moto")
        
        else:

            print("Vai in un'altra officina!")


class Veicolo:

    def __init__(self, marca, modello):

        self.marca = marca
        self.modello = modello


class Auto(Veicolo):

    def __init__(self, marca, modello):

        super().__init__(marca, modello)


class Moto(Veicolo):

    def __init__(self, marca, modello):

        super().__init__(marca, modello)



class App_Riparazioni:

    def ripara(self, officina, a):
        
        if isinstance(a, Moto) and isinstance(officina, OfficinaMoto):
            officina.ripara(a)
        elif isinstance(a, Auto) and isinstance(officina, OfficinaAuto):
            officina.ripara(a)
        else:
            print("Vai in un'altra officina!")  






