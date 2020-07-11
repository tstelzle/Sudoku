from ProblemGenerator.ProblemBaseClass import ProblemFinder
import Board.Board
import math


class BruteForceBacktracking(ProblemFinder):

    def __init__(self, board: Board):
        super().__init__(board)
        self.board = board
        self.setValues = {}
        self.initializeSetValues()

    def initializeSetValues(self):
        for x in range(0, self.board.getBoardLength()):
            for y in range(0, self.board.getBoardLength()):
                self.setValues[self.getIdentifier(x, y)] = list(range(1, self.board.getBoardLength() + 1))

    def getIdentifier(self, x: int, y: int):
        return str(x) + str(y)

    # ToDo Backtracking two step should reset the setValue of the list
    def returnProblemSolution(self):
        y = 0
        x = 0
        print(self.board.getBoardLength())
        while y < self.board.getBoardLength():
            print(y)
            while x < self.board.getBoardLength():
                if (y == self.board.getBoardLength()):
                    break
                print(x)
                tried = []
                try:
                    array = self.setValues[self.getIdentifier(x, y)]
                except:
                    print('hier')
                for val in array:
                    row = self.checkRow(y, val)
                    column = self.checkColumn(x, val)
                    box = self.checkBox(x, y, val)
                    if (row and column and box):
                        self.board.setValue(x, y, val)
                        self.setValues[self.getIdentifier(x, y)].remove(val)
                        if x == self.board.getBoardLength() - 1:
                            x = 0
                            y += 1
                        else:
                            x += 1
                        break
                    # ToDo not working if statemnet -> never insert
                    tried.append(val)
                    if len(tried) >= len(self.setValues[self.getIdentifier(x, y)]):
                        print('jo')
                        if x == self.board.getBoardLength()-1:
                            if (self.board.getValue(0, y + 1) == -1):
                                self.setValues[self.getIdentifier(x + 1, y)] = list(
                                    range(1, self.board.getBoardLength() + 1))
                        else:
                            if (self.board.getValue(x + 1, y) == -1):
                                self.setValues[self.getIdentifier(x + 1, y)] = list(
                                    range(1, self.board.getBoardLength() + 1))
                        # oldVal = self.board.getValue(x, y)
                        # self.setValues[self.getIdentifier(x, y)].append(oldVal)
                        self.board.setValue(x, y, -1)
                        if x == 0:
                            y = y - 1
                            x = self.board.getBoardLength() - 1
                        else:
                            x = x - 1
                        break

    def returnProblem(self):
        print("ToDo")

    def getMultiplier(self, val: int):
        if val == 0:
            return 0
        return math.floor(val / self.board.length)

    def getBoxEdgeMin(self, val: int):
        return self.getMultiplier(val) * self.board.length

    def getBoxEdgeMax(self, val: int):
        return ((self.getMultiplier(val) + 1) * self.board.length)

    def checkBox(self, x: int, y: int, val: int):
        minX = self.getBoxEdgeMin(x)
        maxX = self.getBoxEdgeMax(x)
        minY = self.getBoxEdgeMin(y)
        maxY = self.getBoxEdgeMax(y)
        for x_1 in range(minX, maxX):
            for y_1 in range(minY, maxY):
                value = self.board.getValue(x_1, y_1)
                if value == val:
                    return False
        return True

    def checkColumn(self, x: int, val: int):
        for y in range(0, self.board.getBoardLength()):
            value = self.board.getValue(x, y)
            if value == val:
                return False
        return True

    def checkRow(self, y: int, val: int):
        for x in range(0, self.board.getBoardLength()):
            value = self.board.getValue(x, y)
            if value == val:
                return False
        return True
