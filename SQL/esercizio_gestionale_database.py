import mysql.connector


class Menu:
    def __init__(self):
        """Inizializza il menu con una lista vuota di elementi."""
        self.__elementi = []  # Attributo privato per contenere gli elementi del menu
    
    def __get_elementi(self):
        """Restituisce gli elementi del menu."""
        return self.__elementi

    def __set_elementi(self, elementi):
        """Imposta gli elementi del menu, solo se è una lista."""
        if isinstance(elementi, list):
            self.__elementi = elementi
        else:
            raise TypeError("Elementi deve essere una lista di oggetti Elemento")

    def aggiungi_elemento(self, elemento):
        """Aggiunge un elemento al menu."""
        if isinstance(elemento, Elemento):
            self.__elementi.append(elemento)
        else:
            raise TypeError("L'elemento deve essere un'istanza della classe Elemento")

    def rimuovi_elemento(self, nome):
        """Rimuove un elemento dal menu in base al nome."""
        self.__elementi = [el for el in self.__elementi if el.get_nome() != nome]
    
    def mostra_menu(self):
        """Mostra e gestisce il menu in un ciclo fino a quando l'utente sceglie di uscire."""
        while True:
            print("\nMenu:")
            for i, elemento in enumerate(self.__elementi, start=1):
                print(f"{i}. {elemento.get_nome()}")
            print(f"{len(self.__elementi) + 1}. Esci")

            try:
                scelta = int(input("Seleziona il numero dell'opzione: "))
                
                if 1 <= scelta <= len(self.__elementi):
                    # Esegue l'azione selezionata
                    self.__elementi[scelta - 1].esegui_azione()
                elif scelta == len(self.__elementi) + 1:
                    # Esce dal menu
                    print("Uscita dal menu.")
                    break
                else:
                    print("Scelta non valida. Riprova.")
            except ValueError:
                print("Per favore, inserisci un numero valido.")


class Elemento:
    def __init__(self, nome, azione=None):
        """Inizializza l'elemento con un nome e un'azione."""
        self.__nome = nome  # Attributo privato
        self.__azione = azione  # Attributo privato
    
    def get_nome(self):
        """Restituisce il nome dell'elemento."""
        return self.__nome

    def set_nome(self, nome):
        """Imposta il nome dell'elemento, se è una stringa."""
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("Il nome deve essere una stringa")
    
    def esegui_azione(self):
        """Esegue l'azione associata a questo elemento."""
        if self.__azione:
            self.__azione.esegui()
        else:
            print(f"{self.__nome} non ha alcuna azione associata.")

    def get_azione(self):
        """Restituisce l'azione associata all'elemento."""
        return self.__azione

    def set_azione(self, azione):
        """Imposta l'azione associata all'elemento, se è un'istanza della classe Azione."""
        if isinstance(azione, Azione):
            self.__azione = azione
        else:
            raise TypeError("Azione deve essere un'istanza della classe Azione")


class Azione:
    def __init__(self, funzione):
        """Inizializza l'azione con una funzione."""
        self.__funzione = funzione  # Attributo privato
    
    def esegui(self):
        """Esegue la funzione associata all'azione."""
        if callable(self.__funzione):
            self.__funzione()
        else:
            raise ValueError("L'azione deve essere una funzione chiamabile")


# Definizione delle azioni per interagire con il database
def inserisci_studente():
    """Inserisce un nuovo studente nel database."""
    nome = input("Inserisci il nome dello studente: ").lower()
    cognome = input("Inserisci il cognome dello studente: ").lower()
    valore = (nome, cognome)
    query = "select id from studenti where nome = %s and cognome = %s"
    mycursor.execute(query, valore)
    studente = mycursor.fetchone()
    if studente:
        print("Studente già esistente.")
    else:
        query = "insert into studenti (nome, cognome) values (%s, %s)"
        mycursor.execute(query, valore)
        mydb.commit()
        print(f"Studente {nome} {cognome} inserito.")


def elimina_studente():
    """Elimina uno studente dal database."""
    nome = input("Inserisci il nome dello studente: ").lower()
    cognome = input("Inserisci il cognome dello studente: ").lower()
    valore = (nome, cognome)
    query = "select id from studenti where nome = %s and cognome = %s"
    mycursor.execute(query, valore)
    studente = mycursor.fetchone()
    if studente:
        query = "delete from studenti where nome = %s and cognome = %s"
        mycursor.execute(query, valore)
        mydb.commit()
        print(f"Studente {nome} {cognome} eliminato.")
    else:
        print("Studente non trovato.")


def modifica_voto():
    """Modifica il voto di uno studente."""
    nome = input("Inserisci il nome dello studente: ").lower()
    cognome = input("Inserisci il cognome dello studente: ").lower()
    valore = (nome, cognome)
    query = "select id from studenti where nome = %s and cognome = %s"
    mycursor.execute(query, valore)
    studente = mycursor.fetchone()
    if studente:
        materia = input("Inserisci la materia: ").lower()
        voto = float(input("Inserisci il voto: "))
        valore = (materia, voto, studente[0])
        query = "insert into voti (materia, voto, id) values (%s, %s, %s)"
        mycursor.execute(query, valore)
        mydb.commit()
        print("Voto inserito.")
    else:
        print("Studente non trovato.")


def stampa():
    """Stampa il registro completo di studenti e voti."""
    query = "select studenti.nome, studenti.cognome, voti.materia, voti.voto from studenti join voti on studenti.id = voti.id"
    mycursor.execute(query)
    risultati = mycursor.fetchall()
    for riga in risultati:
        print(riga)


def media():
    """Calcola la media dei voti di uno studente per una materia."""
    nome = input("Inserisci il nome dello studente: ").lower()
    cognome = input("Inserisci il cognome dello studente: ").lower()
    valore = (nome, cognome)
    query = "select id from studenti where nome = %s and cognome = %s"
    mycursor.execute(query, valore)
    studente = mycursor.fetchone()
    if studente:
        id = studente[0]
        materia = input("Inserisci la materia: ").lower()
        query = "select voto from voti where id = %s and materia = %s"
        mycursor.execute(query, (id, materia))
        voti = mycursor.fetchall()
        if voti:
            media_voti = round(sum(v[0] for v in voti) / len(voti), 2)
            print(f"La media di {nome} {cognome} in {materia} è: {media_voti}.")
        else:
            print("Nessun voto trovato per questa materia.")
    else:
        print("Studente non trovato.")


# CREAZIONE DEL DATABASE E DELLA TABELLA
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

mycursor = mydb.cursor()
query = "create database if not exists Registro"
mycursor.execute(query)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Registro"
)

mycursor = mydb.cursor()
query = "create table if not exists studenti (id int auto_increment primary key, nome varchar(50), cognome varchar(50))"
mycursor.execute(query)

query = "create table if not exists voti (id int, materia varchar(50), voto float, foreign key (id) references studenti(id) on delete cascade)"
mycursor.execute(query)


# Creazione del menu e aggiunta degli elementi
menu = Menu()

elemento1 = Elemento("Inserisci Studente", Azione(inserisci_studente))
elemento2 = Elemento("Inserisci Voto", Azione(modifica_voto))
elemento3 = Elemento("Elimina Studente", Azione(elimina_studente))
elemento4 = Elemento("Calcola Media", Azione(media))
elemento5 = Elemento("Stampa Registro", Azione(stampa))

menu.aggiungi_elemento(elemento1)
menu.aggiungi_elemento(elemento2)
menu.aggiungi_elemento(elemento3)
menu.aggiungi_elemento(elemento4)
menu.aggiungi_elemento(elemento5)

# Mostra il menu ripetibile
menu.mostra_menu()
