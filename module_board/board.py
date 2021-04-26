import math

import module_logger as log
from .board_row import BoardRow


class Board:
    """
    The class for the whole Sudoku Board.
    The length defines how many items are in one column.
    """

    def __init__(self, length=3):
        """
        The constructor of the @class completeBoard
        :param length:
        """
        self.board = [BoardRow(length) for i in range(length)]
        self.length = length

    def print_board(self):
        """
        Calls the print_board_row for every boardRow in the Sudoku.
        Prints the board.
        :return: None
        """
        dashes_numbers = 3 * self.get_board_length()
        dashes_posts = 2 * self.length
        print('-' * (dashes_numbers + dashes_posts + 1))
        for i in range(len(self.board)):
            self.board[i].print_board_row()
            print('-' * (dashes_numbers + dashes_posts + 1))

    def log_board(self, file_name: str):
        log.append_to_log(file_name, self.board_to_string())

    def board_to_string(self):
        board_string = ""
        dashes_numbers = 3 * self.get_board_length()
        dashes_posts = 2 * self.length
        board_string += '-' * (dashes_numbers + dashes_posts + 1) + '\n'
        for i in range(len(self.board)):
            board_string += self.board[i].board_row_to_string()
            board_string += '-' * (dashes_numbers + dashes_posts + 1) + '\n'
        return board_string

    def get_board_length(self):
        """
        Returns the length of one site of the board.
        :return: int
        """
        return self.length ** 2

    def get_max_number_of_entries(self):
        """
        Returns the amount of entries, which can be put on the board
        :return: int
        """
        return self.length ** 4

    def set_value_2(self, x_board, y_board, x_field, y_field, value):
        self.board[y_board].boardRow[x_board].field[y_field].fieldRow[x_field] = value

    def get_value_2(self, x_board, y_board, x_field, y_field):
        return self.board[y_board].boardRow[x_board].field[y_field].fieldRow[x_field]

    def set_value(self, x: int, y: int, value: int):
        """
        :param x: The x Coordinate of the Board
        :param y: The y Coordinate of the Board
        :param value: the value which will be inserted
        :return: None
        """

        self.board[math.floor(y / self.length)].boardRow[math.floor(x / self.length)].field[y % self.length].fieldRow[
            x % self.length] = value

    def get_value(self, x: int, y: int):
        """
        :param x: The x Coordinate of the Board
        :param y: The y Coordinate of the Board
        :return: The value of the specified coordinate
        """
        return self.board[math.floor(y / self.length)].boardRow[math.floor(x / self.length)].field[
            y % self.length].fieldRow[x % self.length]

    def is_empty(self, x: int, y: int):
        """
        :param x: The x Coordinate of the Board
        :param y: The y Coordinate of the Board
        :return: bool
        """
        return self.get_value(x, y) is None or self.get_value(x, y) == -1
