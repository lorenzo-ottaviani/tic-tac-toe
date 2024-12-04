"""
Auteur : Lorenzo OTTAVIANI
Date : 04/12/2024 15h39
But du programme :
    Créer un jeu de tic tac toe (morpion) avec deux joueurs humains.
Entrée : case_joueur : Permet au joueur qui joue de choisir la case où il veut jouer sur la grille du jeu.
Sortie : Le tic tac toe.
"""

"""
Rappel des conditions de victoire :

grille_victoire1 = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
grille_victoire2 = [[" ", " ", " "], ["X", "X", "X"], [" ", " ", " "]]
grille_victoire3 = [[" ", " ", " "], [" ", " ", " "], ["X", "X", "X"]]

grille_victoire4 = [["X", " ", " "], ["X", " ", " "], ["X", " ", " "]]
grille_victoire5 = [[" ", "X", " "], [" ", "X", " "], [" ", "X", " "]]
grille_victoire6 = [[" ", " ", "X"], [" ", " ", "X"], [" ", " ", "X"]]

grille_victoire7 = [["X", " ", " "], [" ", "X", " "], [" ", " ", "X"]]
grille_victoire8 = [[" ", " ", "X"], [" ", "X", " "], ["X", " ", " "]]
"""

# Définition des couleurs du jeu
ROUGE = "\033[31m"
VERT = "\033[32m"
BLEU = "\033[34m"
NEUTRE = "\033[0m"


# Fonction qui permet de dessiner le morpion
def dessine_morpion(matrice):
    """
    Fonction qui dessine la matrice du morpion graphiquement avec des bordures.
    :param matrice: La matrice du morpion.
    :return: ∅
    """
    # Détermine le nombre de lignes de la grille
    taille = len(matrice)

    # Affichage de la bordure supérieure
    print("  " + "-" * (6 * taille - 1))

    # Affichage de chaque ligne de la grille avec des bords
    for bord, ligne in enumerate(matrice):
        print("  |", end=" ")
        for cellule in ligne:
            print(f" {cellule} ", end="| ")
        print()

        # Affichage de la bordure horizontale après chaque ligne
        if bord < taille:
            print("  " + "-" * (6 * taille - 1))
    print()


# Fonction qui permet de déterminer si quelqu'un a gagné le jeu
def conditions_victoire(grille):
    """
    Fonction qui determine si l'un des deux joueurs a gagné le jeu.
    :param grille: La grille du morpion.
    :return: Une valeur booléenne permettant de savoir si un joueur a gagné le jeu.
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


# Fonction qui déroule un tour du jeu.
def tour_courant(grille, joueur):
    """
    Fonction qui déroule un tour du jeu.
    :param grille: La grille du morpion.
    :param joueur: Le joueur qui joue actuellement (1 pour joueur 1 et 2 pour joueur 2).
    :return: Effectue un tour du jeu.
    """

    # Choix du symbole en fonction du joueur
    if joueur == 1:
        symbole = ROUGE + "X" + NEUTRE
    else:
        symbole = BLEU + "O" + NEUTRE

    # Déroulé d'un tour du jeu
    k = -1
    while k < 0:
        try:
            case_joueur = (int(input(f"Joueur {joueur} : Dans quelle case veux-tu te placer ?\nLigne : ")) - 1,
                           int(input("Colonne : ")) - 1)  # Demande au joueur de choisir la case ou il souhaite jouer
            if grille[case_joueur[0]][case_joueur[1]] == " ":  # Vérifie que la case soit libre
                grille[case_joueur[0]][case_joueur[1]] = symbole
                k = 1
                print()
            else:
                print("\nCase occupée.\n")  # Cas où la case est occupée

        except IndexError:  # Cas où la case est en dehors de la grille
            print("Case en dehors de la grille.\n")

        except ValueError:  # Cas où on a rentré autre chose qu'un nombre
            print("Ce n'est pas un nombre !\n")

    return grille


# Programme principal
print()
grille_morpion = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]  # Grille du morpion initiale
dessine_morpion(grille_morpion)  # Dessine le morpion du début

for tour_jeu in range(1, 10):  # Déroule les 9 tours du jeu
    print(VERT + f"Tour {tour_jeu}\n" + NEUTRE)  # Rappelle au joueur le tour actuel
    if tour_jeu % 2 != 0:  # Détermine quel joueur doit jouer ce tour-ci
        joueur_courant = 1  # Lors d'un tour impair, le joueur avec "X" joue.
    else:
        joueur_courant = 2  # Lors d'un tour pair, le joueur avec "O" joue.
    tour_courant(grille_morpion, joueur_courant)  # Joue le tour actuel
    dessine_morpion(grille_morpion)  # Dessine le morpion du tour actuel
    if conditions_victoire(grille_morpion) is True:  # Vérification des conditions de victoire
        print(f"Victoire du {joueur_courant}!")
        break  # Arrète le jeu si un joueur a gagné

if conditions_victoire(grille_morpion) is False:
    print("Match nul!")  # Indique que le match est nul si personne n'a gagné
