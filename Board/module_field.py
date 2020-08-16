from Board.module_field_row import FieldRow


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

    def get_value(self, pos):
        """
        Returns None or the value which is written in field.

        :param pos: The position in the board counted from top left to bottom right.
        :return: The value in the field or None
        """
        field_list_pos = pos % self.length
        field_row_list_pos = pos - self.length * field_list_pos
        if self.field[field_list_pos][field_row_list_pos]:
            return self.field[field_list_pos][field_row_list_pos]
        else:
            return None

    def print_field_row(self, pos_field_row):
        """
        Prints the row in the field given by pos_field_row
        :param pos_field_row:
        :return: String with the values in the field_row
        """
        field_row = self.field[pos_field_row].fieldRow
        output = " "
        for val in field_row:
            if val is None or val == -1:
                output = output + '__ '
            elif val < 10:
                output = output + ' ' + str(val) + ' '
            else:
                output = output + str(val) + ' '
        output += "|"
        return output
