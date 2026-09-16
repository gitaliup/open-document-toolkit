import sys

from pypdf import PdfReader, PdfWriter

from odt.pdf import main


def create_pdf(path, number_of_pages=1):
    """Create a simple test PDF."""
    writer = PdfWriter()

    for _ in range(number_of_pages):
        writer.add_blank_page(width=612, height=792)

    with open(path, "wb") as output:
        writer.write(output)


def test_cli_merge(tmp_path, monkeypatch):
    """Test the merge CLI command."""
    first_pdf = tmp_path / "first.pdf"
    second_pdf = tmp_path / "second.pdf"
    output_pdf = tmp_path / "merged.pdf"

    create_pdf(first_pdf, 1)
    create_pdf(second_pdf, 2)

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "odt",
            "merge",
            str(first_pdf),
            str(second_pdf),
            "-o",
            str(output_pdf),
        ],
    )

    main()

    reader = PdfReader(output_pdf)

    assert len(reader.pages) == 3


def test_cli_split(tmp_path, monkeypatch):
    """Test the split CLI command."""
    input_pdf = tmp_path / "document.pdf"
    output_directory = tmp_path / "pages"

    create_pdf(input_pdf, 3)

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "odt",
            "split",
            str(input_pdf),
            "-o",
            str(output_directory),
        ],
    )

    main()

    output_files = list(output_directory.glob("*.pdf"))

    assert len(output_files) == 3


def test_cli_rotate(tmp_path, monkeypatch):
    """Test the rotate CLI command."""
    input_pdf = tmp_path / "document.pdf"
    output_pdf = tmp_path / "rotated.pdf"

    create_pdf(input_pdf, 1)

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "odt",
            "rotate",
            str(input_pdf),
            "-o",
            str(output_pdf),
            "-d",
            "90",
        ],
    )

    main()

    reader = PdfReader(output_pdf)

    assert len(reader.pages) == 1
    assert reader.pages[0].rotation == 90
