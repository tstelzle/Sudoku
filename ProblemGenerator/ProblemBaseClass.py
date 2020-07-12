from abc import ABC, abstractmethod
from Board.Board import Board
import math


class ProblemFinder(ABC):

    @abstractmethod
    def __init__(self, board: Board):
        self.board = board

    @abstractmethod
    def returnProblem(self):
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
        for y in range(0, self.board.getBoardLength()):
            value = self.board.getValue(x, y)
            if value == val:
                return False
        return True

    def checkRow(self, y: int, val: int):
        for x in range(0, self.board.getBoardLength()):
            value = self.board.getValue(x, y)
            if value == val:
                return False
        return True

    def getBoxEdgeMin(self, val: int):
        return self.getMultiplier(val) * self.board.length

    def getBoxEdgeMax(self, val: int):
        return ((self.getMultiplier(val) + 1) * self.board.length)

    def getMultiplier(self, val: int):
        if val == 0:
            return 0
        return math.floor(val / self.board.length)
