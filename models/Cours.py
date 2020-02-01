''' Classe Cours '''
from Note import Note

class Cours:
    """
        docstring for ClassName
        ####
        #
        # _etudiants_instances et _cours_instances
        #
        # servent de systeme de pointeur afin de pouvoir
        # faire reference a un objet ou bien a l'instancier
        # via une chaine de caractere
        #
        # Ayant pour objectif de simplifier le programme
        #
        # _etudiants_instances => { nom_de_instance : emplacement memoire }
        #
        #
        ####
    """
    _cours_instances = {} # static

    def __init__(self, nom_cours):
        self.nom_cours = nom_cours
        # Dict etudiant => [notes] de ce cours
        self._etudiants_notes = {}
        # On stock l'emplacement memoire de chaque instance
        Cours._cours_instances[self.nom_cours] = self

    def add_etudiant(self, etudiant):
        """Ajout d'une instance etudiant a la liste des etudiants participant au cours"""
        self._etudiants_notes[etudiant.identifiant] = []

    def add_note(self, note, etudiant):
        """Ajout de la note d'un etudiant pour ce cours"""
        try:
            self._etudiants_notes[etudiant.identifiant].append(note.note)
        except KeyError:
            print("l'etudiant n'est pas inscit a ce cours ...")

def main():
    """Test"""

if __name__ == '__main__':
    main()
