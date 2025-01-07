from personne import Personne

class Noble(Personne):
    def __init__(self, nom, age, edv):
        super().__init__(nom, "Noble", age, edv, ressources=0, argent=100)#ils ont plus d'argent
        self.terres = []  #les villages possédés

    def ajouter_village(self, village):
        self.terres.append(village)

    def imposer_roturiers(self):#la moitié pour les paysans et le quart pour les autres
        for village in self.terres:
            for personne in village.personnes:
                if isinstance(personne, Paysan):
                    impots = personne.ressources // 2
                else:
                    impots = personne.ressources // 4
                personne.ressources -= impots
                self.ressources += impots
class Seigneur(Noble):
    def __init__(self, nom, age, edv):
        super().__init__(nom, age, edv)
        self.vassaux = []  #nobles vassaux du seigneur

    def ajouter_vassal(self, vassal):
        #Ajoute un noble comme vassal
        if isinstance(vassal, Noble):
            self.vassaux.append(vassal)

    def imposer_vassaux(self, taux=0.15):
        #pour imposer les vassaux à un taux réduit
        for vassal in self.vassaux:
            impots = int(vassal.ressources * taux)
            vassal.ressources -= impots
            self.ressources += impots