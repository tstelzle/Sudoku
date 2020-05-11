from abc import ABC, abstractmethod
from Board.Board import Board

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