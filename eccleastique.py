from personne import Personne
import random

class Ecclesiastique(Personne):
    def __init__(self, nom, age, edv, village, don=None):
        super().__init__(nom, "Ecclésiastique", age, edv, ressources=0, argent=0)
        self.village = village 
        self.don = don or self.assigner_don()

    def assigner_don(self):
        #un don aléatoire à l'ecclésiastique
        dons_possibles = [
            "augmentation_production",
            "augmentation_edv",
            "amélioration_humeur"
        ]
        return random.choice(dons_possibles)

    def appliquer_don(self):
        #Applique le don spécial à la paroisse (village associé)
        if self.don == "augmentation_production":
            for personne in self.village.personnes:
                if isinstance(personne, Roturier):
                    personne.capacite_production += 1
        elif self.don == "augmentation_edv":
            for personne in self.village.personnes:
                personne.edv += 2
        elif self.don == "amélioration_humeur":
            for personne in self.village.personnes:
                personne.humeur = min(personne.humeur + 1, 10)