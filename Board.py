from BoardRow import BoardRow

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
        self.board = [BoardRow() for i in range(length)]
        self.length = length