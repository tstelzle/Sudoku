import os

import bs4
import pdfkit

from Board.module_board import Board


def initialize_printer():
    create_printer_dir()


def create_printer_dir():
    if not os.path.exists('generated'):
        os.makedirs('generated')
        os.chmod('generated', 0o777)


class PdfPrinter:

    def __init__(self, board: Board):
        self.board = board

    def print_html(self, title: str, output_name: str):
        """
        Generates a html template for the given board with the given title.

        :param title: Title of the pdf
        :param output_name: filename of the pdf
        :return: filename of the generated template
        """
        with open('output/template.html') as template:
            html = template.read()
            soup = bs4.BeautifulSoup(html, 'html.parser')

        headline = soup.new_tag('h1', style="text-align:center")
        headline.append(title)
        soup.body.append(headline)

        new_table = soup.new_tag('table', style="margin-left: auto; margin-right: auto")

        row_counter = 1
        last_row = 1
        for boardRow in self.board.board:
            for field in boardRow.boardRow:
                if row_counter % self.board.length == 0 \
                        and last_row * self.board.length != self.board.get_board_length():
                    row_counter = 1
                    last_row += 1
                    column = soup.new_tag('tr', style="border-bottom: 5px solid black")
                else:
                    row_counter += 1
                    column = soup.new_tag('tr')
                for i in range(0, self.board.length):
                    column_counter = 1
                    for val in field.field[i].fieldRow:
                        if column_counter % self.board.length == 0 and (
                                i + 1) * self.board.length != self.board.get_board_length():
                            column_counter = 1
                            elem = soup.new_tag('td', style="border-right: 5px solid black")
                        else:
                            column_counter += 1
                            elem = soup.new_tag('td')
                        elem_div = soup.new_tag('div',
                                                style="text-align: center; line-height: "
                                                      "30px; "
                                                      "height: 30px; width: 20px")
                        if val != -1:
                            elem_div.insert(1, str(val))
                        elem.append(elem_div)
                        column.append(elem)
                    new_table.append(column)

        soup.body.append(new_table)

        file_name = 'generated/.' + output_name + ".html"

        with open(file_name, 'w') as output:
            output.write(soup.prettify())

        return file_name

    def print_sudoku(self, title: str, output_name: str):
        """
        Builds the pdf with from the given template.

        :param title: title of the pdf
        :param output_name: filename of the pdf
        """
        file_name = self.print_html(title, output_name)
        output = 'generated/' + output_name + '.pdf'
        options = {
            'orientation': 'Landscape',
            'title': title,
            'page-size': 'A4'
        }
        pdfkit.from_file(file_name, output, css='output/gutenberg.css', options=options)
        os.chmod(output, 0o777)
        os.remove(file_name)
