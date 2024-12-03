class Sistema:

    def __init__(self):
        
        self.__argomenti = []
        
    def __get_argomenti(self):

        return self.__argomenti
    
    def __set_argomenti(self, args):

        self.__argomenti.extend(args)

    def aggiungi_elementi(self, *args):

        args = list(args)
        self.__set_argomenti(args)

    def stampa(self):

        print(self.__get_argomenti())

    def stampa_senza_ripetizioni(self):

        argomenti = set(self.__get_argomenti())

        print(argomenti)



sistema = Sistema()

sistema.aggiungi_elementi(5,"ciao","ciao",8,"otto",True, False, True, 5)

sistema.stampa()

sistema.stampa_senza_ripetizioni()