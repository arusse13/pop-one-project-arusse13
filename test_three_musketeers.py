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

def test_create_board():
    create_board()
    assert at((0,0)) == R
    assert at((0,4)) == M
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M    
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A1') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    assert ('A0'== location_to_string((0,0)))
    ## Replace with tests

def test_at():
    assert ('M' or 'R' or '-' == at((0,0)))
    ## Replace with tests

def test_all_locations():
    assert ('M' or 'R' or '-' == all_locations())
    ## Replace with tests

def test_adjacent_location():
    assert ((0,1) == adjacent_location((0,0),right))
    ## Replace with tests
    
def test_is_legal_move_by_musketeer():
    assert (True == is_legal_move((0,4),left))
    ## Replace with tests
    
def test_is_legal_move_by_enemy():
    assert (True == is_legal_move_by_enemy((0,0),right))
    ## Replace with tests

def test_is_legal_move():
    assert (True == is_legal_move((0,0),right))
    ## Replace with tests

def test_can_move_piece_at():
    assert (True == can_move_piece_at((0,0)))
    ## Replace with tests

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    assert ([]==possible_moves_from((0,0)))
    ## Replace with tests

def test_is_legal_location():
    assert (True == is_legal_location((0,0)))
    ## Replace with tests

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


