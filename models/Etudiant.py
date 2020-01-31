''' Classe Etudiant '''
from Cours import Cours

class Etudiant:
    """docstring for ClassName"""
    _cours = []
    _notes = []

    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __repr__(self):
        nb_cours = len(self._cours)
        nb_notes = len(self._notes)
        return " %s %s (%d ans) inscris à %d cours, possède %d notes" %(self.nom, self.prenom, self.age, nb_cours, nb_notes)

    def add_cours(self, cours):
        """ Ajouter un cours, cours est une instance de Cours qu'on ajoute à la liste _cours"""
        if isinstance(cours, Cours):
            self._cours.append(cours)
            print()


def main():
    """Test"""
    etudiant = Etudiant('Jean', 'Paul', 18)

if __name__ == '__main__':
    main()
