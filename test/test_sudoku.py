from main import solve_sudoku
from input.sudoku_1 import input, solution


def test_sudoku():
    """
    Assert the sample input gives the right value
    :return:
    """
    output = solve_sudoku(input)
    assert output == solution
