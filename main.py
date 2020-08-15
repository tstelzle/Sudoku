import sys
import time

import ProblemGenerator.difficulties as difficulties
from Board.Board import Board
from ProblemGenerator import BruteForceBacktracking
from ProblemGenerator import ProblemBaseClass
from output import PdfService


def runSolution(sudoku: Board, algorithmClass: ProblemBaseClass):
    """
    Runs the given algorithm and returns the sudoku solution.
    :param sudoku: the sudoku board
    :param algorithmClass: the class of the algorithm to use
    :return: the sudoku board
    """
    algorithmus = algorithmClass(sudoku)
    pdfPrinter = PdfService.PdfPrinter(sudoku)
    print('The Sudoku Solution:')
    starttime = time.time()
    algorithmus.returnProblemSolution()
    endtime = time.time()
    print('Duration: ' + str(endtime - starttime) + "s")
    sudoku.printBoard()
    title = 'Sudoku-Solution'
    pdfPrinter.printSudoku(title, getFileName(sudoku, title))
    return sudoku


def getFileName(sudoku: Board, title: str):
    """
    Returns the filename of the pdf to make, with a timestamp
    :param sudoku: the sudoku board
    :param title: the title of the pdf
    :return: filename
    """
    timestamp = str(int(time.time()))
    boardsize = str(sudoku.length)
    return title + "_" + timestamp + "_" + boardsize


def runProblem(sudoku: Board, algorithmClass: ProblemBaseClass, difficulty: difficulties):
    """
    Runs the given algorithm and returns the sudoku problem.
    :param sudoku: the sudoku board
    :param algorithmClass: the class of the algorithm to use
    :param difficulty: the difficulty of the problem specified by the enum
    :return: the sudoku board
    """
    algorithmus = algorithmClass(sudoku)
    pdfPrinter = PdfService.PdfPrinter(sudoku)
    print('The Sudoku Problem:')
    algorithmus.returnProblem(difficulty)
    sudoku.printBoard()
    title = 'Sudoku-Problem'
    pdfPrinter.printSudoku(title, getFileName(sudoku, title))
    return sudoku


def runSolutionAndProblem(sudoku: Board, algorithmClass: ProblemBaseClass, difficulty=difficulties.HARD):
    """
    Runs the two methods 'runSolution' and 'runProblem' to calculate the sudoku solution and problem.
    :param sudoku: the sudoku board
    :param algorithmClass: the class of the algorithm to use
    :param difficulty: the difficulty of the problem specified by the enum
    :return:
    """
    sudoku_sol = runSolution(sudoku, algorithmClass)
    sudoku_prob = runProblem(sudoku_sol, algorithmClass, difficulty)
    return [sudoku_sol, sudoku_prob]


def printBoardInformation(sudoku: Board):
    """
    Prints the information about the board size.
    :param sudoku: the sudoku board
    :return: None
    """
    print('Length of the Board: ' + str(sudoku.length))
    print('Length of the BoardRow: ' + str(sudoku.board[0].length))
    print('Length of the Field: ' + str(sudoku.board[0].boardRow[0].length))
    print('Length of the FieldRow: ' + str(sudoku.board[0].boardRow[0].field[0].length))
    print("")


def readBoardParameter():
    """
    Reads the input parameters. And returns the size of the board.
    :return: int
    """
    if len(sys.argv) >= 1:
        return int(sys.argv[1])
    return -1


def main():
    boardSize = readBoardParameter() if readBoardParameter() > 0 else 3
    sudoku = Board(boardSize)
    printBoardInformation(sudoku)
    results = runSolutionAndProblem(sudoku, BruteForceBacktracking.BruteForceBacktracking)


if __name__ == "__main__":
    main()
