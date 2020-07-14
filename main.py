from output import PdfService
import ProblemGenerator.difficulties as difficulties
from Board.Board import Board
from ProblemGenerator.BruteForceBacktracking import BruteForceBacktracking


def main():
    sudoku = Board(4)

    print('Length of the Board: ' + str(sudoku.length))
    print('Length of the BoardRow: ' + str(sudoku.board[0].length))
    print('Length of the Field: ' + str(sudoku.board[0].boardRow[0].length))
    print('Length of the FieldRow: ' + str(sudoku.board[0].boardRow[0].field[0].length))
    print("")

    algorithmus = BruteForceBacktracking(sudoku)
    pdfPrinter = PdfService.PdfPrinter(sudoku)

    print('The Sudoku Solution:')
    algorithmus.returnProblemSolution()
    sudoku.printBoard()

    pdfPrinter.printSudoku()
    #pdfPrinter.printToPdf(sudoku.boardToString())

    print('The Sudoku Problem:')
    algorithmus.returnProblem(difficulties.HARD)
    sudoku.printBoard()

    #pdfPrinter.addPage()
    #pdfPrinter.printToPdf(sudoku.boardToString())

    #pdfPrinter.generatePdf('bruteForce_Hard')


if __name__ == "__main__":
    main()
