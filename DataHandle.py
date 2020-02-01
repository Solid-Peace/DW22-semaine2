#!/usr/bin/env python
"""Interface entre le stockage et le programme, il constitue le seul point d'entree
et de sortie du programme vers le stockage"""

import os
import json
from models.Note import Note
from models.Etudiant import Etudiant
from models.Cours import Cours


class DataHandle:
    """docstring for DataHandle"""
    path = os.path.join(os.path.dirname(__file__)) + '/data/'
    status = 0

    def __init__(self, filename):
        self.filename = self.path + filename + '.txt'
        self.status = self.init_file()
        print(str(self.status))

    def __str__(self):
        return "status : " + self.status

    def save_data(self, data):
        """ Sauvegarde les donnee dans un fichier donnee """


    def init_file(self):
        """ verifie si le fichier existe deja sinon on le cree """
        if os.path.exists(self.filename):
            print('Le fichier ' + self.filename + ' existe deja.')
            return 1

        if self.create_file():
            return 2

        return 3


    def create_file(self):
        """ Cree un fichier si il n'existe pas """
        try:
            created_file = open(self.filename, 'w')
            print('Le fichier a ete cree')
            created_file.close()
            return True

        except IOError:
            print(self.filename + 'Verifiez les droit d\'ecriture')
            return False


    def read_data(self):
        """" Lit les donnees d'un fichier txt"""


    def append_data(self):
        """ ajoute des donnees a la fin du fichier """


def main():
    """Test"""

if __name__ == '__main__':
    main()
