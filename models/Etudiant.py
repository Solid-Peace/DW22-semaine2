''' Classe Etudiant '''
from Cours import Cours
from Note import Note

class Etudiant:
    """
        docstring for ClassName
        etudiant = Etudiant('non', 'prenom', 'age')
        etudiant._notes => toutes ses notes (list of obj)
        etudiant._cours => tout ses cours (list of obj)
        etudiant._cours[x]._notes =>
        
        Etudiant._etudiants_instances => 
            Toutes les insctance de cette classe
            (list obj)
    
    """
    _etudiants_instances = [] # static

    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self._cours = []
        self._notes = []
        Etudiant._etudiants_instances.append(self)

    def __str__(self):
        nb_cours = len(self._cours)
        nb_notes = len(self._notes)
        return " %s %s (%d ans) inscrit a %d cours, possede %d notes" %(self.nom, self.prenom, self.age, nb_cours, nb_notes)

    def __repr__(self):
        return {'nom': self.nom, 'prenom': self.prenom, 'age': self.age}

    def add_cours(self, cours):
        """ Ajouter un cours, cours est une instance de Cours qu'on ajoute à la liste _cours"""
        if isinstance(cours, Cours):
            self._cours.append(cours)
        print("L'etudiant %s %s ajoute au cours %s" %(self.nom, self.prenom, cours.nom_cours))

    def add_note(self, note):
        """ Ajouter une note, note est une instance de Note qu'on ajoute à la liste _cours"""
        if not isinstance(note, Note):
            raise ValueError('first parameter must be instance of Note <class>')
        print("L'etudiant %s %s a obtenue la note de %s ( %s )" %(self.nom, self.prenom, note.note, note.cours))

def main():
    """Test"""
    Etudiant('Jean', 'Paul', 18)

if __name__ == '__main__':
    main()
