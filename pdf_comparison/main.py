# pylint: disable=all
"""Explanation of the Code:
extract_text_from_pdf function:

This function uses PyPDF2 to read a PDF file and extract the text from all pages.
The extracted text is stored in a string.
compare_texts function:

The difflib.unified_diff() function compares the text line by line and generates a unified diff output, which shows the differences between the two texts.
The result is printed out in a format similar to what you’d see in a version control diff.
Installation of Required Libraries:
You need to install PyPDF2 and difflib (the latter is part of Python’s standard library, so no need to install it separately).

pip install PyPDF2
"""


import difflib
import PyPDF2

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()  # Extract text from each page
    return text

# Function to compare two texts and print differences
def compare_texts(text1, text2):
    # Use difflib to find differences between two texts
    diff = difflib.unified_diff(text1.splitlines(), text2.splitlines(), lineterm='', fromfile='File 1', tofile='File 2')

    # Print the differences
    print('\n'.join(diff))

# Paths to the two PDF files
pdf_file1 = 'file1.pdf'
pdf_file2 = 'file2.pdf'

# Extract text from both PDFs
text1 = extract_text_from_pdf(pdf_file1)
text2 = extract_text_from_pdf(pdf_file2)

# Compare the texts
compare_texts(text1, text2)
