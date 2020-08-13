import math
from abc import ABC, abstractmethod

import ProblemGenerator.difficulties as difficulties
from Board.Board import Board


class ProblemFinder(ABC):

    @abstractmethod
    def __init__(self, board: Board):
        self.board = board

    @abstractmethod
    def returnProblem(self, difficulty: difficulties):
        """
        Returns the board with the starting numbers for the sudoku.
        :return: Board
        """
        pass

    @abstractmethod
    def returnProblemSolution(self):
        """
        Returns the solution the problem given in returnProblem.
        :return: Board
        """
        pass

    def checkBox(self, x: int, y: int, val: int):
        """
        Checks if the val can be entered in the box, identiefied by the given x and y value.
        :param x: x-axis of the sudoku field
        :param y: y-axis of the sudoku field
        :param val: value you want to set
        :return: Bool
        """
        minX = self.getBoxEdgeMin(x)
        maxX = self.getBoxEdgeMax(x)
        minY = self.getBoxEdgeMin(y)
        maxY = self.getBoxEdgeMax(y)
        for x_1 in range(minX, maxX):
            for y_1 in range(minY, maxY):
                value = self.board.getValue(x_1, y_1)
                if value == val:
                    return False
        return True

    def checkColumn(self, x: int, val: int):
        """
        Checks if it is possible to insert val in given x-axis column.
        :param x: x-axis of the sudoku field
        :param val: value you want to set
        :return: Bool
        """
        for y in range(0, self.board.getBoardLength()):
            value = self.board.getValue(x, y)
            if value == val:
                return False
        return True

    def checkRow(self, y: int, val: int):
        """
        Checks if it is possible to insert val in given y-axis row.
        :param y: y-axis of the sudoku field
        :param val: value you want to set
        :return: Bool
        """
        for x in range(0, self.board.getBoardLength()):
            value = self.board.getValue(x, y)
            if value == val:
                return False
        return True

    def getBoxEdgeMin(self, val: int):
        """
        Returns the minimal value of the box specified by the given multiplier.
        :param val: before processed multiplier
        :return: int
        """
        return self.getMultiplier(val) * self.board.length

    def getBoxEdgeMax(self, val: int):
        """
        Returns the maximal value of the box specified by the given multiplier.
        :param val: before processed multiplier
        :return: int
        """
        return ((self.getMultiplier(val) + 1) * self.board.length)

    def getMultiplier(self, val: int):
        """
        Returns the multiplier, which basically is the current box of the given x or y field. Counted from top left to right(x) or bottom (y).
        :param val: x or y axis value of the current postion in the sudoku field
        :return: int
        """
        if val == 0:
            return 0
        return math.floor(val / self.board.length)
