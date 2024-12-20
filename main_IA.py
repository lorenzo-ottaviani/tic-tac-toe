"""
Auteur : Lorenzo OTTAVIANI, Anissa OURDJINI et Diambor NDIAYE
Date : 05/12/2024 16h20
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

# Importation de modules
import random

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
    print("  " + "-" * (5 * taille - 1))

    # Affichage de chaque ligne de la grille avec des bords
    for bord, ligne in enumerate(matrice):
        print("  |", end=" ")
        for cellule in ligne:
            print(f"{cellule} ", end="| ")
        print()

        # Affichage de la bordure horizontale après chaque ligne
        if bord < taille:
            print("  " + "-" * (5 * taille - 1))
    print()


# Fonction qui permet de déterminer si quelqu'un a gagné le jeu
def conditions_victoire(grille):
    """
    Fonction qui determine si l'un des deux joueurs a gagné le jeu.
    :param grille: La grille du morpion.
    :return: Une valeur booléenne permettant de savoir si un joueur a gagné le jeu.
    """
    victoire = False
    symbole_x = ROUGE + "X" + NEUTRE  # # Symbole "X" de couleur rouge
    symbole_o = BLEU + "O" + NEUTRE  # Symbole "O" de couleur bleue

    # Conditions de victoire en ligne
    for ligne in range(3):
        if (grille[ligne][0] == grille[ligne][1] == grille[ligne][2] == symbole_x
                or grille[ligne][0] == grille[ligne][1] == grille[ligne][2] == symbole_o):
            victoire = True

    # Conditions de victoire en colonne
    for colonne in range(3):
        if (grille[0][colonne] == grille[1][colonne] == grille[2][colonne] == symbole_x
                or grille[0][colonne] == grille[1][colonne] == grille[2][colonne] == symbole_o):
            victoire = True

    # Conditions de victoire en diagonale
    if (grille[0][0] == grille[1][1] == grille[2][2] == symbole_x
            or grille[0][0] == grille[1][1] == grille[2][2] == symbole_o):
        victoire = True
    elif (grille[0][2] == grille[1][1] == grille[2][0] == symbole_x
          or grille[0][2] == grille[1][1] == grille[2][0] == symbole_o):
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

    # Fonction qui fait jouer l'IA
    def jeu_ia():
        """
        Fonction qui fait choisir une case par l'IA.
        :return: La case choisie aléatoirement par l'IA.
        """
        # Identifie toutes les positions vides dans la grille
        positions_vides = []
        for ligne_index, ligne in enumerate(grille):
            for colonne_index, valeur in enumerate(ligne):
                if valeur == ' ':
                    positions_vides.append((ligne_index, colonne_index))

        # Choisi une position aléatoire si possible
        if positions_vides:
            ia = random.choice(positions_vides)
        else:
            ia = None  # Cas où la grille est pleine

        return ia

    # Choix du symbole en fonction du joueur
    if joueur == 1:
        symbole = ROUGE + "X" + NEUTRE  # Symbole "X" de couleur rouge

        # Déroulé d'un tour de jeu du joueur humain
        case_valide = False
        while not case_valide:
            try:
                case_joueur = (int(input(f"Joueur {joueur} : Dans quelle case veux-tu te placer ?\nLigne : ")) - 1,
                               int(input(
                                   "Colonne : ")) - 1)  # Demande au joueur de choisir la case ou il souhaite jouer
                if grille[case_joueur[0]][case_joueur[1]] == " ":  # Vérifie que la case soit libre
                    grille[case_joueur[0]][case_joueur[1]] = symbole
                    case_valide = True
                    print()
                else:
                    print("\nCase occupée.\n")  # Cas où la case est occupée

            except IndexError:  # Cas où la case est en dehors de la grille
                print("Case en dehors de la grille.\n")

            except ValueError:  # Cas où on a rentré autre chose qu'un nombre
                print("Ce n'est pas un nombre !\n")

    else:
        symbole = BLEU + "O" + NEUTRE  # # Symbole "O" de couleur bleue

        # Déroulé d'un tour de jeu de l'IA
        case_ia = jeu_ia()
        grille[case_ia[0]][case_ia[1]] = symbole

    return grille


# Fonction principale du jeu
def morpion():
    """
    Fonction qui permet de jouer au morpion (en utilisant les fonctions précédentes).
    :return: Une partie du jeu du morpion.
    """
    print("Bienvenue dans notre version du morpion !\nVoici la grille du jeu vide :\n")
    grille_morpion = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]  # Grille du morpion initiale
    dessine_morpion(grille_morpion)  # Dessine le morpion du début
    print("Le jeu durera au maximum 9 tours, à toi de gagner avant !\nBonne chance !\n")
    joueur_courant = 1  # Défini le joueur qui joue au début

    for tour_jeu in range(1, 10):  # Déroule les 9 tours du jeu
        print(VERT + f"Tour {tour_jeu}\n" + NEUTRE)  # Rappelle au joueur le tour actuel
        tour_courant(grille_morpion, joueur_courant)  # Joue le tour actuel
        dessine_morpion(grille_morpion)  # Dessine le morpion du tour actuel

        if conditions_victoire(grille_morpion):  # Vérification des conditions de victoire
            print(f"Victoire du Joueur {joueur_courant}! 🎉")
            break  # Arrète le jeu si un joueur a gagné

        joueur_courant = 1 if joueur_courant == "IA" else "IA"  # Détermine quel joueur doit jouer le tour suivant

    if not conditions_victoire(grille_morpion):
        print("Match nul! 🤝")  # Indique que le match est nul si personne n'a gagné


# Programme principal
morpion()
