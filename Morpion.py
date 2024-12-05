import random  # Importation du module pour les choix aléatoires

# Codes couleurs ANSI
ROUGE = '\033[91m'  # Rouge pour "O"
BLEU = '\033[94m'   # Bleu pour "X"
RESET = '\033[0m'   # Réinitialisation des couleurs

# Initialisation du plateau
def initialiser_plateau():
    """
    Crée un plateau vide de 9 cases représentées par des espaces.
    """
    return [" " for _ in range(9)]

# Fonction pour colorer les caractères
def colorer_signe(signe):
    """
    Retourne le signe coloré selon qu'il est 'X' ou 'O'.
    """
    if signe == "X":
        return f"{BLEU}X{RESET}"  # Bleu pour X
    elif signe == "O":
        return f"{ROUGE}O{RESET}"  # Rouge pour O
    return " "  # Espace pour une case vide

# Affichage du plateau
def afficher_plateau(plateau):
    """
    Affiche le plateau de jeu avec des bordures fermées et des cases alignées.
    Les cases sont colorées selon leur contenu.
    """
    print("\n")
    for i in range(3):  # Parcourt chaque ligne
        # Affiche la ligne avec les cases colorées
        print(f" {colorer_signe(plateau[i * 3])} │ {colorer_signe(plateau[i * 3 + 1])} │ {colorer_signe(plateau[i * 3 + 2])} ")
        if i < 2:  # Affiche les séparateurs horizontaux pour les deux premières lignes
            print("───┼───┼───")
    print("\n")

# Vérification des conditions de victoire
def verifier_victoire(plateau, joueur):
    conditions_victoire = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for condition in conditions_victoire:
        if all(plateau[position] == joueur for position in condition):
            return True
    return False

# Vérification du match nul
def verifier_match_nul(plateau):
    return all(case != " " for case in plateau)

# Intelligence artificielle de niveau moyen
def ia_moyenne(plateau, signe):
    adversaire = "X" if signe == "O" else "O"

    for i in range(9):
        if plateau[i] == " ":
            plateau[i] = signe
            if verifier_victoire(plateau, signe):
                plateau[i] = " "
                return i
            plateau[i] = " "

    for i in range(9):
        if plateau[i] == " ":
            plateau[i] = adversaire
            if verifier_victoire(plateau, adversaire):
                plateau[i] = " "
                return i
            plateau[i] = " "

    for choix_preferable in [4, 0, 2, 6, 8]:
        if plateau[choix_preferable] == " ":
            return choix_preferable

    cases_vides = [i for i, case in enumerate(plateau) if case == " "]
    return random.choice(cases_vides) if cases_vides else False

# Boucle principale du jeu
def jeu_tic_tac_toe():
    while True:
        plateau = initialiser_plateau()
        mode = input("Mode de jeu : 1 pour 2 joueurs, 2 pour jouer contre l'IA : ")

        ia_niveau = None
        if mode == "2":
            ia_niveau = input("Niveau IA : 1 (facile) ou 2 (moyen) : ")

        joueur_actuel = "X"
        while True:
            afficher_plateau(plateau)

            if mode == "2" and joueur_actuel == "O":
                print("Tour de l'IA...")
                position = ia_moyenne(plateau, "O") if ia_niveau == "2" else random.choice(
                    [i for i, case in enumerate(plateau) if case == " "]
                )
            else:
                try:
                    position = int(input(f"Joueur {joueur_actuel}, choisissez une case (1-9) : ")) - 1
                    if position < 0 or position > 8 or plateau[position] != " ":
                        print("Position invalide. Réessayez.")
                        continue
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un chiffre entre 1 et 9.")
                    continue

            plateau[position] = joueur_actuel

            if verifier_victoire(plateau, joueur_actuel):
                afficher_plateau(plateau)
                print(f"Le joueur {colorer_signe(joueur_actuel)} gagne ! 🎉")
                break
            elif verifier_match_nul(plateau):
                afficher_plateau(plateau)
                print("Match nul ! 🤝")
                break

            joueur_actuel = "O" if joueur_actuel == "X" else "X"

        rejouer = input("Voulez-vous rejouer ? (oui/non) : ").lower()
        if rejouer != "oui":
            print("Merci d'avoir joué !")
            break

if __name__ == "__main__":
    jeu_tic_tac_toe()



#Explications :
#Boucles : Utilisation de for et while pour parcourir les cases du plateau et gérer les tours de jeu.
#Conditions : Les if, else et elif permettent de vérifier la validité des actions et de décider du gagnant.
#Listes : Le plateau est une liste de 9 éléments, représentant les cases du jeu.
#Fonctions de base : input, int, print, range, etc., sont utilisés pour interagir avec l'utilisateur et manipuler les données.
#Ce code est simple, pédagogique et exploite uniquement les concepts fondamentaux de Python.

