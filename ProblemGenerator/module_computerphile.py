import random

import Board.module_board
from ProblemGenerator.module_problem_base_class import ProblemFinder


class Computerphile(ProblemFinder):
    """
    This Algorithm is inspired by the youtube video from the Computerphile channel.
    https://www.youtube.com/watch?v=G_UYXzGuqvM
    """

    def __init__(self, board: Board, seed: int, log_name: str):
        super().__init__(board, seed, log_name)
        self.board = board

    def return_problem_solution(self):
        for y in range(self.board.get_board_length()):
            for x in range(self.board.get_board_length()):
                if self.board.get_value(x, y) == -1 or self.board.get_value(x, y) is None:
                    random_value_list = list(range(1, self.board.get_board_length() + 1))
                    while len(random_value_list) != 0:
                        n = random.choice(random_value_list)
                        random_value_list.remove(n)
                        if self.possible(y, x, n):
                            self.board.set_value(x, y, n)
                            if self.return_problem_solution():
                                self.board.set_value(x, y, -1)
                            else:
                                return False
                    return True
        return False

    def possible(self, y: int, x: int, n: int):
        """
        This methods checks if value n is possible at position x,y.
        :param y: y position of the board
        :param x: x position of the board
        :param n: value we want to place at the position
        :return: True or False
        """
        if self.check_column(x, n) == self.check_row(y, n) == self.check_box(x, y, n) is True:
            return True
        return False
