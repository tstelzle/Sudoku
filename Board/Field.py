from Board.FieldRow import FieldRow


class Field:
    """
    The class for structuring one piece of the complete Sudoku board.
    Each Field, as many FieldColumns as the given length.
    """

    def __init__(self, length=3):
        """
        The constructor of the @class Board.

        :param length: The length of the board. Default=3
        """
        self.field = [FieldRow(length) for i in range(length)]
        self.length = length

    def getValue(self, pos):
        """
        Returns None or the value which is written in field.

        :param pos: The position in the board counted from top left to bottom right.
        :return: The value in the field or None
        """
        fieldListPos = pos % self.length
        fieldRowListPos = pos - self.length * fieldListPos
        if (self.field[fieldListPos][fieldRowListPos]):
            return self.field[fieldListPos][fieldRowListPos]
        else:
            return None

    def printFieldRow(self, posFieldRow):
        """
        Prints the row in the field given by posFieldRow
        :param posFieldRow:
        :return: String with the values in the fieldRow
        """
        fieldRow = self.field[posFieldRow].fieldRow
        output = " "
        for val in fieldRow:
            if val == None or val == -1:
                output = output + '_ '
            else:
                output = output + str(val) + ' '
        output += "|"
        return output
