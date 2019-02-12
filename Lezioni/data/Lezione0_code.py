class Mammifero:
    # Variabili di classe: sono le proprietà comuni a tutte le istanze
    genere = "animale"
    essere_vivente = "si"
    
    # Costruttore: operazioni eseguite quando viene creato l'oggetto (istanza)
    def __init__(self, nome, ha_pelo, ha_coda, verso):
        self.nome = nome
        self.ha_pelo = ha_pelo
        self.ha_coda = ha_coda
        self.verso = verso
        self.vivo = "no"
        
    # Definisco i metodi per il Mammifero (associati all'istanza)
    def nascita(self):
        self.vivo = "si"
        print("È nato un nuovo {0} di nome '{1}'".format(self.genere, self.nome))
    def morte(self):
        self.vivo = "no"
        print("R.I.P. {0} di nome '{1}.".format(self.genere, self.nome))
    def stato_vita(self):
        if self.vivo == "si":
            print("È vivo!")
        else:
            print("È morto!")
    def fai_verso(self):
        print("{}: <<< {} >>>".format(self.nome, self.verso))
        
gatto = Mammifero(nome="Micio Mao", ha_pelo="si", ha_coda="si", verso="miaooooooo")

print(gatto)

gatto.stato_vita()
gatto.nascita()
gatto.stato_vita()
#Variabili comuni a tutti gli animali
print("Il genere del gatto è: " + gatto.genere)
print("È un essere vivente? " + gatto.essere_vivente)
#Variabili di istanza
print("Ha il pelo? " + gatto.ha_pelo)
print("Ha la coda? " + gatto.ha_coda)
gatto.fai_verso()

un_altro_gatto = Mammifero(nome="Felix", ha_pelo="si", ha_coda="si", verso="miaooooooo")
print(un_altro_gatto)
un_altro_gatto.nascita()
un_altro_gatto.stato_vita()
print("Ha il pelo? " + un_altro_gatto.ha_pelo)
print("Ha la coda? " + un_altro_gatto.ha_coda)

un_altro_gatto.ha_coda = "no"

print(gatto.nome + " - " + str(gatto))
print("Ha la coda? " + gatto.ha_coda)
print(un_altro_gatto.nome + " - " + str(un_altro_gatto))
print("Ha la coda? " + un_altro_gatto.ha_coda)

gatto.morte()
un_altro_gatto.morte()

class Uomo(Mammifero):
    # Sovrascrivo il genere, non siamo più semplici animali
    genere = "Homo Sapiens"
    
    # Definisco il costruttore, inizializzo le variabili della sovra-classe e quelle della classe 
    def __init__(self, nome, colore_pelle, colore_capelli, lingua_parlata):
        super().__init__(nome, ha_pelo="no", ha_coda="no", verso="bla bla bla")
        self.colore_pelle = colore_pelle
        self.colore_capelli = colore_capelli
        self.lingua_parlata = lingua_parlata
        
    # Un metodo specifico dell'Uomo
    def info_uomo(self):
        print("{0} è un {1} con la pelle di colore {2}, i capelli di colore {3} e parla {4}.".format(self.nome, \
            self.genere, self.colore_pelle, self.colore_capelli, self.lingua_parlata))
        
        
vicino_di_casa = Uomo("Marcolino", "bianco", "castano", "italiano")
print(vicino_di_casa)

vicino_di_casa.nascita()
vicino_di_casa.stato_vita()
#Variabili comuni a tutti gli animali
print("Il genere è: " + vicino_di_casa.genere)
print("È un essere vivente? " + vicino_di_casa.essere_vivente)
#Variabili di istanza
print("Ha il pelo? " + vicino_di_casa.ha_pelo)
print("Ha la coda? " + vicino_di_casa.ha_coda)
vicino_di_casa.fai_verso()

vicino_di_casa.info_uomo()

vicino_di_casa.morte()