from pathlib import Path
from pypdf import PdfReader, PdfWriter


def merge_pdfs(input_files, output_file):
    """Merge multiple PDF files into one PDF."""
    writer = PdfWriter()

    for file in input_files:
        reader = PdfReader(file)

        for page in reader.pages:
            writer.add_page(page)

    with open(output_file, "wb") as output:
        writer.write(output)


def split_pdf(input_file, output_directory):
    """Split a PDF into individual pages."""
    reader = PdfReader(input_file)

    output_directory = Path(output_directory)
    output_directory.mkdir(parents=True, exist_ok=True)

    for number, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)

        output_file = output_directory / f"page_{number}.pdf"

        with open(output_file, "wb") as output:
            writer.write(output)


def rotate_pdf(input_file, output_file, degrees=90):
    """Rotate every page in a PDF."""
    reader = PdfReader(input_file)
    writer = PdfWriter()

    for page in reader.pages:
        page.rotate(degrees)
        writer.add_page(page)

    with open(output_file, "wb") as output:
        writer.write(output)


def main():
    print("Open Document Toolkit v0.1.0")
