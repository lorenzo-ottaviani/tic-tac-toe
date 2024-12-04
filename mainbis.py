def afficher_plateau(plateau):
    print(f"{plateau[0]} | {plateau[1]} | {plateau[2]}")
    print("--+---+--")
    print(f"{plateau[3]} | {plateau[4]} | {plateau[5]}")
    print("--+---+--")
    print(f"{plateau[6]} | {plateau[7]} | {plateau[8]}")

def verifier_victoire(plateau, joueur):
    combinaisons_victoires = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Lignes
                              (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colonnes
                              (0, 4, 8), (2, 4, 6)]  # Diagonales
    for comb in combinaisons_victoires:
        if plateau[comb[0]] == plateau[comb[1]] == plateau[comb[2]] == joueur:
            return True
    return False

def jeu_morpion():
    plateau = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    joueur_actuel = 'X'
    
    for tour in range(9):
        afficher_plateau(plateau)
        choix = int(input(f"Joueur {joueur_actuel}, choisissez une case (1-9): ")) - 1
        
        if plateau[choix] == ' ':
            plateau[choix] = joueur_actuel
        else:
            print("Cette case est déjà occupée. Essayez à nouveau.")
            continue
        
        if verifier_victoire(plateau, joueur_actuel):
            afficher_plateau(plateau)
            print(f"Joueur {joueur_actuel} a gagné !")
            break
        
        # Changer de joueur
        joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'
    else:
        afficher_plateau(plateau)
        print("Match nul !")

jeu_morpion()
