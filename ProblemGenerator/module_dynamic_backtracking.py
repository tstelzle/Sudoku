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


def find_and_remove(arr: [], val: int):
    for value in arr:
        if value == val:
            arr.remove(val)


class DynamicBacktracking(ProblemFinder):

    def __init__(self, board: Board, seed: int, log_name: str):
        super().__init__(board, seed, log_name)
        self.board = board
        self.set_values = {}
        self.initialize_set_values()
        self.board_states = [copy.deepcopy(self.board)]
        self.values_states = [copy.deepcopy(self.set_values)]
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
            if len(self.set_values[id_min]) > self.repeat[-1]:
                self.insert_value(id_min)
            else:
                self.board = self.board_states[-1]
                self.set_values = self.values_states[-1]
                del self.board_states[-1]
                del self.values_states[-1]
                del self.repeat[-1]

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
        """

        :param identifier:
        :return:
        """
        val = self.set_values[identifier][self.repeat[-1]]
        coordinates = split_identifier(identifier)
        x = coordinates[0]
        y = coordinates[1]
        self.board.set_value(x, y, val)
        for i in range(0, self.board.get_board_length()):
            find_and_remove(self.set_values[get_identifier(i, y)], val)
            find_and_remove(self.set_values[get_identifier(x, i)], val)

        min_x = self.get_multiplier(x) * self.board.length
        max_x = (self.get_multiplier(x) + 1) * self.board.length
        min_y = self.get_multiplier(y) * self.board.length
        max_y = (self.get_multiplier(y) + 1) * self.board.length
        for x_1 in range(min_x, max_x):
            for y_1 in range(min_y, max_y):
                find_and_remove(self.set_values[get_identifier(x_1, y_1)], val)

        self.repeat[-1] += 1
        self.repeat.append(0)
        self.board_states.append(copy.deepcopy(self.board))
