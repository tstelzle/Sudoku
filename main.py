import copy
import sys
import threading
import time

from module_problem_generator import *
from module_logger import logger as log
from module_board import Board
from module_output import pdf_service


def get_seed():
    return int(time.time())


def get_timestamp():
    return str(int(time.time()))


def get_log_file_name(class_name: str):
    return class_name + '_' + get_timestamp()


def run_solution(sudoku: Board, algorithm_class: module_problem_base_class, seed: int, printing: bool, log_name=None):
    """
    Runs the given algorithm and returns the sudoku solution.
    :param log_name: log file name
    :param seed: seed value
    :param printing: Bool value if the pages should be printed
    :param sudoku: the sudoku board
    :param algorithm_class: the class of the algorithm to use
    :return: the sudoku board
    """
    if log_name is None:
        log_name = get_log_file_name(algorithm_class.__name__)
    algorithm = algorithm_class(sudoku, seed, log_name)
    title = 'Sudoku-Solution'
    log.append_to_log(log_name, title)
    start_time = time.time()
    algorithm.return_problem_solution()
    end_time = time.time()
    duration_string = 'Duration: ' + str(end_time - start_time) + 's'
    log.append_to_log(log_name, duration_string)
    log.append_to_log(log_name, "Seed: " + str(seed))
    log.append_date(log_name)
    log.append_to_log(log_name, algorithm.board.board_to_string())
    if printing:
        pdf_printer = pdf_service.PdfPrinter(algorithm.board)
        pdf_printer.print_sudoku(title, get_file_name(sudoku, title, algorithm_class.__name__))
    return algorithm.board


def get_file_name(sudoku: Board, title: str, algorithm_name: str):
    """
    Returns the filename of the pdf to make, with a timestamp
    :param algorithm_name: classname of the algorithm
    :param sudoku: the sudoku board
    :param title: the title of the pdf
    :return: filename
    """
    timestamp = get_timestamp()
    board_size = str(sudoku.length)
    return title + '_' + algorithm_name + '_' + timestamp + '_' + board_size


def run_problem(sudoku: Board, algorithm_class: module_problem_base_class, seed: int, difficulty: difficulties,
                printing: bool,
                log_name=None):
    """
    Runs the given algorithm and returns the sudoku problem.
    :param log_name: log file name
    :param seed: seed value
    :param sudoku: the sudoku board
    :param printing: Bool value if the pages should be printed
    :param algorithm_class: the class of the algorithm to use
    :param difficulty: the difficulty of the problem specified by the enum
    :return: the sudoku board
    """
    if log_name is None:
        log_name = get_log_file_name(algorithm_class.__name__)
    algorithm = algorithm_class(sudoku, seed, log_name)
    title = 'Sudoku-Problem'
    log.append_to_log(log_name, title)
    algorithm.return_problem(difficulty)
    log.append_to_log(log_name, algorithm.board.board_to_string())
    if printing:
        pdf_printer = pdf_service.PdfPrinter(algorithm.board)
        pdf_printer.print_sudoku(title, get_file_name(sudoku, title, algorithm_class.__name__))
    return algorithm.board


def run_solution_and_problem(sudoku: Board, algorithm_class: module_problem_base_class, seed: int, printing: bool,
                             difficulty=difficulties.HARD):
    """
    Runs the two methods 'runSolution' and 'runProblem' to calculate the sudoku solution and problem.
    :param seed: seed value
    :param sudoku: the sudoku board
    :param printing: Bool value if the pages should be printed
    :param algorithm_class: the class of the algorithm to use
    :param difficulty: the difficulty of the problem specified by the enum
    :return:
    """
    log_name = get_log_file_name(algorithm_class.__name__)
    sudoku_sol = run_solution(sudoku, algorithm_class, seed, printing, log_name)
    sudoku_prob = run_problem(sudoku_sol, algorithm_class, seed, difficulty, printing, log_name)
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


def main():
    print_sudoku = False
    board_size = 3

    if len(sys.argv) > 1:
        for argument in sys.argv:
            splitted_argument = argument[:2]
            if splitted_argument == "-p":
                print_sudoku = True
            elif splitted_argument == "-s":
                board_size = int(argument.split("=")[1])

    sudoku = Board(board_size)
    sudoku_2 = copy.deepcopy(sudoku)
    sudoku_3 = copy.deepcopy(sudoku)

    seed = get_seed()

    log.initialize_logger()
    pdf_service.initialize_printer()

    recursive_thread = threading.Thread(target=run_solution_and_problem,
                                        args=(sudoku, RecursiveBacktracking, seed, print_sudoku))
    recursive_thread.start()

    iterative_thread = threading.Thread(target=run_solution_and_problem,
                                        args=(sudoku_2, BruteForceBacktracking, seed, print_sudoku))
    iterative_thread.start()

    dynamic_thread = threading.Thread(target=run_solution_and_problem,
                                      args=(sudoku_3, DynamicBacktracking, seed, print_sudoku))
    dynamic_thread.start()

    recursive_thread.join()
    iterative_thread.join()
    dynamic_thread.join()


if __name__ == "__main__":
    main()
