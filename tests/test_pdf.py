from pypdf import PdfReader, PdfWriter

from odt import merge_pdfs, split_pdf, rotate_pdf, delete_pages


def create_pdf(path, number_of_pages=1):
    """Create a simple test PDF."""
    writer = PdfWriter()

    for _ in range(number_of_pages):
        writer.add_blank_page(width=612, height=792)

    with open(path, "wb") as output:
        writer.write(output)


def test_merge_pdfs(tmp_path):
    """Test merging multiple PDF files."""
    first_pdf = tmp_path / "first.pdf"
    second_pdf = tmp_path / "second.pdf"
    merged_pdf = tmp_path / "merged.pdf"

    create_pdf(first_pdf, 1)
    create_pdf(second_pdf, 2)

    merge_pdfs(
        [first_pdf, second_pdf],
        merged_pdf,
    )

    reader = PdfReader(merged_pdf)

    assert len(reader.pages) == 3


def test_split_pdf(tmp_path):
    """Test splitting a PDF into individual pages."""
    input_pdf = tmp_path / "document.pdf"
    output_directory = tmp_path / "pages"

    create_pdf(input_pdf, 3)

    split_pdf(
        input_pdf,
        output_directory,
    )

    output_files = list(output_directory.glob("*.pdf"))

    assert len(output_files) == 3


def test_rotate_pdf(tmp_path):
    """Test rotating a PDF."""
    input_pdf = tmp_path / "document.pdf"
    output_pdf = tmp_path / "rotated.pdf"

    create_pdf(input_pdf, 1)

    rotate_pdf(
        input_pdf,
        output_pdf,
        degrees=90,
    )

    reader = PdfReader(output_pdf)

    assert len(reader.pages) == 1
    assert reader.pages[0].rotation == 90


def test_delete_pages(tmp_path):
    """Test deleting specific pages from a PDF."""
    input_pdf = tmp_path / "document.pdf"
    output_pdf = tmp_path / "without_pages.pdf"

    create_pdf(input_pdf, 5)

    delete_pages(
        input_pdf,
        output_pdf,
        [2, 4],
    )

    reader = PdfReader(output_pdf)

    assert len(reader.pages) == 3
