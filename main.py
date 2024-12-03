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

def jouer():
    plateau = [" " for _ in range(9)] 
    joueur_courant = "X"  

    while True:
        afficher_plateau(plateau)
        print(f"C'est le tour de {joueur_courant}. Choisissez une case (1-9):")
        
        
        try:
            choix = int(input()) - 1
            if choix < 0 or choix > 8 or plateau[choix] != " ":
                print("Case invalide, essayez à nouveau.")
                continue
        except ValueError:
            print("Entrée invalide, entrez un nombre entre 1 et 9.")
            continue

        plateau[choix] = joueur_courant

        if verifier_gagnant(plateau, joueur_courant):
            afficher_plateau(plateau)
            print(f"Félicitations! {joueur_courant} a gagné!")
            break

      
        if jeu_termine(plateau):
            afficher_plateau(plateau)
            print("Match nul!")
            break

       
        joueur_courant = "O" if joueur_courant == "X" else "X"

if __name__ == "__main__":
    jouer()
