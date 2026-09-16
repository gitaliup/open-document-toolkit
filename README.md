# Open Document Toolkit

An open-source Python toolkit for creating, editing, converting, and managing PDF documents.

## Features

Currently supported:

- Merge multiple PDF files into one PDF
- Split a PDF into individual pages
- Rotate all pages in a PDF
- Simple Python API
- Command-line entry point

More document-processing features will be added over time.

## Installation

Clone the repository:

```bash
git clone https://github.com/gitaliup/open-document-toolkit.git
cd open-document-toolkit
```

Install the project:

```bash
pip install .
```

## Usage

### Merge PDFs

```python
from odt import merge_pdfs

merge_pdfs(
    ["first.pdf", "second.pdf"],
    "merged.pdf"
)
```

### Split a PDF

```python
from odt import split_pdf

split_pdf(
    "document.pdf",
    "output_pages"
)
```

### Rotate a PDF

```python
from odt import rotate_pdf

rotate_pdf(
    "document.pdf",
    "rotated.pdf",
    degrees=90
)
```

## Project Status

This project is currently under active development.

The goal is to provide a simple, reliable, and developer-friendly toolkit for common PDF and document-processing tasks.

## Contributing

Contributions, bug reports, feature requests, and pull requests are welcome.

Please open an issue before making major changes.

## License

This project is licensed under the MIT License.
