from pdf2docx import Converter
import tkinter.filedialog
from docx2pdf import convert

def description():
    input_file=tkinter.filedialog.askopenfilename()
    output_file=tkinter.filedialog.asksaveasfilename()
    return input_file,output_file


def pdftodox():
    pdf_file,docx_file=description()
    docx_file=docx_file+'.docx'
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()

pdftodox()