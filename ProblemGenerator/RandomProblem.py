from ProblemGenerator.ProblemBaseClass import ProblemFinder

# seed the pseudorandom number generator
from random import seed
from random import randrange
from Board.Board import Board
import math

class RandomProblem(ProblemFinder):
    super

    def __init__(self, board: Board):
        self.board = board

    def returnProblem(self, s: int, number_of_entries: int):
        """
        Creates a random Sudoko Problem, which may not be solvable. Prints the number of inserted values.
        :param s: value for the seed
        :param number_of_entries: number of random values to insert in the board
        :return: None
        """
        # seed random number generator
        seed(s)
        number_of_inserted = 0

        for i in range(number_of_entries):
            max = self.board.length * self.board.length
            x = randrange(0, max)
            y = randrange(0, max)

            while self.board.getCoordinate(x, y) is not None:
                x = randrange(0, max)
                y = randrange(0, max)

            possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            for j in range(max):
                temp = self.board.getCoordinate(j, y)

                if temp in possible_numbers:
                    possible_numbers.remove(temp)

                temp = self.board.getCoordinate(x, j)

                if temp in possible_numbers:
                    possible_numbers.remove(temp)

            field = self.board.board[math.floor(y / self.board.length)].boardRow[
                math.floor(x / self.board.length)].field

            for row in range(self.board.length):
                for col in range(self.board.length):
                    temp = field[row].fieldRow[col]
                    if temp in possible_numbers:
                        possible_numbers.remove(temp)

            if len(possible_numbers) > 0:
                self.board.setCoordinate(x, y, possible_numbers[randrange(0, len(possible_numbers))])
                number_of_inserted += 1

        print(str(number_of_inserted) + " values in Sudoku inserted.")

    def returnProblemSolution(self):
        """

        :return:
        """