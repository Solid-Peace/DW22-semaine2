''' Classe Note '''
from Cours import Cours
from Etudiant import Etudiant

class Note:
    """
        note = Note(note, Etudiant(obj), Cours(obj))

        Note._notes_instances => Toutes les instances de Note (list obj)
    """
    _notes_instances = [] # static

    def __init__(self, note, etudiant, cours):
        if not isinstance(cours, Cours):
            raise ValueError('third parameter must be instance of Cours <class>')
        if not isinstance(etudiant, Etudiant):
            raise ValueError('second parameter must be instance of Etudiant <class>')
        self.note = note
        self.etudiant = etudiant
        self.cours = cours
        etudiant.add_note(self)
        cours.add_note(self)
        Note._notes_instances.append(self)

def main():
    """Test"""
    #Etudiant('Jean', 'Paul', 18)

if __name__ == '__main__':
    main()
