from ProblemGenerator.ProblemBaseClass import ProblemFinder

# seed the pseudorandom number generator
from random import seed
from random import randrange
from Board.Board import Board

class RandomProblem(ProblemFinder):
    super

    def __init__(self, board: Board):
        self.board = board

    def returnProblem(self, s: int, number_of_entries: int):
        """

        :param s: value for the seed
        :return: None
        """
        # seed random number generator
        seed(s)
        # generate some random numbers
        # print(random(), random(), random())

        for i in range(number_of_entries):
            max = self.board.length * self.board.length
            x = randrange(0, max)
            y = randrange(0, max)
            while self.board.getCoordinate(x, y) is not None:
                x = randrange(0, max)
                y = randrange(0, max)

            self.board.setCoordinate(x, y, randrange(1, max+1))

    def returnProblemSolution(self):
        """

        :return:
        """