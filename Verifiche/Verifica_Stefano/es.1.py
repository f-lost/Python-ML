class Esecutore:

    def __init__(self):

        self.numeri = []
        self.stringhe = []
        self.booleani = []
        self.altro = []

    def dividi(self, dato):

        if type(dato) == int or type(dato) == float:

            self.numeri.append(dato)

        elif type(dato) == str:
            
            self.stringhe.append(dato)
        
        elif type(dato) == bool:

            self.booleani.append(dato)
        
        else:

            print("Dato non basilare.")
            self.altro.append(dato)


    def stampa(self, n = 4):

        if n == 1:

            print(self.numeri)

        elif n == 2:

            print(self.stringhe)

        elif n == 3:

            print(self.booleani)

        elif n == 4:

            print(self.numeri)
            print(self.stringhe)
            print(self.booleani)

        else:

            print("Scelta non valida.")




#test

esecutore = Esecutore()

prove = [1, "ciao", True, 2, "stefano", False, 3, "S", True]

for prova in prove:

    esecutore.dividi(prova)

#n = int(input("Quale lista vuoi stampare?\n1)Lista di numeri\n2)Lista di stringhe\n3)Lista di booleani\n4)Tutte"))


for i in range(1,4):

    esecutore.stampa(i)

esecutore.stampa()