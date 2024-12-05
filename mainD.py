# Tic Tac Toe - Mode de jeu direct avec saisie de plateau

# Affiche le plateau sous forme de grille
def display_board(board):
    for row in board:
        print(" | ".join(row))
    print("-" * 9)

# Vérifie si un joueur a gagné
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Vérifie si le plateau est plein (match nul)
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Boucle principale de jeu
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        display_board(board)
        print(f"Joueur {current_player}, entrez le plateau complet :")
        for i in range(3):
            board[i] = input(f"Ligne {i + 1} (séparée par des espaces) : ").split()

        # Vérifie la victoire ou le nul après chaque mise à jour
        if check_winner(board, current_player):
            display_board(board)
            print(f"Joueur {current_player} gagne ! 🎉")
            break
        elif is_draw(board):
            display_board(board)
            print("Match nul ! 🤝")
            break

        # Change de joueur
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
