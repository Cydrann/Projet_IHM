import random 


class Personne:
    def __init__(self, nom, statut, age, edv, ressources, argent):
        self.nom = nom
        self.statut = statut
        self.age = age
        self.edv = edv  # Ajoutez edv ici
        self.ressources = ressources
        self.argent = argent
        self.humeur = 5


    def acheter_ressources(self, vendeur, quantite, prix):
        if self.argent >= quantite * prix: #on vérifie si la personne a assez d'argent
            self.ressources += quantite
            self.argent -= quantite * prix
            vendeur.ressources -= quantite
            vendeur.argent += quantite * prix
            print(f"{self.nom} a acheté {quantite} ressources à {vendeur.nom} pour {quantite * prix} unités d'argent.")
        else:
            print(f"{self.nom} n'a pas assez d'argent pour acheter {quantite} ressources.")

    def vendre_ressources(self, acheteur, quantite, prix):
        if self.ressources >= quantite: #test de l'existance de la quantité chez la personne
            self.ressources -= quantite
            self.argent += quantite * prix
            acheteur.ressources += quantite
            acheteur.argent -= quantite * prix
            print(f"{self.nom} a vendu {quantite} ressources à {acheteur.nom} pour {quantite * prix} unités d'argent.")
        else:
            print(f"{self.nom} n'a pas assez de ressources pour vendre {quantite}.")

    def augmenter_humeur(self):
        if self.humeur >= 10: #verification de l'humeur de la personne
            self.humeur += 1
        else:
            print(f"{self.nom} est bieen.")

    def baisser_humeur(self):
        if self.humeur < 0:
            self.humeur -= 1
        else:
            print(f"{self.nom} va bientot crever.")

    def viellir(self):
        if self.age < self.edv: # on vérifie si la personne n'a pas encore atteint son edv
            self.age += 1 
            print(f"{self.nom} a pris de l'age.")
        else:
            print(f"{self.nom} a atteint son edv et est malheureusement décédé.")
            self.mourir()
            
    def mourir(self):
        self.village.habitants.remove(self)
