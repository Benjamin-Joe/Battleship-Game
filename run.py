import random

"""
KEYS:
X = Hit Battleship
O = Miss Battleship
' ' = Spaces Availiable To Guess
V = Vertical
H = Horizontal

user_board = The board where the user's ships are placed
computer_board = The board where the computer's ships are placed
Letters_to_numbers = Allocating a number to the first 8 letter of the alphabet
game_ships = the sizes of the ships the player and computer will use

"""
# ------------------------- Game Boards

user_board = [[' '] * 9 for x in range(9)]
user_guess_board = [[' '] * 9 for x in range(9)]
computer_guess_board = [[' '] * 9 for x in range(9)]
computer_board = [[' '] * 9 for x in range(9)]
game_ships = [2, 3, 3, 4, 5]
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

def place_ships(board):
    """
    Function for looping through all the game_ships
    and for checking that ships fit and don't go outside
    the game boundaries 
    """
    for ship_size in game_ships:
        while True:
            if board == computer_board:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0, 8), random.randint(0, 8)
                break




def check_ship_fits(ship_size, column, row, orientation):
    """
    Function for checking if ship fits on board
    """
    if orientation == "H":
        if column + ship_size > 9:
            return False
        else:
            return True
    else:
        if row + ship_size > 9:
            return False
        else:
            return True


print_board(user_board)
print_board(computer_board)

"""
def user_input():


def create_ships():





def check_ship_fits:


def check_for_overlap():


def hit_ship_counter():


def turn():


def play_game():

"""