import pymupdf4llm


def extract_document(pdf_file):

    markdown_text = pymupdf4llm.to_markdown(
        pdf_file
    )

    return markdown_text