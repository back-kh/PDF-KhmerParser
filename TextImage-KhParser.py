#!/usr/bin/env python3
"""
khmer_image_recognizer.py

A Python script to recognize and extract Khmer text from image files using Tesseract OCR.
Supports image formats such as PNG, JPEG, TIFF, and more.

Usage:
    python khmer_image_recognizer.py path/to/input_image.jpg

Optional Arguments:
    --output, -o: Specify the output .txt file path. If not provided, the script will create a .txt file with the same base name as the input image.

Dependencies:
    - pytesseract
    - Pillow
    - tqdm

    Install via pip:
        pip install -r requirements.txt

Author:
    Your Name (https://github.com/your-github-username)
"""

import os
import sys
import argparse
import logging
import unicodedata
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from tqdm import tqdm
from typing import Optional

def setup_logging():
    """
    Configures logging for the script.
    Logs are written to both the console and a log file.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("khmer_image_recognizer.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )


def preprocess_image(image_path: str) -> Image.Image:
    """
    Preprocesses the image to improve OCR accuracy.

    Steps:
        - Convert to grayscale
        - Enhance contrast
        - Apply thresholding
        - Remove noise

    :param image_path: Path to the input image file.
    :return: Preprocessed PIL Image object.
    """
    try:
        image = Image.open(image_path)
        logging.info(f"Opened image file: {image_path}")

        # Convert to grayscale
        image = image.convert('L')
        logging.info("Converted image to grayscale.")

        # Enhance contrast
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2)
        logging.info("Enhanced image contrast.")

        # Apply thresholding
        image = image.point(lambda x: 0 if x < 140 else 255, '1')
        logging.info("Applied thresholding to image.")

        # Remove noise
        image = image.filter(ImageFilter.MedianFilter())
        logging.info("Applied median filter to remove noise.")

        return image
    except Exception as e:
        logging.error(f"Error during image preprocessing: {e}")
        raise


def extract_text_from_image(image: Image.Image, lang: str = "khm") -> str:
    """
    Extracts Khmer text from a preprocessed image using Tesseract OCR.

    :param image: Preprocessed PIL Image object.
    :param lang: Tesseract language code for Khmer.
    :return: Extracted Khmer text.
    """
    try:
        logging.info("Starting OCR on the image.")
        text = pytesseract.image_to_string(image, lang=lang)
        normalized_text = unicodedata.normalize('NFC', ' '.join(text.split()))
        logging.info("OCR completed successfully.")
        return normalized_text
    except Exception as e:
        logging.error(f"Error during OCR: {e}")
        raise


def generate_output_path(input_path: str, output_path: str = None) -> str:
    """
    Generates the output .txt file path based on the input image file path.

    :param input_path: Path to the input image file.
    :param output_path: User-specified output file path (optional).
    :return: Path to the output .txt file.
    """
    if output_path:
        return output_path
    base, _ = os.path.splitext(input_path)
    return f"{base}_TextImage.txt"


def parse_image(image_path: str, output_path: str = None, lang: str = "khm") -> Optional[str]:
    """
    Parses the image file and extracts Khmer text.

    :param image_path: Path to the input image file.
    :param output_path: Path to the output .txt file (optional).
    :param lang: Tesseract language code for Khmer.
    :return: Extracted Khmer text or None if extraction fails.
    """
    try:
        preprocessed_image = preprocess_image(image_path)
        extracted_text = extract_text_from_image(preprocessed_image, lang=lang)
        return extracted_text
    except Exception as e:
        logging.error(f"Failed to parse image: {e}")
        return None


def main():
    """
    Main function to execute the OCR process.
    """
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Recognize and extract Khmer text from image files using Tesseract OCR."
    )
    parser.add_argument(
        "input_image",
        help="Path to the input image file (e.g., PNG, JPEG, TIFF)."
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Path to the output .txt file. If not provided, the script will create a .txt file with the same base name as the input image."
    )
    parser.add_argument(
        "--lang",
        default="khm",
        help="Tesseract language code for OCR (default: 'khm'). Ensure the Khmer language pack is installed."
    )

    args = parser.parse_args()
    input_path = args.input_image
    output_path = generate_output_path(input_path, args.output)
    lang = args.lang

    if not os.path.isfile(input_path):
        logging.error(f"Input file not found: {input_path}")
        sys.exit(1)

    extracted_text = parse_image(input_path, output_path, lang)

    if extracted_text:
        try:
            with open(output_path, 'w', encoding='utf-8') as out_file:
                out_file.write(extracted_text)
            logging.info(f"Extracted text saved to: {output_path}")
        except Exception as e:
            logging.error(f"Failed to write extracted text to file: {e}")
            sys.exit(1)
    else:
        logging.error("No text extracted from the image.")
        sys.exit(1)


if __name__ == "__main__":
    main()
