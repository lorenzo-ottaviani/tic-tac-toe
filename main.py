"""
Auteur : Lorenzo OTTAVIANI
Date : 03/12/2024 9h54
But du programme :
    Créer un jeu de tic tac toe (morpion) avec deux joueurs humains.
Entrée : ∅
Sortie : Le tic tac toe.
"""

# Grille du jeu
grille_morpion = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print(grille_morpion)

# Conditions de victoire
grille_victoire1 = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
grille_victoire2 = [[" ", " ", " "], ["X", "X", "X"], [" ", " ", " "]]
grille_victoire3 = [[" ", " ", " "], [" ", " ", " "], ["X", "X", "X"]]

grille_victoire4 = [["X", " ", " "], ["X", " ", " "], ["X", " ", " "]]
grille_victoire5 = [[" ", "X", " "], [" ", "X", " "], [" ", "X", " "]]
grille_victoire6 = [[" ", " ", "X"], [" ", " ", "X"], [" ", " ", "X"]]

grille_victoire7 = [["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]
grille_victoire8 = [[" ", " ", "X"], [" ", "X", " "], ["X", " ", " "]]


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
dessine_morpion([["X", "O", " "], [" ", "X", "O"], [" ", " ", "X"]])


# Fonction qui permet de déterminer si quelqu'un a gagné le jeu
def conditions_victoire(grille):
    """
    Fonction qui determine si l'un des deux joueurs a gagné le jeu.
    :param grille: La grille du morpion.
    :return:
    """
    victoire = False
    # Conditions de victoire en ligne
    for colonne in range(3):
        if (grille[colonne][0] == grille[colonne][1] == grille[colonne][2] == "X"
                or grille[colonne][0] == grille[colonne][1] == grille[colonne][2] == "O"):
            victoire = True

    # Conditions de victoire en colonne
    for ligne in range(3):
        if (grille[0][ligne] == grille[1][ligne] == grille[2][ligne] == "X"
                or grille[0][ligne] == grille[1][ligne] == grille[2][ligne] == "O"):
            victoire = True

    # Conditions de victoire en diagonale
    if grille[0][0] == grille[1][1] == grille[2][2] == "X" or grille[0][0] == grille[1][1] == grille[2][2] == "O":
        victoire = True
    elif grille[0][2] == grille[1][1] == grille[2][0] == "X" or grille[0][2] == grille[1][1] == grille[2][0] == "O":
        victoire = True

    return victoire


# Exemple de victoire (avec message)
grillage = [[" ", " ", " "], ["X", "X", "X"], [" ", " ", " "]]
if conditions_victoire(grillage) is True:
    print("Victoire !")
