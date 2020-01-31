''' Classe Etudiant '''
from Note import Note
from Etudiant import Etudiant

class Cours:
    """
        cours = Cours('nom du cours')
        cours._notes = toutes les notes du cours
        cours._etudiants => tous les etudiants inscrits
            a ce cours (list obj)
        cours._notes => toutes les notes de ce cours (list obj)

        Cours._cours_instances =>
            Toutes les insctance de cette classe (list obj)
    """
    _cours_instances = [] # static

    def __init__(self, nom_cours):
        self.nom_cours = nom_cours
        self._notes = []
        self._etudiants = []
        Cours._cours_instances.append(self)

    def __str__(self):
        nb_etudiants = len(self._etudiants)
        return "%s (%d etudiants inscrits)" %(self.nom_cours, nb_etudiants)

    def add_etudiant(self, etudiant):
        """Ajout d'une instance etudiant a la liste des etudiants participant au cours"""
        if not isinstance(etudiant, Etudiant):
            raise ValueError('first parameter must be instance of Etudiant <class>')
        self._etudiants.append(etudiant)
        etudiant.add_cours(self)

    def add_notes(self, note):
        if not isinstance(note, Note):
            raise ValueError('first parameter must be instance of Note <class>')
        self._notes.append(note)

def main():
    """Test"""
    #Etudiant('Jean', 'Paul', 18)

if __name__ == '__main__':
    main()
