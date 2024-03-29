import random

from module_board import Board
from .module_problem_base_class import ProblemFinder


def get_identifier(x: int, y: int):
    """
    Returns the string which identifies the fields in the sudoku for the setValues dictionary.
    :param x: x-axis of the sudoku field
    :param y: y-axis of the sudoku field
    :return: identifier string
    """
    return str(x) + "_" + str(y)


def random_list(length: int):
    """
    Builds and returns a randomized array of values from one to the given length.

    :param length: the range for the array
    :return: randomized array of values within the given length
    """
    sorted_list = list(range(1, length))
    return random.sample(sorted_list, len(sorted_list))


class BruteForceBacktracking(ProblemFinder):

    def __init__(self, board: Board, seed: int, log_name: str):
        super().__init__(board, seed, log_name)
        self.board = board
        self.set_values = {}
        self.initialize_set_values()

    def return_problem_solution(self):
        y = 0
        x = 0
        while y < self.board.get_board_length():
            while x < self.board.get_board_length():
                if y == self.board.get_board_length() and x == 0:
                    return self.board
                tried = []
                array = self.set_values[get_identifier(x, y)]
                for val in array:
                    row = self.check_row(y, val)
                    column = self.check_column(x, val)
                    box = self.check_box(x, y, val)
                    tried.append(val)
                    if row and column and box:
                        self.reset_following_set_values(x, y)
                        self.board.set_value(x, y, val)
                        self.set_values[get_identifier(x, y)].remove(val)
                        if x == self.board.get_board_length() - 1:
                            x = 0
                            y += 1
                        else:
                            x += 1
                        break
                    elif len(tried) >= len(self.set_values[get_identifier(x, y)]):
                        self.board.set_value(x, y, -1)
                        if x == 0:
                            y -= 1
                            x = self.board.get_board_length() - 1
                        else:
                            x -= 1
                        break

    def initialize_set_values(self):
        """
        Initializes the setValues dictionary, which stores which values can be used in the sudoku at this position.
        :return: None
        """
        for x in range(0, self.board.get_board_length()):
            for y in range(0, self.board.get_board_length()):
                self.set_values[get_identifier(x, y)] = random_list(self.board.get_board_length() + 1)

    def reset_following_set_values(self, x: int, y: int):
        """
        Reset the values in the setValues dictionary after the given x,y position.
        :param x: x-axis of the sudoku field
        :param y: y-axis of the sudoku field
        :return: None
        """
        for x_1 in range(x + 1, self.board.get_board_length()):
            self.set_values[get_identifier(x_1, y)] = random_list(self.board.get_board_length() + 1)
        for y_1 in range(y + 1, self.board.get_board_length()):
            for x_1 in range(0, self.board.get_board_length()):
                self.set_values[get_identifier(x_1, y_1)] = random_list(self.board.get_board_length() + 1)
