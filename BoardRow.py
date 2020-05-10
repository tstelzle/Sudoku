from Field import Field

class BoardRow:
    """
    One row in the complete Sudoku Board.
    Each BoardRow contains, as many Fields as given length.
    """

    def __init__(self, length=3):
        """
        The constructor of the @class BoardRow.
        :param length: the lenght of the BoardRow list.
        """
        self.boardRow = [Field(length) for i in range(length)]
        self.length = length

    def printBoardRow(self):
        """
        Prints all the lines in the Sudoku from the given boardRow
        :return: None
        """
        for i in range(self.length):
            line = "|"
            for field in self.boardRow:
                line += field.printFieldRow(i)
            print(line)