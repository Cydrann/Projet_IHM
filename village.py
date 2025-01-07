from roturiers import Paysan, Artisan
from eccleastique import Ecclesiastique


class Village:
    def __init__(self, id, nom, x, y):
        self.id = id
        self.position = (x, y)
        self.nom = nom
        self.habitants = []  # Liste d'instances de Roturier et de Paysan
        self.noble = None  # Instance de Noble
        self.eglise = None
        self.armee_village = 15

    def ajouter_habitant(self, habitant):
        self.habitants.append(habitant)

    def ajouter_liste_habitants(self, liste_habitants):
        self.habitants.extend(liste_habitants)

    def ajouter_noble(self, noble):
        self.noble = noble

    def recruter_soldats(self, nombre_soldats=5): #Recrute 5 soldats 
        self.armee_village += nombre_soldats
        #print(f"{nombre_soldats} soldats ont été recrutés dans le village {self.nom}.")
        #print(f"Armée actuelle : {self.armee_village} soldats.")

    def ajouter_ecclesiastique(self):

        nom_ecclesiastique = f"Ecclésiastique {len(self.habitants) + 1}"  
        ecclesiastique = Ecclesiastique(
            nom=nom_ecclesiastique,
            age=40,
            edv=70,
            village=self
        )
        self.ajouter_habitant(ecclesiastique)

        print(f"L'ecclésiastique {nom_ecclesiastique} a été ajouté au village {self.nom}. et il a le don :{ecclesiastique.don}]")

    def population(self):
        return len(self.habitants)

    def somme_ressources(self):
        somme_res = 0
        for habitant in self.habitants:
            somme_res += habitant.argent
        return somme_res

    def somme_argent(self):
        somme_arg = 0
        for habitant in self.habitants:
            somme_arg += habitant.argent
        return somme_arg


    def immigrer(self, nombre_paysans=5, nombre_artisans=2):
        compteur_paysans = 0
        while compteur_paysans < nombre_paysans:
            nom_paysan = f"Paysan {len(self.habitants) + 1}"
            paysan = Paysan(nom=nom_paysan, age=20, edv=60)
            self.ajouter_habitant(paysan)
            compteur_paysans += 1

        compteur_artisans = 0
        while compteur_artisans < nombre_artisans:
            nom_artisan = f"Artisan {len(self.habitants) + 1}"
            artisan = Artisan(nom=nom_artisan, age=25, edv=75)
            self.ajouter_habitant(artisan)
            compteur_artisans += 1
