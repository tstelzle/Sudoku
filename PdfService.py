import fpdf

from Board.Board import Board


class PdfPrinter:

    def __init__(self, board: Board):
        self.board = board
        self.pdf = fpdf.FPDF(format='legal')
        self.pdf.add_page('Landscape')
        self.pdf.set_line_width(2)
        self.pdf.set_font('Arial', size=25)

    def printToPdf(self, value: str):
        self.pdf.write(8.7, value)

    def addPage(self):
        self.pdf.add_page('Landscape')

    def getPdf(self):
        return self.pdf

    def generatePdf(self, pdfName: str):
        self.pdf.output(pdfName + '.pdf')

    def printPdf(self, pdfName: str):
        pdf = fpdf.FPDF(format='letter')
        pdf.add_page()
        pdf.set_font('Arial', size=12)
        pdf.write(5, self.board.boardToString())
        pdf.output(pdfName + ".pdf")
