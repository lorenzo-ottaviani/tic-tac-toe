import random
def afficher_plateau(plateau):
    print(f"{plateau[0]} | {plateau[1]} | {plateau[2]}")
    print("---------")
    print(f"{plateau[3]} | {plateau[4]} | {plateau[5]}")
    print("---------")
    print(f"{plateau[6]} | {plateau[7]} | {plateau[8]}")


def verifier_gagnant(plateau, joueur):
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    for combinaison in combinaisons_gagnantes:
        if plateau[combinaison[0]] == plateau[combinaison[1]] == plateau[combinaison[2]] == joueur:
            return True
    return False


def jeu_termine(plateau):
    return " " not in plateau


def ia_facile(plateau):
    cases_vides = [i for i, case in enumerate(plateau) if case == " "]
    return random.choice(cases_vides)


def ia_moyenne(plateau, joueur_courant):
    adversaire = "O" if joueur_courant == "X" else "X"
    

    for case in range(9):
        if plateau[case] == " ":
            plateau[case] = joueur_courant
            if verifier_gagnant(plateau, joueur_courant):
                return case
            plateau[case] = " "

  
    for case in range(9):
        if plateau[case] == " ":
            plateau[case] = adversaire
            if verifier_gagnant(plateau, adversaire):
                plateau[case] = " "
                return case
            plateau[case] = " "

    return ia_facile(plateau)


def minimax(plateau, profondeur, est_maximisant, joueur_courant):
    adversaire = "O" if joueur_courant == "X" else "X"


    if verifier_gagnant(plateau, "X"):
        return -1
    if verifier_gagnant(plateau, "O"):
        return 1
    if jeu_termine(plateau):
        return 0

   
    if est_maximisant:
        meilleur_score = -float('inf')
        for i in range(9):
            if plateau[i] == " ":
                plateau[i] = "O"
                score = minimax(plateau, profondeur + 1, False, joueur_courant)
                plateau[i] = " "
                meilleur_score = max(score, meilleur_score)
        return meilleur_score

    else:
        meilleur_score = float('inf')
        for i in range(9):
            if plateau[i] == " ":
                plateau[i] = "X"
                score = minimax(plateau, profondeur + 1, True, joueur_courant)
                plateau[i] = " "
                meilleur_score = min(score, meilleur_score)
        return meilleur_score

def ia_difficile(plateau, joueur_courant):
    meilleur_coup = None
    meilleur_score = -float('inf')

    for i in range(9):
        if plateau[i] == " ":
            plateau[i] = "O"
            score = minimax(plateau, 0, False, joueur_courant)
            plateau[i] = " "
            if score > meilleur_score:
                meilleur_score = score
                meilleur_coup = i

    return meilleur_coup

def choisir_coup_ia(plateau, niveau_ia, joueur_courant):
    if niveau_ia == "facile":
        return ia_facile(plateau)
    elif niveau_ia == "moyenne":
        return ia_moyenne(plateau, joueur_courant)
    elif niveau_ia == "difficile":
        return ia_difficile(plateau, joueur_courant)

def jouer():
    plateau = [" " for _ in range(9)]  
    joueur_courant = "X" 
    niveau_ia = input("Choisissez le niveau de difficulté de l'IA (facile, moyenne, difficile): ").lower()

    while True:
        afficher_plateau(plateau)
        if joueur_courant == "X":
            print("C'est votre tour. Choisissez une case (1-9):")
            try:
                choix = int(input()) - 1
                if choix < 0 or choix > 8 or plateau[choix] != " ":
                    print("Case invalide, essayez à nouveau.")
                    continue
            except ValueError:
                print("Entrée invalide, entrez un nombre entre 1 et 9.")
                continue
            plateau[choix] = joueur_courant
        else:
            print(f"C'est le tour de l'IA ({joueur_courant}). L'IA joue...")
            choix = choisir_coup_ia(plateau, niveau_ia, joueur_courant)
            plateau[choix] = joueur_courant
            print(f"L'IA a choisi la case {choix + 1}")

        if verifier_gagnant(plateau, joueur_courant):
            afficher_plateau(plateau)
            print(f"Félicitations! {joueur_courant} a gagné!")
            break

        if jeu_termine(plateau):
            afficher_plateau(plateau)
            print("Match nul!")
            break

        joueur_courant = "O" if joueur_courant == "X" else "X"  # Changer de joueur

if __name__ == "__main__":
    jouer()
