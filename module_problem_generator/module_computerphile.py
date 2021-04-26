import random

from module_board import Board
from .module_problem_base_class import ProblemFinder


class Computerphile(ProblemFinder):
    """
    This Algorithm is inspired by the youtube video from the Computerphile channel.
    https://www.youtube.com/watch?v=G_UYXzGuqvM
    """

    def __init__(self, board: Board, seed: int, log_name: str):
        super().__init__(board, seed, log_name)
        self.board = board

    def return_problem_solution(self):
        self.solve()
        for y in range(self.board.get_board_length()):
            for x in range(self.board.get_board_length()):
                if self.board.get_value(x, y) == -1 or self.board.get_value(x, y) is None:
                    return False
        return True

    def solve(self):
        """
        Calculates a solution for the sudoku board.
        It iteratores over the free fields and chooses a valid value.
        With recursion it does this for the next free field.
        When there is no possible option for a field solve() returns False and resets the previous entry.
        Otherwise it returns True and goes on with the next free field.
        :return: Bool algorithm finished / value was good or not
        """
        for y in range(self.board.get_board_length()):
            for x in range(self.board.get_board_length()):
                if self.board.get_value(x, y) == -1 or self.board.get_value(x, y) is None:
                    random_value_list = list(range(1, self.board.get_board_length() + 1))
                    while len(random_value_list) != 0:
                        n = random.choice(random_value_list)
                        random_value_list.remove(n)
                        if self.possible(y, x, n):
                            self.board.set_value(x, y, n)
                            if not self.solve():
                                self.board.set_value(x, y, -1)
                            else:
                                return True
                    return False
        return True

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
