from Board.mdoule_field import Field


class BoardRow:
    """
    One row in the complete Sudoku Board.
    Each BoardRow contains, as many Fields as given length.
    """

    def __init__(self, length=3):
        """
        The constructor of the @class BoardRow.
        :param length: the length of the BoardRow list.
        """
        self.boardRow = [Field(length) for i in range(length)]
        self.length = length

    def print_board_row(self):
        """
        Prints all the lines in the Sudoku from the given boardRow
        :return: None
        """
        for i in range(self.length):
            line = "|"
            for field in self.boardRow:
                line += field.print_field_row(i)
            print(line)

    def board_row_to_string(self):
        board_row_string = ""
        for i in range(self.length):
            line = "|"
            for field in self.boardRow:
                line += field.print_field_row(i)
            board_row_string += line + '\n'
        return board_row_string
