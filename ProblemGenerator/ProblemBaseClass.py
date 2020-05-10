from abc import abstractmethod
from Board.Board import Board

class ProblemFinder:

    @abstractmethod
    def __init__(self, board: Board):
        self.board = board

    @abstractmethod
    def returnProblem(self):
        pass

    @abstractmethod
    def returnProblemSolution(self):
        pass