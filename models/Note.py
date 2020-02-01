''' Classe Note '''
#from Cours import Cours


class Note:
    """
    """
    _notes_instances = [] # static

    def __init__(self, note, etudiant, cours):     
        self.note = note
        self.etudiant = etudiant
        self.cours = cours
        cours.add_note(self, self.etudiant)
        Note._notes_instances.append(self)

def main():
    """Test"""

if __name__ == '__main__':
    main()
