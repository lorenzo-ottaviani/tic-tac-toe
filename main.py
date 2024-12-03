"""
Auteur : Lorenzo OTTAVIANI
Date : 03/12/2024 9h54
But du programme :
    Créer un jeu de tic tac toe (morpion) avec deux joueurs humains.
Entrée : ∅
Sortie : Le tic tac toe.
"""

# Grille du jeu
grille = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(grille)

# Conditions de victoire
grille_victoire1 = [["X", "X", "X"], [0, 0, 0], [0, 0, 0]]
grille_victoire2 = [[0, 0, 0], ["X", "X", "X"], [0, 0, 0]]
grille_victoire3 = [[0, 0, 0], [0, 0, 0], ["X", "X", "X"]]

grille_victoire4 = [["X", 0, 0], ["X", 0, 0], ["X", 0, 0]]
grille_victoire5 = [[0, "X", 0], [0, "X", 0], [0, "X", 0]]
grille_victoire6 = [[0, 0, "X"], [0, 0, "X"], [0, 0, "X"]]

grille_victoire7 = [["X", 0, 0], [0, "X", 0], [0, 0, "X"]]
grille_victoire8 = [[0, 0, "X"], [0, "X", 0], ["X", 0, 0]]


# Fonction qui permet de dessiner le morpion
def dessine_morpion(matrice):

    """
    Fonction qui dessine la matrice du morpion graphiquement (sans return).
    :param matrice: La matrice du morpion.
    :return: ∅
    """
    if len(matrice) > 0:
        for colonne in range(len(matrice)):
            for ligne in range(len(matrice[colonne])):
                print(matrice[colonne][ligne], end=" ")
            print()
    else:
        print()


# Dessin du morpion dans le terminal
dessine_morpion([["X", "X", " "], [" ", "X", " "], [" ", " ", "X"]])
