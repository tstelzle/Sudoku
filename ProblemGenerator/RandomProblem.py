from ProblemGenerator.ProblemBaseClass import ProblemFinder

# seed the pseudorandom number generator
from random import seed
from random import random
from Board.Board import Board

class RandomProblem(ProblemFinder):
    super

    def __init__(self, board: Board):
        self.board = board

    def returnProblem(self, s: int):
        """

        :param s: value for the seed
        :return:
        """
        # seed random number generator
        seed(s)
        # generate some random numbers
        # print(random(), random(), random())
        self.board.setValue(0, 0, 1)
        self.board.setValue(1, 0, 1)
        self.board.setValue(4, 0, 1)
        self.board.setValue(4, 4, 1)


    def returnProblemSolution(self):
        """

        :return:
        """