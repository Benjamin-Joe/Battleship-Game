"""
KEYS:
X = Hit Battleship
O = Miss Battleship
' ' = Spaces Availiable To Guess
"""
# ------------------------- Game Boards

guess_board = [[' '] * 9 for x in range(9)]
hidden_board = [[' '] * 9 for x in range(9)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'f': 5, 'G': 6, 'H': 7, 'I': 8}


def print_board(board):
    """
    Creating the view of the gameboards
    """
    print('   A B C D E F G H I')
    print('  -------------------')
    row_number = 1

    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


print_board(guess_board)
