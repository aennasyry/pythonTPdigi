
import pathlib, re
from typing import ClassVar
import json
import datetime
class Movie:

    data_file: ClassVar[pathlib.Path] = pathlib.Path().joinpath("data.json") 

    def __init__(self,titre: str,date_sortie: str,resume: str) -> None:
        self.titre=titre
        self.date_sortie = date_sortie
        self.resume=resume
            
        Movie.data_file.touch(exist_ok=True)
        if bool(Movie.data_file.read_text()):
            with open(Movie.data_file, "rb") as file_rb:  
                contenu = json.load(file_rb)

                if self.__dict__ not in contenu["movies"]:  
                    contenu["movies"].append(self.__dict__)  
                    with open(Movie.data_file, 'w') as file_w:  
                        json.dump(contenu, file_w, indent=True)  
                    print("Film rajouté en base de donnée !")  
                else:  
                    print("Film déjà existan en base de donnée !") 
        else:
            with open(Movie.data_file, "w") as file_w:  
                json.dump({"movies": [self.__dict__]}, file_w, indent=True)

    @staticmethod  
    def get_contenu():  
        with open(Movie.data_file, "rb") as file_rb:  
            return json.load(file_rb)
    
    @staticmethod  
    def find_by_title(title: str) -> dict | bool:  

        contenu = Movie.get_contenu()  
        
        for movie in contenu["movies"]:  
            if movie["titre"].lower() == title.lower():  
                return movie  
            return False
    

    @staticmethod  
    def delete(title: str) -> bool:        
        contenu = Movie.get_contenu()  
  
        for index, movie in enumerate(contenu["movies"]):  
            if movie["titre"].lower() == title.lower():  
                contenu["movies"].pop(index)  
                with open(Movie.data_file, 'w') as file_w:  
                    json.dump(contenu, file_w, indent=True)  
                print("le film a bien été supprimé !")  
                Movie.find_all()  
                return True
            else:  
                print("Le film n'existe pas en base de donnée")
                return False
    
    @staticmethod  
    def update(title: str, prop: str, value: str) -> bool:         
        contenu = Movie.get_contenu()  
  
        for movie in contenu["movies"]:  
            if movie["titre"].lower() == title.lower():  
                if prop in movie:  
                    movie[prop] = value  
                    with open(Movie.data_file, 'w') as file_w:  
                        json.dump(contenu, file_w, indent=True)  
                    print(f"Modification de {prop} réussie !")  
                    print(movie)  
                    return True  
                print(f"Propriété {prop} n'existe pas.")  
                return False  

while True:  
    action = input("Choisissez une action: create, read, update ou delete. Stop pour arrêter le script.")  
    match action.lower():  
   
        case "create":  
            title = input("quel est le titre du film ? ")  
            if Movie.data_file.is_file() and bool(Movie.find_by_title(title)):  
                print("Ce film est déjà présent den base de donnée !")  
                exit()  
            date_sortie = input("sa date de sortie ? (dd/mm/YYYY)  ")  
            if not re.fullmatch(r'\d{2}/\d{2}/\d{4}', date_sortie):  
                print("Date au format invalide !")  
                exit()  
            resume = input("son résumé ? ")  
            if bool(title) and bool(resume):  
                movie = Movie(title.title(), date_sortie, resume)  
            else:  
                print("Données vides!")  
  

        case "update":  
            title = input("quelle est le titre du film que vous souhaitez modifier ?  ")  
            if not bool(Movie.find_by_title(title)):  
                print("ce film n'existe pas en base de données !")  
                exit()  
            prop = input("que voulez vous modifier ? (titre, date_sortie, ou resume) ? ")  
            match prop.lower():  
                case "titre":  
                    valeur = input("quel est le nouveau titre de film ? ")  
                    Movie.update(title, prop, valeur)  
                case "date_sortie":  
                    valeur = input("quelle est la nouvelle date de sortie de film ?(dd/mm/YYYY) ? ")  
                    if not re.fullmatch(r'\d{2}/\d{2}/\d{4}', valeur):  
                        print("Date au format invalide !")  
                        exit()  
                    Movie.update(title, prop, valeur)  
                case "resume":  
                    valeur = input("quel est le nouveau résumé du film ? ")  
                    Movie.update(title, prop, valeur)  


        case "delete":  
            title = input("quel est le titre de film que vous voulez supprimer ? ")  
            Movie.delete(title)  


        case "read":    
                title = input("quel est le titre de film que vous cherchez ? ")  
                if not Movie.find_by_title(title):  
                    print("ce film n'existe pas encore en base de données !")  
                    exit()  
                movie = Movie.find_by_title(title)  
                print(movie)
        case _:
            print("le choix saisi est invalide")

