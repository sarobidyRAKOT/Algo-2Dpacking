from utils.Bac import Bac
from utils.Object import Object
from itertools import permutations

class Dim_1 :
    
    def __init__ (self) :
        self.list_bac = [] # bacs + obj ao anatiny
    # Constructeur ...



# First Fit algorithme
# objectif : zay bac omby anazy voloany no asina azy
    def first_fit (self, objs, n, bac) :
        # objs : tableau d'object
        # n : taille du tableau
        count_bac = 0
        # boucler tableau obj
        for i in range(n) : 
            j = 0
            while (j < count_bac) : 
                if (self.list_bac[j].capacite_restant >= objs[i].taille) :
                    self.list_bac[j].ajouter_obj(objs[i])
                    break
                j += 1
            if (j == count_bac) : # si aucun bac n'est compatible a l'object
                self.list_bac.append(Bac(bac.capacite))
                self.list_bac[count_bac].ajouter_obj(objs[i])
                count_bac = count_bac + 1

        return count_bac
# fin First Fit algorithme


# Best Fit
# Objectif : laisse le moins d'espace possible apres l'insertion
    def best_fit (self, objs, n, bac) :

        count_bac = 0
        for i in range(n):
            j = 0

            min = bac.capacite + 1 # min bac restant
            index = 0 # index du meilleur bac   
        
            for j in range(count_bac):
                if (self.list_bac[j].capacite_restant >= objs[i].taille and self.list_bac[j].capacite_restant - objs[i].taille < min) :
                    index = j
                    min = self.list_bac[j].capacite_restant - objs[i].taille

            #  si aucun bac n'est compatible
            if (min == bac.capacite + 1) :
                self.list_bac.append(Bac(bac.capacite))
                self.list_bac[count_bac].ajouter_obj(objs[i])
                count_bac += 1
            else : # si compatible
                self.list_bac[index].ajouter_obj(objs[i])

        return count_bac
# fin bestFit

# Worst Fit
# Objectif : laisse le plus d'espace possible apres l'insertion
    def worst_fit (self, objs, n, bac) :

        count_bac = 0

        for i in range(n):
            max = -1
            index = 0
            for j in range(count_bac):
                if (self.list_bac[j].capacite_restant >= objs[i].taille and self.list_bac[j].capacite_restant - objs[i].taille > max) :
                    index = j
                    max = self.list_bac[j].capacite_restant - objs[i].taille
        
            # si aucun bac n'est compatible a la taille de l'objet
            # creer un nouveau bac
            if (max == -1):
                self.list_bac.append(Bac(bac.capacite))
                self.list_bac[count_bac].ajouter_obj(objs[i])
                count_bac += 1
            else: # sinon
                self.list_bac[index].ajouter_obj(objs[i])

        return count_bac
# fin worstFit

# brute force
            
    def add_to_bacs (self, bacs, obj, capacite) :
        for bac in bacs :
            if (bac.capacite_restant >= obj.taille) : 
                bac.ajouter_obj (obj)
                return bacs
        bac = Bac (cap= capacite)
        bac.ajouter_obj(obj)
        bacs.append(bac)

        return bacs

    def brute_force (self, objs, bac) :
        min_bacs = float('inf')

        # pour chaque permutation possible
        for perm in permutations(objs) : 
            bacs = []
            for obj in perm :
                bacs = self.add_to_bacs(bacs, obj, bac.capacite)
            if len(bacs) < min_bacs:
                min_bacs = len(bacs)
                self.list_bac = bacs

        return len (self.list_bac) # nbr de bacs utilisés
# fin brute force 

    def display_res (self) :
        i = 1
        for bac in self.list_bac :
            print ("bac",i,": ", end='')
            for obj in bac.liste_obj : 
                print (obj.taille," ", end='')
            i += 1
            print()
    # fin fonction display