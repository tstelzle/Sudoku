import math
import random
import copy

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


def split_identifier(identifier: str):
    """
    Splits the identifier and returns it as an array.
    :param identifier: identifier of the dictionary set_values
    :return: Array
    """
    return [int(i) for i in identifier.split("_")]


def random_list(length: int):
    """
    Builds and returns a randomized array of values from one to the given length.

    :param length: the range for the array
    :return: randomized array of values within the given length
    """
    sorted_list = list(range(1, length))
    return random.sample(sorted_list, len(sorted_list))


class DynamicBacktracking(ProblemFinder):

    def __init__(self, board: Board, seed: int, log_name: str):
        super().__init__(board, seed, log_name)
        self.board = board
        self.set_values = {}
        self.initialize_set_values()
        self.states = [copy.deepcopy(self.board)]
        self.repeat = [0]

    def return_problem_solution(self):
        id_min = ""
        while id_min is not None:
            id_min = self.find_minimum()
            if id_min is None:
                return
            coordinates = split_identifier(id_min)
            x = coordinates[0]
            y = coordinates[1]
            if len(self.set_values[id_min]) < self.repeat[-1]:
                self.insert_value(id_min)
            else:
                self.board = self.states[-1]
                del self.states[-1]
                del self.repeat[-1]

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

    def find_minimum(self):
        """
        Searches the identifier with the shortest array length in set_values.
        :return: Returns Identifier
        """
        minimum = self.board.get_board_length() + 1
        identifier = None
        for key, value in self.set_values.items():
            coordinates = split_identifier(key)
            if len(value) < minimum and self.board.is_empty(coordinates[0], coordinates[1]):
                minimum = len(value)
                identifier = key
        return identifier

    def insert_value(self, identifier: str):
        val = self.set_values[identifier][self.repeat[-1]]
        coordinates = split_identifier(identifier)
        x = coordinates[0]
        y = coordinates[1]
        self.board.set_value(x, y, val)
        for i in range(0, self.board.get_board_length()):
            self.set_values[get_identifier(i, y)].remove(val)
            self.set_values[get_identifier(x, i)].remove(val)
        self.repeat[-1] += 1
        self.repeat.append(0)
        self.states.append(copy.deepcopy(self.board))
