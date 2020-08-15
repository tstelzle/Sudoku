import math
import random

import Board.Board
import ProblemGenerator.difficulties as difficulties
from ProblemGenerator.ProblemBaseClass import ProblemFinder


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

    def __init__(self, board: Board):
        super().__init__(board)
        self.board = board
        self.set_values = {}
        self.initialize_set_values()

    def returnProblemSolution(self):
        finished = False
        x = 0
        y = 0
        val_index = 0
        count = 0
        while not finished:
            new_parameter = self.recursive(x, y, val_index, count)
            finished = new_parameter[0]
            x = new_parameter[1]
            y = new_parameter[2]
            val_index = new_parameter[3]
            count = new_parameter[4]

    def recursive(self, x: int, y: int, val_index: int, count: int):
        """
        Checks for this position if the value fits.
        :param x: x position in the sudoku board
        :param y: y position in the sudoku board
        :param val_index: index for which value to use from the set_values
        :param count: counts the amount of calls for this method
        :return: an array of all the input values
        """
        if y == self.board.getBoardLength() and x == 0:
            return [True, x, y, val_index, count]

        if y < self.board.getBoardLength() and x < self.board.getBoardLength():
            val = self.set_values[get_identifier(x, y)][val_index]
            row = self.checkRow(y, val)
            column = self.checkColumn(x, val)
            box = self.checkBox(x, y, val)
            if row and column and box:
                self.reset_following_set_values(x, y)
                self.board.setValue(x, y, val)
                self.set_values[get_identifier(x, y)].remove(val)
                if x == self.board.getBoardLength() - 1:
                    return [False, 0, y + 1, 0, count + 1]
                else:
                    return [False, x + 1, y, 0, count + 1]
            elif val_index + 1 >= len(self.set_values[get_identifier(x, y)]):
                self.board.setValue(x, y, -1)
                if x == 0:
                    return [False, self.board.getBoardLength() - 1, y - 1, 0, count + 1]
                else:
                    return [False, x - 1, y, 0, count + 1]
            else:
                return [False, x, y, val_index + 1, count + 1]

    def returnProblem(self, difficulty: difficulties):
        if self.board.getValue(0, 0) is None:
            self.returnProblemSolution()
        for val in range(0, math.floor(self.board.getMaxNumberOfEntries() * difficulty)):
            x = random.randint(0, self.board.getBoardLength() - 1)
            y = random.randint(0, self.board.getBoardLength() - 1)
            self.board.setValue(x, y, -1)

    def initialize_set_values(self):
        """
        Initializes the setValues dictionary, which stores which values can be used in the sudoku at this position.
        :return: None
        """
        for x in range(0, self.board.getBoardLength()):
            for y in range(0, self.board.getBoardLength()):
                self.set_values[get_identifier(x, y)] = random_list(self.board.getBoardLength() + 1)

    def reset_following_set_values(self, x: int, y: int):
        """
        Reset the values in the setValues dictionary after the given x,y position.
        :param x: x-axis of the sudoku field
        :param y: y-axis of the sudoku field
        :return: None
        """
        for x_1 in range(x + 1, self.board.getBoardLength()):
            self.set_values[get_identifier(x_1, y)] = random_list(self.board.getBoardLength() + 1)
        for y_1 in range(y + 1, self.board.getBoardLength()):
            for x_1 in range(0, self.board.getBoardLength()):
                self.set_values[get_identifier(x_1, y_1)] = random_list(self.board.getBoardLength() + 1)
