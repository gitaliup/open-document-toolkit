import argparse
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


def build_parser():
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="odt",
        description="Open Document Toolkit - PDF utilities",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    merge_parser = subparsers.add_parser(
        "merge",
        help="Merge multiple PDF files into one PDF",
    )
    merge_parser.add_argument(
        "input_files",
        nargs="+",
        help="Input PDF files",
    )
    merge_parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output PDF file",
    )

    split_parser = subparsers.add_parser(
        "split",
        help="Split a PDF into individual pages",
    )
    split_parser.add_argument(
        "input_file",
        help="Input PDF file",
    )
    split_parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output directory",
    )

    rotate_parser = subparsers.add_parser(
        "rotate",
        help="Rotate every page in a PDF",
    )
    rotate_parser.add_argument(
        "input_file",
        help="Input PDF file",
    )
    rotate_parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output PDF file",
    )
    rotate_parser.add_argument(
        "-d",
        "--degrees",
        type=int,
        default=90,
        choices=[90, 180, 270],
        help="Rotation angle",
    )

    return parser


def main():
    """Run the command-line interface."""
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "merge":
        merge_pdfs(
            args.input_files,
            args.output,
        )

    elif args.command == "split":
        split_pdf(
            args.input_file,
            args.output,
        )

    elif args.command == "rotate":
        rotate_pdf(
            args.input_file,
            args.output,
            args.degrees,
        )


if __name__ == "__main__":
    main()
