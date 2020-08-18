import math
import random

import Board.module_board
import ProblemGenerator.difficulties as difficulties
from ProblemGenerator.module_problem_base_class import ProblemFinder


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


class RecursiveBacktracking(ProblemFinder):

    def __init__(self, board: Board, seed: int, log_name: str):
        super().__init__(board, seed, log_name)
        self.board = board
        self.set_values = {}
        self.initialize_set_values()

    def return_problem_solution(self):
        finished = False
        x = 0
        y = 0
        val_index = 0
        while not finished:
            new_parameter = self.recursive(x, y, val_index)
            finished = new_parameter[0]
            x = new_parameter[1]
            y = new_parameter[2]
            val_index = new_parameter[3]
        return self.board

    def recursive(self, x: int, y: int, val_index: int):
        """
        Checks for this position if the value fits.
        :param x: x position in the sudoku board
        :param y: y position in the sudoku board
        :param val_index: index for which value to use from the set_values
        :return: an array of the values for the new method call
        """
        if y == self.board.get_board_length() and x == 0:
            return [True, x, y, val_index]

        if y < self.board.get_board_length() and x < self.board.get_board_length():
            val = self.set_values[get_identifier(x, y)][val_index]
            row = self.check_row(y, val)
            column = self.check_column(x, val)
            box = self.check_box(x, y, val)
            if row and column and box:
                self.reset_following_set_values(x, y)
                self.board.set_value(x, y, val)
                self.set_values[get_identifier(x, y)].remove(val)
                if x == self.board.get_board_length() - 1:
                    return [False, 0, y + 1, 0]
                else:
                    return [False, x + 1, y, 0]
            elif val_index + 1 >= len(self.set_values[get_identifier(x, y)]):
                self.board.set_value(x, y, -1)
                if x == 0:
                    return [False, self.board.get_board_length() - 1, y - 1, 0]
                else:
                    return [False, x - 1, y, 0]
            else:
                return [False, x, y, val_index + 1]

    def return_problem(self, difficulty: difficulties):
        if self.board.get_value(0, 0) is None:
            self.return_problem_solution()
        for val in range(0, math.floor(self.board.get_max_number_of_entries() * difficulty)):
            x = random.randint(0, self.board.get_board_length() - 1)
            y = random.randint(0, self.board.get_board_length() - 1)
            self.board.set_value(x, y, -1)

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
