# The Three Musketeers Game

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    row_loc = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
    col_loc = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4}
    location = (row_loc[s[0]], col_loc[s[1]])
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4)).
       The function should raise ValueError exception if the input
       is outside of the correct range (between 'A' and 'E' for s[0] and
       between '1' and '5' for s[1]
       """
    return location
    #pass # Replace with code
    ## 181210 row_loc & col_loc added are dictionaries for location tuple referencing

def location_to_string(location):
    location_string=""
    row_str = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E"}
    col_str = {0:"1", 1:"2", 2:"3", 3:"4", 4:"5"}
    location_string = row_str[location[0]]+col_str[location[1]]
    """Returns the string representation of a location.
    Similarly to the previous function, this function should raise
    ValueError exception if the input is outside of the correct range
    """
    return location_string
    #pass # Replace with code
    ## 181210 row_str & col_str added are dictionaries for location string referencing

def at(location):
    """Returns the contents of the board at the given location.
    You can assume that input will always be in correct range."""
    return board[location[0]][location[1]]

def all_locations():
    global board
    location_contains = [board[0]+board[1]+board[2]+board[3]+board[4]]
    """Returns a list of all 25 locations on the board."""
    return location_contains
    #pass # Replace with code
    ## 181222 location_contains now concatination of board row lists
    ## IS THIS SUPPOSED TO LOCATION CONTENTS OR COORDINATES ??

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board.
       You can assume that input will always be in correct range."""
    (row, column) = location
    if direction == 'left':
        adj_location = (row, column-1)
    elif direction == 'right':
        adj_location = (row, column+1)
    elif direction == 'up':
        adj_location = (row-1, column)
    elif direction == 'down':
        adj_location = (row+1, column)
    return adj_location
    #pass # Replace with code
    ## 181227 modified location based on direction input

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'M'"""
    (row, column) = location
    (adj_row, adj_column) = adjacent_location(location,direction)
    try:
        if board[row][column] == 'M':
            if board[adj_row][adj_column] == 'R':
                return True
            else:
                raise ValueError('No Enemy in direction input')
        else:
            raise ValueError('No Musketeer at location input')
    except ValueError:
        print('No Enemy in direction input OR No Musketeer at location input')
        return False
    #pass # Replace with code
    ## 181227 calls adjacent_location function to check if directional cell is occupied for move
    ## returns True if location is occupied by 'M' and if neighbouring cell in direction is occupied by 'R'
    ## returns False by way of exception handling of raised ValueError

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction.
    You can assume that input will always be in correct range. Raises
    ValueError exception if at(location) is not 'R'"""
    (row, column) = location
    (adj_row, adj_column) = adjacent_location(location,direction)
    try:
        if board[row][column] == 'R':
            if board[adj_row][adj_column] == '-':
                return True
            else:
                raise ValueError('Not empty cell in direction input')
        else:
            raise ValueError('No Enemy at location input')
    except ValueError:
        print('No empty cell in direction input OR No Enemy at location input')
        return False
    #pass # Replace with code
    ## 181227 calls adjacent_location function to check if directional cell is occupied for move
    ## returns True if location is occupied by 'R' and if neighbouring cell in direction is occupied by '-'
    ## returns False by way of exception handling of raised ValueError

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction.
    You can assume that input will always be in correct range."""
    if is_legal_move_by_musketeer(location, direction) or is_legal_move_by_enemy(location, direction) == True:
        return True
    else:
        return False
    #pass # Replace with code
    ## 181227 combination of is_legal_move_by functions under one function which returns true if either are legel
    ## main program body checks if 'M' or 'R' are at location depending on who's move it is

def limiter(coordinate):
    if coordinate < 0:
        coordinate = 0
    elif coordinate > 4:
        coordinate = 4
    return coordinate

## 181227 added function added to keep cell traversing from 0 to 4

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available.
    You can assume that input will always be in correct range."""
    (row, column) = location
    if board[row][column] == 'R':
        if board[limiter(row+1)][column] == '-' or board[limiter(row-1)][column] == '-' or board[row][limiter(column+1)] == '-' or board[row][limiter(column-1)] == '-':
            return True
        else:
            return False
    elif board[row][column] == 'M':
        if board[limiter(row+1)][column] == 'R' or board[limiter(row-1)][column] == 'R' or board[row][limiter(column+1)] == 'R' or board[row][limiter(column-1)] == 'R':
            return True
        else:
            return False
    else:
        return False
    #pass # Replace with code
    ## 181227 tests whether there is an empty cell or enemy cell in any orthogonal to location
    ## limiter function used (in place of abs) to prevent negative indexing or indexing outside upper limit


def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is.
    You can assume that input will always be in correct range."""
    i=0
    j=0
    possible_move=False
    if who == 'M':
        for i in range(5):
            for j in range(5):
                if board[i][j] == 'M':
                    if can_move_piece_at((i,j)) == True:
                        possible_move=True

    elif who == 'R':
        for i in range(5):
            for j in range(5):
                if board[i][j] == 'R':
                    if can_move_piece_at((i,j)) == True:
                        possible_move=True
    return possible_move
    #pass # Replace with code
    ## 181227 uses for loop to check every board cell,
    ## upon a match to 'M' or 'R@ intiates can_move_piece_at function

def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, [].
       You can assume that input will always be in correct range."""
    possible_move_list = []
    (row, column) = location
    if board[row][column] == 'R':
        if board[limiter(row+1)][column] == '-' and (row+1) <= 4:
            possible_move_list.append('down')

        if board[limiter(row-1)][column] == '-' and (row-1) >= 0:
            possible_move_list.append('up')

        if board[row][limiter(column+1)] == '-' and (column+1) <= 4:
            possible_move_list.append('right')

        if board[row][limiter(column-1)] == '-' and (column-1) >= 0:
            possible_move_list.append('left')

    elif board[row][column] == 'M':
        if board[limiter(row+1)][column] == 'R' and (row+1) <= 4:
            possible_move_list.append('down')

        if board[limiter(row-1)][column] == 'R' and (row-1) >= 0:
            possible_move_list.append('up')

        if board[row][limiter(column+1)] == 'R' and (column+1) <= 4:
            possible_move_list.append('right')

        if board[row][limiter(column-1)] == 'R' and (column-1) >= 0:
            possible_move_list.append('left')

    return possible_move_list
    #pass # Replace with code
    ## 181227 uses if statements to check if orthagonal cell location are viable for move

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board.
    You can assume that input will always be a pair of integers."""
    (row, column) = location
    if row >= 0 and row <= 4:
        if column >= 0 and column <= 4:
            return True
    else:
        return False
    #pass # Replace with code
    ## 181227 uses if statements to test location coordinates are in index range
    
def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board.
    You can assume that input will always be in correct range."""
    
    return True
    #pass # Replace with code
    
def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples.
       You can assume that input will always be in correct range."""
    return []
    #pass # Replace with code

def make_move(location, direction):
    """Moves the piece in location in the indicated direction.
    Doesn't check if the move is legal. You can assume that input will always
    be in correct range."""
    "POSSIBLY NON-FRUITFUL FUNCTION - COMPARE BOARDS"
    return ()
    #pass # Replace with code

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual.
       You can assume that input will always be in correct range."""
    return ()
    #pass # Replace with code

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    return True
    #pass # Replace with code

#---------- Communicating with the user ----------
#----you do not need to modify code below unless you find a bug
#----a bug in it before you move to stage 3

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break
