class Lista:

    def __init__(self, lista):

        self.lista = lista
        
    

    def somma_e_stampa(self, lista2):
        
        confronto = lista2.lista
        lista_somma = []

        for i in range(len(self.lista)):

            elemento_i = self.lista[i] + lista2.lista[i]
            lista_somma.append(elemento_i) 

            #PROBLEMA: le due liste devono avere la stessa lunghezza,
            #          così come è scritto il codice sta all'utente
            #          inserire liste della giusta lunghezza!
             
    
        print(lista_somma)



#main

prima_lista = []
seconda_lista = []

print("Inserisci 5 numeri nella prima lista.")
for i in range(5):

    n = float(input("Inserisci un numero: "))
    prima_lista.append(n)

print("Inserisci 5 numeri nella seconda lista.")
for i in range(5):

    n = float(input("Inserisci un numero: "))
    seconda_lista.append(n)

lista1 = Lista(prima_lista)
lista2 = Lista(seconda_lista)


lista1.somma_e_stampa(lista2)
lista2.somma_e_stampa(lista1)
