from Board import Board

def main():
    sudoku = Board()
    print('Length of the Board: ' + str(sudoku.length))
    print('Length of the BoardRow: '  + str(sudoku.board[0].length))
    print('Length of the Field: ' + str(sudoku.board[0].boardRow[0].length))
    print('Length of the FieldRow: ' +  str(sudoku.board[0].boardRow[0].field[0].length))

if __name__ == "__main__":
    main()