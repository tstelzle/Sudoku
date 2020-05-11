from Board.Board import Board
from ProblemGenerator.RandomProblem import RandomProblem

def main():
    sudoku = Board()
    randProb = RandomProblem(sudoku)
    randProb.returnProblem(10, 81)

    print('Length of the Board: ' + str(sudoku.length))
    print('Length of the BoardRow: ' + str(sudoku.board[0].length))
    print('Length of the Field: ' + str(sudoku.board[0].boardRow[0].length))
    print('Length of the FieldRow: ' + str(sudoku.board[0].boardRow[0].field[0].length))

    print("")
    print('The given Sudoku board:')
    sudoku.printBoard()

if __name__ == "__main__":
    main()