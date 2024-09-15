import re
from typing import ClassVar
#Créer une classe "Client" possédant un nom, un prénom, une adresse, et un numéro de sécurité sociale (NIR) composé de 15 chiffres. Un contrôle doit être réalisé sur 
#le NIR au moment de la création d'un nouvel objet.
class Client:

    def __init__(self, nom:str, prenom:str, adresse:str, nir:str) -> None:
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.nir =nir
    
    @property
    def nir(self):
        return self.__nir
    @nir.setter
    def nir(self,nir):
        if re.match(r"^[0-9]{15}$", nir):
            self.__nir = nir
        else:
            raise ValueError("le numero de securité social doit comporter 15 chiffres")

from datetime import date
import random
import string
#La classe a 4 propriétés : - Une date de création au format `date` - Un client de type `Client` - Un identifiant interne composé de 4 lettres majuscules 
# aléatoires suivies de la date de création du compte au format `DDMMYYYY` (exemple: IYSQ26052020) - Un solde de type `float`
class Compte_bancaire:

    #La classe "CompteBancaire" possède également une propriété statique renvoyant la somme des soldes de tous les clients de la banque.
    solde_total : ClassVar[float] =0

    def __init__(self, date_creation :date, client :Client, solde :float) -> None:
        self.date_creation = date_creation
        self.client = client
        self.solde = solde

        lettres_aleatoires = ''.join(random.choice(string.ascii_letters) for _ in range(3))
        day = str(date_creation.day) if date_creation.day>9 else "0" + str(date_creation.day)
        month = str(date_creation.month) if date_creation.month>9 else "0" + str(date_creation.month)
        self.identifiant = lettres_aleatoires + day +  month + str(date_creation.year)

        Compte_bancaire.solde_total +=solde

    def __str__(self) -> str:
        return f"Compte bancaire : (date de creation : {self.date}, client : {self.client}, idsentifiant : {self.identifiant}, solde : {self.solde}) "
    
    #Deux comptes bancaires sont considérés comme égaux lorsque leur soldes sont égales (méthode magique
    def __eq__(self, value: object) -> bool:
        return self.solde == value.solde

client1 = Client("alae", "naciri", "9 rue gauguin", "123456789123456")

#Créer 2 objets comptes bancaires, printer leur identifiant interne respectif, et printer leur égalité l'un avec l'autre.
compte1 = Compte_bancaire(date(2024,11,2), client1, 20000.5)
compte2 = Compte_bancaire(date(2024,1,2), client1, 20000)

print(f"l'identifiant du compte 1 : {compte1.identifiant}")
print(f"l'identifiant du compte 2 : {compte2.identifiant}")

print(f"le compte 1 est-il égale au compte 2 ? {compte1.__eq__(compte2)}")

#Printer le solde total de tous les comptes bancaires créés   
print(f"le solde total est: {Compte_bancaire.solde_total}")