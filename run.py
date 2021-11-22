"""
KEYS:
X = Hit Battleship
O = Miss Battleship
' ' = Spaces Availiable To Guess

user_board = The board where the user's ships are placed
computer_board = The board where the computer's ships are placed
Letters_to_numbers = Allocating a number to the first 8 letter of the alphabet
"""
# ------------------------- Game Boards

user_board = [[' '] * 9 for x in range(9)]
computer_board = [[' '] * 9 for x in range(9)]

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


"""
def user_input():


def create_ships():


def place_ships():


def check_ship_fits:



def check_for_overlap():


def hit_ship_counter():


def turn():


"""