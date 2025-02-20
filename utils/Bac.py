from utils.Object import Object
class Bac :

    def __init__ (self, cap) :
        self.capacite = cap
        self.capacite_restant = cap
        self.liste_obj = []
    # fin constructeur...
    
    def ajouter_obj (self, objet) :
        self.capacite_restant = self.capacite_restant - objet.taille
        self.liste_obj.append(objet)

# and class Bac