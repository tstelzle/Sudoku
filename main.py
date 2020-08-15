import sys
import time

import ProblemGenerator.difficulties as difficulties
from Board.Board import Board
from ProblemGenerator import BruteForceBacktracking
from ProblemGenerator import ProblemBaseClass
from output import PdfService


def run_solution(sudoku: Board, algorithm_class: ProblemBaseClass):
    """
    Runs the given algorithm and returns the sudoku solution.
    :param sudoku: the sudoku board
    :param algorithm_class: the class of the algorithm to use
    :return: the sudoku board
    """
    algorithm = algorithm_class(sudoku)
    pdf_printer = PdfService.PdfPrinter(sudoku)
    print('The Sudoku Solution:')
    start_time = time.time()
    algorithm.returnProblemSolution()
    end_time = time.time()
    print('Duration: ' + str(end_time - start_time) + "s")
    sudoku.printBoard()
    title = 'Sudoku-Solution'
    pdf_printer.print_sudoku(title, get_file_name(sudoku, title))
    return sudoku


def get_file_name(sudoku: Board, title: str):
    """
    Returns the filename of the pdf to make, with a timestamp
    :param sudoku: the sudoku board
    :param title: the title of the pdf
    :return: filename
    """
    timestamp = str(int(time.time()))
    board_size = str(sudoku.length)
    return title + "_" + timestamp + "_" + board_size


def run_problem(sudoku: Board, algorithm_class: ProblemBaseClass, difficulty: difficulties):
    """
    Runs the given algorithm and returns the sudoku problem.
    :param sudoku: the sudoku board
    :param algorithm_class: the class of the algorithm to use
    :param difficulty: the difficulty of the problem specified by the enum
    :return: the sudoku board
    """
    algorithm = algorithm_class(sudoku)
    pdf_printer = PdfService.PdfPrinter(sudoku)
    print('The Sudoku Problem:')
    algorithm.returnProblem(difficulty)
    sudoku.printBoard()
    title = 'Sudoku-Problem'
    pdf_printer.print_sudoku(title, get_file_name(sudoku, title))
    return sudoku


def run_solution_and_problem(sudoku: Board, algorithm_class: ProblemBaseClass, difficulty=difficulties.HARD):
    """
    Runs the two methods 'runSolution' and 'runProblem' to calculate the sudoku solution and problem.
    :param sudoku: the sudoku board
    :param algorithm_class: the class of the algorithm to use
    :param difficulty: the difficulty of the problem specified by the enum
    :return:
    """
    sudoku_sol = run_solution(sudoku, algorithm_class)
    sudoku_prob = run_problem(sudoku_sol, algorithm_class, difficulty)
    return [sudoku_sol, sudoku_prob]


def print_board_information(sudoku: Board):
    """
    Prints the information about the board size.
    :param sudoku: the sudoku board
    :return: None
    """
    print('Length of the Board: ' + str(sudoku.length))
    print('Length of the BoardRow: ' + str(sudoku.board[0].length))
    print('Length of the Field: ' + str(sudoku.board[0].boardRow[0].length))
    print('Length of the FieldRow: ' + str(sudoku.board[0].boardRow[0].field[0].length))
    print("")


def read_board_parameter():
    """
    Reads the input parameters. And returns the size of the board.
    :return: int
    """
    if len(sys.argv) >= 1:
        return int(sys.argv[1])
    return -1


def main():
    board_size = read_board_parameter() if read_board_parameter() > 0 else 3
    sudoku = Board(board_size)
    print_board_information(sudoku)
    run_solution_and_problem(sudoku, BruteForceBacktracking.BruteForceBacktracking)


if __name__ == "__main__":
    main()
