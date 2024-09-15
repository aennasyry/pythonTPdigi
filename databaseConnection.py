from dataclasses import dataclass
from typing import ClassVar

@dataclass
class DatabaseConnection:
    type :str
    user : str
    password : str
    hote : str = "localhost"

    nb_instance: ClassVar[int] = 0

    #La classe possède une propriété statique `nb_instance` qui va s'incrémenter à chaque création d'un objet issu de cette classe.
    def __post_init__(self):
        DatabaseConnection.nb_instance =+ 1 
    
    #La classe possède une méthode statique retournant le nombre total d'instance sous la forme : "La classe DatabaseConnection possède actuellement {x} instance(s).".
    @staticmethod
    def nb_total_instance():
        return f"La classe DatabaseConnection possède actuellement {DatabaseConnection.nb_instance} instance(s)."
    
    #La classe possède une méthode de classe permettant de créer une instance avec les informations suivante : type -> "mariadb", hôte -> "76.287.872.12", utilisateur -> "root", mot de passe -> "1234".
    @classmethod
    def creer_instance_specifique(cls):
        return cls("mariadb",  "root", "1234", "76.287.872.12")
    
    def __str__(self) -> str:
        return f"DatabaseConnexion : (type : {self.type}, user : {self.user}, mot de passe : {self.password}, hote : {self.hote} )"
    

#Initialiser un objet de cette classe sans spécifier l'hôte et printer le résultat obtenu.
connexion1 = DatabaseConnection("mariadb", "aladin", "12340")
print(connexion1)

#Initialiser un objet de cette classe en appelant votre factory, et printer le résultat obtenu.
connexion2 = DatabaseConnection.creer_instance_specifique()
print(connexion2)