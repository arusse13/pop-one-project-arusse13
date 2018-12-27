import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board2 =  [ [M, _, _, R, _],
            [_, _, _, _, _],
            [_, M, M, _, _],
            [R, _, _, _, R],
            [_, R, _, R, _] ]
# 181210 - board2 added, M winners

board3 =  [ [M, M, R, M, _],
            [_, _, R, _, R],
            [_, _, _, R, _],
            [R, R, _, _, _],
            [_, _, _, R, _] ]

# 181210 - board3 added, R winners

def test_create_board():
    create_board()
    assert at((0, 0)) == R
    assert at((0, 4)) == M
    assert at((2, 2)) == M
    assert at((4, 0)) == M

    #eventually add at least two more test cases
    ## 181210 - other two M position tests added because they must start at this positions
    ### add additional test that number of R's on new board equal to 22

def test_set_board():
    set_board(board1)
    assert at((0, 0)) == _
    assert at((1, 2)) == R
    assert at((1, 3)) == M
    #eventually add some board2 and at least 3 tests with it

    set_board(board2)
    assert at((0, 0)) == M
    assert at((1, 2)) == _
    assert at((3, 4)) == R
    ## 181210 - above tests for new board2

    set_board(board3)
    assert at((0, 0)) == M
    assert at((1, 2)) == R
    assert at((3, 4)) == _
    ## 181210 - above tests for new board3


def test_get_board():
    set_board(board1)
    assert board1 == get_board()

    set_board(board2)
    assert board2 == get_board()

    set_board(board3)
    assert board3 == get_board()
    #eventually add at least one more test with another board
    ## 181210 tests for new board2 and board3 added

def test_string_to_location():
    with pytest.raises(KeyError):
        string_to_location('X3')
        string_to_location('A8')
    assert string_to_location('A1') == (0, 0)
    assert string_to_location('C3') == (2, 2)
    assert string_to_location('E4') == (4, 3)
    #eventually add at least one more exception test and two more
    #test with correct inputs
    ## 181210 two more positional tests added C3 & E4
    ## 181210 exception type changed to KeyError because locations references are in dictionaries

def test_location_to_string():
    with pytest.raises(KeyError):
        location_to_string((1, 7))
        location_to_string((8, 3))
    assert location_to_string((0, 0)) == "A1"
    assert location_to_string((2, 2)) == "C3"
    assert location_to_string((4, 3)) == "E4"
    ## Replace with tests
    ## 181210 added location cross referencing tests and KeyError exceptions

def test_at():
    assert ('M' or 'R' or '-' == at((0, 0)))
    ## Replace with tests

def test_all_locations():
    assert ('M' or 'R' or '-' == all_locations())
    #assert (25 == len(all_locations())) - INCORRECT
    ## Replace with tests

def test_adjacent_location():
    assert ((0, 1) == adjacent_location((0, 0), right))
    assert ((0, 0) == adjacent_location((0, 1), left))
    assert ((0, 0) == adjacent_location((1, 0), up))
    assert ((1, 0) == adjacent_location((0, 0), down))
    ## Replace with tests
    ## 181222 added tests to verify direction modifications
    
def test_is_legal_move_by_musketeer():
    set_board(board1)
    assert (True == is_legal_move_by_musketeer((2, 2), left))
    assert (True == is_legal_move_by_musketeer((2, 2), up))
    assert (False == is_legal_move_by_musketeer((2, 2), down))
    assert (False == is_legal_move_by_musketeer((1, 1), right))
    assert (False == is_legal_move_by_musketeer((0, 1), right))
    ## Replace with tests
    ## 181227 added tests to verify that function returns true OR false for
    ## correct checks of 'M' and 'R' given location and direction
    ## as set out by test board1

def test_is_legal_move_by_enemy():
    set_board(board1)
    assert (True == is_legal_move_by_enemy((1, 2), left))
    assert (True == is_legal_move_by_enemy((1, 2), up))
    assert (False == is_legal_move_by_enemy((1, 2), down))
    assert (False == is_legal_move_by_enemy((1, 2), right))
    assert (False == is_legal_move_by_enemy((0, 1), right))
    ## Replace with tests
    ## 181227 added tests to verify that function returns true OR false for
    ## correct checks of 'R' and '_' given location and direction
    ## as set out by test board1

def test_is_legal_move():
    set_board(board1)
    assert (True == is_legal_move((2, 2), left))
    assert (True == is_legal_move((2, 2), up))
    assert (False == is_legal_move((2, 2), down))
    assert (False == is_legal_move((1, 1), right))
    assert (False == is_legal_move((0, 1), right))

    assert (True == is_legal_move((1, 2), left))
    assert (True == is_legal_move((1, 2), up))
    assert (False == is_legal_move((1, 2), down))
    assert (False == is_legal_move((1, 2), right))
    assert (False == is_legal_move((0, 1), right))
    ## Replace with tests
    ## 181227 copied tests for is_legal_move_by_enemy/musketeer function to test
    ## combining both functions in is_legal_move

def test_can_move_piece_at():
    set_board(board1)
    assert (True == can_move_piece_at((2, 2)))
    assert (True == can_move_piece_at((1, 2)))
    assert (False == can_move_piece_at((0, 0)))
    assert (False == can_move_piece_at((0, 3)))

    set_board(board2)
    assert (False == can_move_piece_at((0, 0)))
    assert (False == can_move_piece_at((2, 2)))
    assert (True == can_move_piece_at((4, 3)))
    assert (False == can_move_piece_at((2, 4)))

    set_board(board3)
    assert (False == can_move_piece_at((0, 0)))
    assert (True == can_move_piece_at((0, 3)))
    assert (True == can_move_piece_at((3, 1)))
    assert (False == can_move_piece_at((2, 4)))

    ## Replace with tests
    ## 181227 tests added verifying movement options for 'R', 'M' and '-' locations

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert (True == has_some_legal_move_somewhere('M'))
    assert (True == has_some_legal_move_somewhere('R'))

    set_board(board2)
    assert (False == has_some_legal_move_somewhere('M'))
    assert (True == has_some_legal_move_somewhere('R'))
    # Eventually put at least three additional tests here
    # with at least one additional board
    ## 181227 tests expanded with two boards

def test_possible_moves_from():
    set_board(board1)
    #['down', 'up', 'right', 'left']
    assert ([]==possible_moves_from((0,0)))
    assert (['up', 'right', 'left']==possible_moves_from((2, 2)))
    assert (['up', 'right', 'left']==possible_moves_from((4, 3)))
    assert ([] == possible_moves_from((0, 3)))
    ## Replace with tests
    ## 181227 tests added selecting locations of 'M', 'R' and '-'

def test_is_legal_location():
    assert (True == is_legal_location((0, 0)))
    assert (True == is_legal_location((2, 0)))
    assert (True == is_legal_location((4, 3)))
    assert (False == is_legal_location((5, 1)))
    assert (False == is_legal_location((-1, -3)))

    ## Replace with tests
    ## 181227 addtional tests added including outside of range tests

def test_is_within_board():
    assert (True == is_within_board((0,0),right))
    ## Replace with tests

def test_all_possible_moves_for():
    assert ([] ==  all_possible_moves_for(M))
    ## Replace with tests
    
def test_make_move():
    assert ((0,0) == make_move((0,1),left))
    # Replace with tests
    
def test_choose_computer_move():
    assert (()==choose_computer_move(M))
    # Replace with tests; should work for both 'M' and 'R'

def test_is_enemy_win():
    assert True
    # Replace with tests


