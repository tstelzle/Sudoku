import math
import random
from abc import ABC, abstractmethod

import ProblemGenerator.difficulties as difficulties
from Board.module_board import Board


class ProblemFinder(ABC):

    @abstractmethod
    def __init__(self, board: Board, seed: int, log_name: str):
        self.board = board
        self.log_name = log_name
        random.seed(seed)

    def return_problem(self, difficulty: difficulties):
        """
        Calcualtes the board with the starting numbers for the sudoku.
        :return: None
        """
        if self.board.get_value(0, 0) is None:
            self.return_problem_solution()
        for val in range(0, math.floor(self.board.get_max_number_of_entries() * difficulty)):
            x = random.randint(0, self.board.get_board_length() - 1)
            y = random.randint(0, self.board.get_board_length() - 1)
            self.board.set_value(x, y, -1)

    @abstractmethod
    def return_problem_solution(self):
        """
        Calculates the solution the problem given in returnProblem.
        :return: None
        """
        pass

    def check_box(self, x: int, y: int, val: int):
        """
        Checks if the val can be entered in the box, identified by the given x and y value.
        :param x: x-axis of the sudoku field
        :param y: y-axis of the sudoku field
        :param val: value you want to set
        :return: Bool
        """
        min_x = self.get_box_edge_min(x)
        max_x = self.get_box_edge_max(x)
        min_y = self.get_box_edge_min(y)
        max_y = self.get_box_edge_max(y)
        for x_1 in range(min_x, max_x):
            for y_1 in range(min_y, max_y):
                value = self.board.get_value(x_1, y_1)
                if value == val:
                    return False
        return True

    def check_column(self, x: int, val: int):
        """
        Checks if it is possible to insert val in given x-axis column.
        :param x: x-axis of the sudoku field
        :param val: value you want to set
        :return: Bool
        """
        for y in range(0, self.board.get_board_length()):
            value = self.board.get_value(x, y)
            if value == val:
                return False
        return True

    def check_row(self, y: int, val: int):
        """
        Checks if it is possible to insert val in given y-axis row.
        :param y: y-axis of the sudoku field
        :param val: value you want to set
        :return: Bool
        """
        for x in range(0, self.board.get_board_length()):
            value = self.board.get_value(x, y)
            if value == val:
                return False
        return True

    def get_box_edge_min(self, val: int):
        """
        Returns the minimal value of the box specified by the given multiplier.
        :param val: before processed multiplier
        :return: int
        """
        return self.get_multiplier(val) * self.board.length

    def get_box_edge_max(self, val: int):
        """
        Returns the maximal value of the box specified by the given multiplier.
        :param val: before processed multiplier
        :return: int
        """
        return (self.get_multiplier(val) + 1) * self.board.length

    def get_multiplier(self, val: int):
        """
        Returns the multiplier, which basically is the current box of the given x or y field.
            Counted from top left to right(x) or bottom (y).
        :param val: x or y axis value of the current position in the sudoku field
        :return: int
        """
        if val == 0:
            return 0
        return math.floor(val / self.board.length)
