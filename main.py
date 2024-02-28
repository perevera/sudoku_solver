from typing import List, Tuple
import sys
import copy


def accomplish(input_board, x, i, j):
    """
    Check if value x in the position (i, j) of the input board accomplishes all restrictions
    :return: True if x is a valid candidate, False elsewhere
    """
    ret = True

    # rows
    row_set = set(input_board[i])
    if x in row_set:
        ret = False     # row NOK

    # columns
    transposed_board = list(zip(*input_board))
    col_set = set(transposed_board[j])
    if x in col_set:
        ret = False     # column NOK

    # blocks
    i_1 = 3 * (i // 3)
    i_2 = 3 * (i // 3) + 3
    j_1 = 3 * (j // 3)
    j_2 = 3 * (j // 3) + 3
    block_set = set()
    for n in range(i_1, i_2):
        for m in range(j_1, j_2):
            block_set.add(input_board[n][m])
    if x in block_set:
        ret = False     # block NOK

    return ret


def find(input_board: List[List[str]]) -> List[List[str]]:
    """
    Recursively look for solutions for the given board
    :param input_board: input board
    :return: the solution board
    """
    # look for solutions starting with the first unknown position
    for i in range(0, 9):
        for j in range(0, 9):
            if input_board[i][j] == '.':
                for x in range(1, 10):
                    if accomplish(input_board, str(x), i, j):
                        test_board = copy.deepcopy(input_board)
                        input_board[i][j] = str(x)
                        print_sudoku(input_board, highlight=(i, j))
                        ret = find(input_board)
                        if ret:
                            return ret
                        else:
                            input_board = test_board
                return []

    return input_board


def print_sudoku(board: List[List[str]], highlight: Tuple[int, int] = None):
    """
    Pretty print the given sudoku board, highlighting red a particular position, if any
    :param board: sudoku board
    :param highlight: coordinates of the position to be highlighted
    :return: None
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if highlight and i == highlight[0] and j == highlight[1]:
                print('\033[91m' + board[i][j] + '\033[0m', end=" ")
            else:
                print(board[i][j], end=" ")
        print(flush=True)
    print('\n')


def solve_sudoku(input_board: List[List[str]]) -> List[List[str]]:
    """
    Main function to solve a sudoku
    :param input_board: the input board
    :return: the output board (unique solution), None if no solution has been found
    """
    solution = find(input_board)
    if solution:
        print("Solved!")
        return solution

    return []


def parse_input_file(input_file: str) -> List[List[str]]:
    """
    Process all lines from the input file to extract data
    :param input_file: input file name with path
    :return: initial board
    """
    board = []

    with open(input_file, 'r') as file:
        for line in file:
            row = [c for c in line.strip()]
            board.append(row)

    return board


def main(input_file: str):
    """
    Entry point
    :param input_file: input file containing the starting sudoku puzzle
    :return: None
    """
    print_sudoku(solve_sudoku(parse_input_file(input_file)))


if __name__ == '__main__':
    main(sys.argv[1])
