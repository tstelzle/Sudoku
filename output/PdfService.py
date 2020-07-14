import pdfkit
import bs4
from Board.Board import Board


class PdfPrinter():

    def __init__(self, board: Board):
        self.board = board

    # def printToPdf(self, value: str):
    #     self.pdf.write(8.7, value)
    #
    # def addPage(self):
    #     self.pdf.add_page('Landscape')
    #
    # def getPdf(self):
    #     return self.pdf
    #
    # def generatePdf(self, pdfName: str):
    #     self.pdf.output(pdfName + '.pdf')
    #
    # def printPdf(self, pdfName: str):
    #     pdf = fpdf.FPDF(format='letter')
    #     pdf.add_page()
    #     pdf.set_font('Arial', size=12)
    #     pdf.write(5, self.board.boardToString())
    #     pdf.output(pdfName + ".pdf")

    def printHtml(self):
        with open('template.html') as template:
            html = template.read()
            soup = bs4.BeautifulSoup(html)

        new_table = soup.new_tag('table')
        soup.body.append(new_table)

        with open('template.html', 'w') as output:
            output.write(str(soup))


        html = "<html><head><h1 style=\"text-align:center\">" + "Sudoku" + "</h1></head><body><table style=\"width:100%; text-align:center; border:1px solid black\">"
        for boardRow in self.board.board:
            for field in boardRow.boardRow:
                html += "<tr>"
                for i in range(0,self.board.length):
                        for val in field.field[i].fieldRow:
                            html += "<td>" + str(val) + "</td>"
                html += "</tr>"
        html += "</table></body></html>"
        Html_file = open("test.html", "w")
        Html_file.write(html)
        Html_file.close()
        return html

    def printSudoku(self):
        html = self.printHtml()
        print(html)
        pdfkit.from_file('test.html', 'test.pdf', css='gutenberg.css')