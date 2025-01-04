#!/usr/bin/env python3
"""
khmer_pdf_parser.py

A Python script to parse Khmer text from PDF files. It handles both native (text-based)
and scanned (image-based) PDFs by extracting selectable text or performing OCR respectively.

Usage:
    python khmer_pdf_parser.py path/to/input.pdf

Dependencies:
    - pdfplumber
    - pdf2image
    - pytesseract
    - Pillow
    - tqdm

    Install via pip:
        pip install -r requirements.txt

    Additionally, ensure Tesseract OCR is installed on your system with the Khmer language pack.

Author:
    Your Name (https://github.com/your-github-username)
"""

import os
import sys
import argparse
import logging
import unicodedata
from typing import Optional

import pdfplumber
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
from tqdm import tqdm


def setup_logging():
    """
    Configures the logging for the script.
    Logs are written to both the console and a log file.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("khmer_pdf_parser.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )


def parse_khmer_text_native(pdf_path: str) -> str:
    """
    Extracts Khmer text from a native (text-based) PDF using pdfplumber.

    :param pdf_path: Path to the input PDF file.
    :return: Extracted Khmer text.
    :raises Exception: If text extraction fails.
    """
    extracted_text = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            logging.info(f"Opened PDF file: {pdf_path}")
            for page_number, page in enumerate(tqdm(pdf.pages, desc="Extracting text from PDF"), start=1):
                text = page.extract_text()
                if text:
                    extracted_text.append(text)
                else:
                    logging.warning(f"No text found on page {page_number}. It might be a scanned page.")
        full_text = "\n".join(extracted_text)
        if not full_text.strip():
            raise ValueError("No text extracted. The PDF might be scanned images.")
        normalized_text = unicodedata.normalize('NFC', ' '.join(full_text.split()))
        return normalized_text
    except Exception as e:
        logging.error(f"Failed to extract text from native PDF: {e}")
        raise


def parse_khmer_text_scanned(pdf_path: str, lang: str = "khm") -> str:
    """
    Extracts Khmer text from a scanned (image-based) PDF using OCR with pytesseract.

    :param pdf_path: Path to the input PDF file.
    :param lang: Tesseract language code for Khmer.
    :return: Extracted Khmer text.
    :raises Exception: If OCR fails.
    """
    extracted_text = []
    try:
        logging.info(f"Converting PDF to images: {pdf_path}")
        pages = convert_from_path(pdf_path, dpi=300)
        for page_number, page in enumerate(tqdm(pages, desc="Performing OCR on PDF"), start=1):
            logging.info(f"Processing page {page_number}")
            text = pytesseract.image_to_string(page, lang=lang)
            extracted_text.append(text)
        full_text = "\n".join(extracted_text)
        normalized_text = unicodedata.normalize('NFC', ' '.join(full_text.split()))
        return normalized_text
    except Exception as e:
        logging.error(f"Failed to perform OCR on scanned PDF: {e}")
        raise


def detect_pdf_type(pdf_path: str) -> str:
    """
    Detects whether the PDF is native (text-based) or scanned (image-based).

    :param pdf_path: Path to the input PDF file.
    :return: 'native' if text is found, 'scanned' otherwise.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    return 'native'
        return 'scanned'
    except Exception as e:
        logging.warning(f"Could not determine PDF type automatically: {e}")
        return 'scanned'  # Default to scanned if unsure


def generate_output_path(input_path: str) -> str:
    """
    Generates the output `.txt` file path based on the input PDF file path.

    :param input_path: Path to the input PDF file.
    :return: Path to the output `.txt` file.
    """
    base, _ = os.path.splitext(input_path)
    return f"{base}_PDF_Scanned.txt"


def parse_pdf(pdf_path: str, lang: str = "khm") -> Optional[str]:
    """
    Parses the PDF file and extracts Khmer text, handling both native and scanned PDFs.

    :param pdf_path: Path to the input PDF file.
    :param lang: Tesseract language code for Khmer.
    :return: Extracted Khmer text or None if extraction fails.
    """
    pdf_type = detect_pdf_type(pdf_path)
    logging.info(f"Detected PDF type: {pdf_type}")

    if pdf_type == 'native':
        logging.info("Attempting to extract text from native PDF.")
        try:
            text = parse_khmer_text_native(pdf_path)
            return text
        except Exception:
            logging.warning("Failed to extract text from native PDF. Attempting OCR.")
            # Fallback to OCR
            try:
                text = parse_khmer_text_scanned(pdf_path, lang=lang)
                return text
            except Exception as e:
                logging.error(f"Failed to extract text via OCR: {e}")
                return None
    elif pdf_type == 'scanned':
        logging.info("Performing OCR on scanned PDF.")
        try:
            text = parse_khmer_text_scanned(pdf_path, lang=lang)
            return text
        except Exception:
            logging.error("Failed to extract text via OCR.")
            return None
    else:
        logging.error("Unknown PDF type.")
        return None


def main():
    """
    Main function to execute the parsing and saving process.
    """
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Parse and extract Khmer text from a PDF file."
    )
    parser.add_argument(
        "input_pdf",
        help="Path to the input PDF file."
    )
    parser.add_argument(
        "--lang",
        default="khm",
        help="Tesseract language code for OCR (default: 'khm'). Ensure the Khmer language pack is installed."
    )

    args = parser.parse_args()
    input_path = args.input_pdf
    output_path = generate_output_path(input_path)

    if not os.path.isfile(input_path):
        logging.error(f"Input file not found: {input_path}")
        sys.exit(1)

    try:
        # Parse the PDF and extract text
        extracted_text = parse_pdf(input_path, lang=args.lang)

        if extracted_text:
            # Write the extracted text to the output file
            with open(output_path, 'w', encoding='utf-8') as out_file:
                out_file.write(extracted_text)
            logging.info(f"Extracted text saved to: {output_path}")
        else:
            logging.error("No text extracted from the PDF.")
            sys.exit(1)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
