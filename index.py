

def menu():
    entries = ['1. Lecture des donnees depuis un fichier',
               '2. Ajouter un etudiant', '3. Ajouter une note',
               '4. Afficher les notes d\'un etudiant',
               '5. Afficher les notes triees d\'un cours',
               '6. Supprimer un cours', '7. Sauvegarde des donnees dans un fichier',
               '8. Quitter']

    for menuEntry in entries:
        print(menuEntry)

    choice = input('Votre choix: ')

    print(choice)


menu()
