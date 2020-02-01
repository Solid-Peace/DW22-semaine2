''' Classe Etudiant '''
from Cours import Cours
from Note import Note

class Etudiant:
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
    _etudiants_instances = {} # static

    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.identifiant = nom + prenom[:2]
        # Dict cours => [notes] de cet etudiant
        self._cours_notes = {}
        # On stock l'emplacement memoire de chaque instance
        Etudiant._etudiants_instances[self.identifiant] = self

    def add_cours(self, nom_cours):
        """
        Nous permet d'acceder a l'emplacement de l'instance cours tout en passant
        un string en parametre de la methode
        """
        cours = Cours._cours_instances[nom_cours] # pylint: disable=W0212
        if not nom_cours in self._cours_notes:
            # On ajoute un cours en tant que key du dict _cours_notes
            self._cours_notes[nom_cours] = []
            cours.add_etudiant(self)
            print("L'etudiant %s %s a ete ajoute au cours de %s" %(self.nom, self.prenom, cours.nom_cours))
        else:
            print("L'etudiant est deja inscrit a ce cours")

    def add_note(self, note, nom_cours):
        """ On ajoute une en tant que valeur du dict _cours_notes"""
        cours = Cours._cours_instances[nom_cours] # pylint: disable=W0212
        Note(note, self, cours)
        try:
            self._cours_notes[nom_cours].append(note)
            print("L'etudiant %s %s obtient %d en cours de %s" %(self.prenom, self.nom, note, nom_cours))
        except KeyError:
            print("l'etudiant n'est pas inscit a ce cours ...")

def main():
    """
        __dict__ est utilise pour retourner l'objet sou forme de dictionnaire 
        facilement exploitable en le parsant en JSON pour esuite le stocker
    """
    jean = Etudiant('Jean', 'Paul', 18)
    print(jean.__dict__)

    anglais = Cours('anglais')
    print(anglais.__dict__)

    jean.add_cours('anglais') # Equivaudrait a faire jean.add_cours(anglais)
    print(jean.__dict__)        # sans les guillemes
    print(anglais.__dict__)

    jean.add_note(17, 'anglais')
    print(jean.__dict__)
    print(anglais.__dict__)

if __name__ == '__main__':
    main()
