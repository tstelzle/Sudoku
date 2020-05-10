class FieldRow:
    """
    The class FieldRow.
    Each FieldRow contains three values for the Sudoku.
    Field is one row of the @class Board.
    """

    def __init__(self, length=3):
        """
        The constructor of the @class Field.
        """
        self.fieldRow = [length]
        self.length = length