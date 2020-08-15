import os

import bs4
import pdfkit

from Board.Board import Board


class PdfPrinter():

    def __init__(self, board: Board):
        self.board = board

    def printHtml(self, title: str, outputName: str):
        """
        Gnerates a html template for the given board with the given title.

        :param title: Title of the pdf
        :param outputName: filename of the pdf
        :return: filename of the gnerated tempalte
        """
        with open('output/template.html') as template:
            html = template.read()
            soup = bs4.BeautifulSoup(html, 'html.parser')

        headline = soup.new_tag('h1', style="text-align:center")
        headline.append(title)
        soup.body.append(headline)

        new_table = soup.new_tag('table', style="margin-left: auto; margin-right: auto")

        rowCounter = 1
        lastRow = 1
        for boardRow in self.board.board:
            for field in boardRow.boardRow:
                if rowCounter % self.board.length == 0 and lastRow * self.board.length != self.board.getBoardLength():
                    rowCounter = 1
                    lastRow += 1
                    column = soup.new_tag('tr', style="border-bottom: 5px solid black")
                else:
                    rowCounter += 1
                    column = soup.new_tag('tr')
                for i in range(0, self.board.length):
                    columnCounter = 1
                    for val in field.field[i].fieldRow:
                        if columnCounter % self.board.length == 0 and (
                                i + 1) * self.board.length != self.board.getBoardLength():
                            columnCounter = 1
                            elem = soup.new_tag('td', style="border-right: 5px solid black")
                        else:
                            columnCounter += 1
                            elem = soup.new_tag('td')
                        elemDiv = soup.new_tag('div',
                                               style="text-align: center; line-height: 30px; height: 30px; width: 20px")
                        if val != -1:
                            elemDiv.insert(1, str(val))
                        elem.append(elemDiv)
                        column.append(elem)
                    new_table.append(column)

        soup.body.append(new_table)

        if not os.path.exists('generated'):
            os.makedirs('generated')
        fileName = 'generated/.' + outputName + ".html"

        with open(fileName, 'w') as output:
            output.write(soup.prettify())

        return fileName

    def printSudoku(self, title: str, outputName: str):
        """
        Builds the pdf with from the given template.

        :param title: title of the pdf
        :param outputName: filename of the pdf
        """
        fileName = self.printHtml(title, outputName)
        output = 'generated/' + outputName + '.pdf'
        options = {
            'orientation': 'Landscape',
            'title': title,
            'page-size': 'A4'
        }
        pdfkit.from_file(fileName, output, css='output/gutenberg.css', options=options)
        os.remove(fileName)
