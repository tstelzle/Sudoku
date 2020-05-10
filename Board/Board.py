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
        for boardRow in self.board:
            boardRow.printBoardRow()
            print("")

    def setValue2(self, xBoard, yBoard, xField, yField, value):
         self.board[yBoard].boardRow[xBoard].field[yField].fieldRow[xField] = value

    def getValue2(self, xBoard, yBoard, xField, yField):
        return self.board[yBoard].boardRow[xBoard].field[yField].fieldRow[xField]