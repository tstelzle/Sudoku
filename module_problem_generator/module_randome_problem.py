# seed the pseudorandom number generator
from random import seed

from Board.module_board import Board
from module_problem_generator.module_problem_base_class import ProblemFinder


class RandomProblem(ProblemFinder):
    super

    def __init__(self, board: Board):
        self.board = board

    def return_problem(self, s: int):
        """

        :param s: value for the seed
        :return:
        """
        # seed random number generator
        seed(s)
        # generate some random numbers
        # print(random(), random(), random())
        # self.board.setValue(0, 0, 1)
        # self.board.setValue(1, 0, 1)
        # self.board.setValue(4, 0, 1)
        # self.board.setValue(4, 4, 1)

    def return_problem_solution(self):
        """

        :return:
        """
