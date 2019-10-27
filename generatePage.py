import sys
import argparse

from docx import Document
from docx.shared import Inches

pars = argparse.ArgumentParser()
pars.add_argument("--start_year", help="year of birth", required=True)
pars.add_argument("--years_per_page",  required=False, help="e.g. 2 years a page")

document = Document()

document.add_picture('youarenew.png', width=Inches(1.25))
document.add_heading('Notes for Time Here', 0)

def printYear(year):
    document.add_heading(str(year), level=1)

    p = document.add_paragraph('A plain paragraph having some ')
    p.add_run('bold').bold = True
    p.add_run(' and some ')
    p.add_run('italic.').italic = True


args = pars.parse_args()
start = args.start_year
for year in range(2020,int(start)-1, -1):
    printYear(year)

document.save('demo.docx')