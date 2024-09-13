import re

class Entreprise:
    def __init__(self,nom : str, adresse : str, siret : str) -> None:
        self.nom = nom
        self.adresse = adresse
        self.siret=siret

    
    def __str__(self) -> str:
        return f"L'entreprise {self.nom}, ayant son siège social au {self.adresse}, possède le numéro de SIRET {self.siret}"
    
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self,nom):
        self.__nom = nom
    
    @property
    def adresse(self):
        return self.__adresse
    @adresse.setter
    def adresse(self,adresse):
        self.__adresse = adresse
    
    @property
    def siret(self):
        return self.__siret
    @siret.setter
    def siret(self,siret):
        if re.match(r"^[0-9]{14}$",siret):
            self.__siret = siret
        else:
            print("le numero siret saisi n'est pas valide")

entreprise1 = Entreprise("nike","2 rue america, usa","42131111111111")
print(entreprise1)
print(entreprise1.nom)
entreprise1.siret = "321245678945612"
print(entreprise1)
