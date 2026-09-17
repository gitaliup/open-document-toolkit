# Open Document Toolkit

A lightweight, open-source Python toolkit for working with PDF documents.

Open Document Toolkit provides a simple Python API and command-line interface for common PDF operations, with a focus on reliability, automation, and developer-friendly usage.

## Features

- Merge multiple PDF files into one PDF
- Split PDF files into individual pages
- Rotate PDF pages
- Delete specific pages from a PDF
- Python API
- Command-line interface
- Automated tests
- GitHub Actions continuous integration
- MIT licensed

## Installation

Install the latest release from PyPI:

    pip install open-document-toolkit

## Quick Start

### Python API

#### Merge PDFs

    from odt import merge_pdfs

    merge_pdfs(
        ["first.pdf", "second.pdf"],
        "merged.pdf"
    )

#### Split a PDF

    from odt import split_pdf

    split_pdf(
        "document.pdf",
        "output_pages"
    )

#### Rotate a PDF

    from odt import rotate_pdf

    rotate_pdf(
        "document.pdf",
        "rotated.pdf",
        degrees=90
    )

#### Delete Pages

    from odt import delete_pages

    delete_pages(
        "document.pdf",
        "without_pages.pdf",
        [2, 4]
    )

Pages are specified using 1-based page numbers.

## Command-Line Interface

After installation, the `odt` command is available.

### Merge PDFs

    odt merge first.pdf second.pdf -o merged.pdf

### Split PDF

    odt split document.pdf -o output_pages

### Rotate PDF

    odt rotate document.pdf -o rotated.pdf -d 90

### Delete Pages

    odt delete document.pdf 2 4 -o without_pages.pdf

The example above deletes pages 2 and 4.

Supported rotation angles:

- 90°
- 180°
- 270°

## Development

Clone the repository:

    git clone https://github.com/gitaliup/open-document-toolkit.git
    cd open-document-toolkit

Install the project with test dependencies:

    pip install -e ".[test]"

Run the test suite:

    pytest

## Project Structure

    open-document-toolkit/
    ├── src/
    │   └── odt/
    │       ├── __init__.py
    │       └── pdf.py
    ├── tests/
    │   ├── test_pdf.py
    │   └── test_cli.py
    ├── .github/
    │   └── workflows/
    │       ├── tests.yml
    │       └── publish.yml
    ├── CHANGELOG.md
    ├── LICENSE
    ├── README.md
    └── pyproject.toml

## Project Status

Open Document Toolkit is currently in early development.

The current release provides the foundation for common PDF processing operations. More document-processing capabilities will be added over time based on real-world use cases and community feedback.

## Contributing

Contributions are welcome.

You can contribute by:

- Reporting bugs
- Suggesting features
- Improving documentation
- Adding tests
- Improving the implementation

For bugs and feature requests, please open an issue in the GitHub repository.

## License

This project is licensed under the MIT License.

## Links

- PyPI: https://pypi.org/project/open-document-toolkit/
- GitHub: https://github.com/gitaliup/open-document-toolkit/
