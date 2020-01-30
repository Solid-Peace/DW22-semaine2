from consolemenu import ConsoleMenu
from consolemenu.items import MenuItem


menu = ConsoleMenu("Etudiants - Cours - Notes")

menuItems = [
    "Lecture des donnees depuis un fichier",
    "Ajouter un etudiant", "Ajouter un note",
    "Afficher les notes d\'un etudiant",
    "Afficher les notes triees d\'un cours",
    "Supprimer un cours",
    "Sauvegarde des donees dans un fichier",
]

for menuItem in menuItems:
    menu.append_item(MenuItem(menuItem))


menu.show()
