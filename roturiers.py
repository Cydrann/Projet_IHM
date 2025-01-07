from personne import Personne  

class Roturier(Personne):
    def __init__(self, nom, statut, age, edv, capacite_production, ressources=0, argent=0):
        super().__init__(nom, statut, age, edv, ressources, argent)
        self.capacite_production = capacite_production

    def produire(self):
        #Augmente les ressources en fonction de la capacite de production
        self.ressources += self.capacite_production


class Paysan(Roturier):
    def __init__(self, nom, age, edv=60):
        super().__init__(nom, "Paysan", age, edv, capacite_production=3, ressources=5, argent=5)


class Artisan(Roturier):
    def __init__(self, nom, age, edv=75):
        super().__init__(nom, "Artisan", age, edv, capacite_production=5, ressources=15, argent=15)


