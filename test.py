import random

# Initialisation du plateau
def init_board():
    return [" " for _ in range(9)]

# Affichage du plateau
def display_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 5)
    print("\n")

# Vérifie les conditions de victoire
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

# Vérifie si le plateau est plein (match nul)
def is_draw(board):
    return all(cell != " " for cell in board)

# IA de niveau moyen (prend des décisions un peu plus intelligentes)
def ia_medium(board, signe):
    opponent = "X" if signe == "O" else "O"

    # 1. Vérifie si l'IA peut gagner au prochain coup
    for i in range(9):
        if board[i] == " ":
            board[i] = signe
            if check_winner(board, signe):
                return i
            board[i] = " "

    # 2. Bloque l'adversaire s'il peut gagner au prochain coup
    for i in range(9):
        if board[i] == " ":
            board[i] = opponent
            if check_winner(board, opponent):
                board[i] = " "  # Rétablir le plateau
                return i
            board[i] = " "

    # 3. Sinon, joue sur une case centrale ou un coin si possible
    for preferred_move in [4, 0, 2, 6, 8]:
        if board[preferred_move] == " ":
            return preferred_move

    # 4. Choix aléatoire si aucune des conditions ci-dessus n'est remplie
    empty_positions = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(empty_positions) if empty_positions else False

# Boucle principale du jeu
def tic_tac_toe():
    while True:
        board = init_board()
        mode = input("Choisissez le mode de jeu : 1 pour 2 joueurs, 2 pour jouer contre une IA : ")

        ia_level = None
        if mode == "2":
            ia_level = input("Choisissez le niveau de l'IA : 1 (facile) ou 2 (moyen) : ")

        current_player = "X"
        while True:
            display_board(board)

            if mode == "2" and current_player == "O":  # Tour de l'IA
                print("Tour de l'IA...")
                if ia_level == "2":
                    position = ia_medium(board, "O")
                else:
                    position = ia_medium(board, "O")
            else:
                try:
                    position = int(input(f"Joueur {current_player}, choisissez une case (1-9) : ") -1)
                    if position < 0 or position > 8 or board[position] != " ":
                        print("Position invalide. Réessayez.")
                        continue
                except ValueError:
                    print("Veuillez entrer un chiffre valide (1-9).")
                    continue

            # Place le signe sur le plateau
            board[position] = current_player

            # Vérifie les conditions de victoire ou de match nul
            if check_winner(board, current_player):
                display_board(board)
                if mode == "2" and current_player == "O":
                    print("Vous avez perdu ! 💔")
                else:
                    print(f"Le joueur {current_player} gagne ! 🎉")
                break
            elif is_draw(board):
                display_board(board)
                print("Match nul ! 🤝")
                break

            # Change de joueur
            current_player = "O" if current_player == "X" else "X"

        # Proposer une nouvelle partie avec mode progressif
        replay = input("Voulez-vous jouer une nouvelle partie ? (oui/non) : ").lower()
        if replay != "oui":
            print("Merci d'avoir joué !")
            break

if __name__ == "__main__":
    tic_tac_toe()






 # Fonctionnalités :
#Mode de jeu :
#2 joueurs humains.
#Joueur contre une IA basique.
#Intelligence Artificielle :

#L'IA joue de manière aléatoire en choisissant une case vide.
#Vérifications intégrées :

#Empêche les joueurs de jouer sur une case déjà occupée.
#Détecte automatiquement les victoires, défaites ou matchs nuls.
#Expérience utilisateur :

#Affiche le plateau après chaque tour.
#Messages clairs pour guider les joueurs.
#Instructions :
#Exécutez le code dans Visual Studio Code.
#Suivez les instructions pour choisir le mode et jouer.
#Pour aller plus loin :
#Améliorer l’IA : Implémentez un algorithme comme le Minimax pour rendre l’IA plus intelligente.
#Interface graphique : Ajoutez une interface graphique avec des bibliothèques comme Tkinter ou Pygame.
#Souhaitez-vous des améliorations ou des explications sur une partie du code ?


#Conditions du jeu :
#Victoire :

#Un joueur aligne 3 signes identiques de manière horizontale, verticale ou diagonale.
#Exemple : X X X dans une rangée ou une diagonale.
#Match nul :

#Le plateau est rempli sans qu’aucun joueur ne parvienne à aligner 3 signes.
#Aucun gagnant.
#Défaite :

#Dans un mode où le joueur affronte une IA, la défaite correspond à une victoire de l'IA.





