import math

from Board.BoardRow import BoardRow


class Board:
    """
    The class for the whole Sudoko Board.
    The length defines how many items are in one columen.
    """

    def __init__(self, length=3):
        """
        The connstructor of the @class completeBoard
        :param length:
        """
        self.board = [BoardRow(length) for i in range(length)]
        self.length = length

    def printBoard(self):
        """
        Calls the printBaordRow for every boardRow in the Sudoku.
        Prints the board.
        :return: None
        """
        dashesNumbers = 3 * self.getBoardLength()
        dashesPosts = 2 * self.length
        print('-' * (dashesNumbers + dashesPosts + 1))
        for i in range(len(self.board)):
            self.board[i].printBoardRow()
            print('-' * (dashesNumbers + dashesPosts + 1))

    def boardToString(self):
        boardString = ""
        dashesNumbers = 3 * self.getBoardLength()
        dashesPosts = 2 * self.length
        boardString += '-' * (dashesNumbers + dashesPosts + 1) + '\n'
        for i in range(len(self.board)):
            boardString += self.board[i].boardRowToString()
            boardString += '-' * (dashesNumbers + dashesPosts + 1) + '\n'
        return boardString

    def getBoardLength(self):
        """
        Returns the length of one site of the board.
        :return: int
        """
        return self.length ** 2

    def getMaxNumberOfEntries(self):
        """
        Returns the amount of entries, which can be put on the board
        :return: int
        """
        return self.length ** 4

    def setValue2(self, xBoard, yBoard, xField, yField, value):
        self.board[yBoard].boardRow[xBoard].field[yField].fieldRow[xField] = value

    def getValue2(self, xBoard, yBoard, xField, yField):
        return self.board[yBoard].boardRow[xBoard].field[yField].fieldRow[xField]

    def setValue(self, x: int, y: int, value: int):
        """

        :param x: The x Coordinate of the Board
        :param y: The y Coordinate of the Board
        :return: None
        """

        self.board[math.floor(y / self.length)].boardRow[math.floor(x / self.length)].field[y % self.length].fieldRow[
            x % self.length] = value

    def getValue(self, x: int, y: int):
        """

        :param x: The x Coordinate of the Board
        :param y: The y Coordinate of the Board
        :return: The value of the specified Coordinate
        """
        return self.board[math.floor(y / self.length)].boardRow[math.floor(x / self.length)].field[
            y % self.length].fieldRow[x % self.length]
