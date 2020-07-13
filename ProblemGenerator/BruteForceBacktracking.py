import math
import random

import Board.Board
import ProblemGenerator.difficulties as difficulties
from ProblemGenerator.ProblemBaseClass import ProblemFinder


class BruteForceBacktracking(ProblemFinder):

    def __init__(self, board: Board):
        super().__init__(board)
        self.board = board
        self.setValues = {}
        self.initializeSetValues()

    def returnProblemSolution(self):
        y = 0
        x = 0
        while y < self.board.getBoardLength():
            while x < self.board.getBoardLength():
                if (y == self.board.getBoardLength() and x == 0):
                    return
                tried = []
                array = self.setValues[self.getIdentifier(x, y)]
                for val in array:
                    row = self.checkRow(y, val)
                    column = self.checkColumn(x, val)
                    box = self.checkBox(x, y, val)
                    tried.append(val)
                    if (row and column and box):
                        self.resetFollowingSetValues(x, y)
                        self.board.setValue(x, y, val)
                        self.setValues[self.getIdentifier(x, y)].remove(val)
                        if x == self.board.getBoardLength() - 1:
                            x = 0
                            y += 1
                        else:
                            x += 1
                        break
                    elif len(tried) >= len(self.setValues[self.getIdentifier(x, y)]):
                        self.board.setValue(x, y, -1)
                        if x == 0:
                            y -= 1
                            x = self.board.getBoardLength() - 1
                        else:
                            x -= 1
                        break

    def returnProblem(self, difficulty: difficulties):
        if self.board.getValue(0, 0) == None:
            self.returnProblemSolution()
        for val in range(0, math.floor(self.board.getMaxNumberOfEntries() * difficulty)):
            x = random.randint(0, self.board.getBoardLength() - 1)
            y = random.randint(0, self.board.getBoardLength() - 1)
            self.board.setValue(x, y, -1)

    def initializeSetValues(self):
        """
        Initializes the setValues dictionary, which stores which values can be used in the sudoku at this position.
        :return: None
        """
        for x in range(0, self.board.getBoardLength()):
            for y in range(0, self.board.getBoardLength()):
                self.setValues[self.getIdentifier(x, y)] = list(range(1, self.board.getBoardLength() + 1))

    def getIdentifier(self, x: int, y: int):
        """
        Returns the string which identifies the fields in the sudoku for the setValues dictionary.
        :param x: x-axis of the sudoku field
        :param y: y-axis of the sudoku field
        :return: identifier string
        """
        return str(x) + str(y)

    def resetFollowingSetValues(self, x: int, y: int):
        """
        Reset the values in the setValues dictionary after the given x,y position.
        :param x: x-axis of the sudoku field
        :param y: y-axis of the sudoku field
        :return: None
        """
        for x_1 in range(x + 1, self.board.getBoardLength()):
            self.setValues[self.getIdentifier(x_1, y)] = list(range(1, self.board.getBoardLength() + 1))
        for y_1 in range(y + 1, self.board.getBoardLength()):
            for x_1 in range(0, self.board.getBoardLength()):
                self.setValues[self.getIdentifier(x_1, y_1)] = list(range(1, self.board.getBoardLength() + 1))
