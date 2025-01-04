import unittest
from unittest.mock import patch, mock_open
from khmer_pdf_parser import parse_khmer_text_native, parse_khmer_text_scanned
from PIL import Image

class TestKhmerPdfParser(unittest.TestCase):
    def test_parse_khmer_text_native(self):
        # Mock pdfplumber.open and its methods
        with patch('khmer_pdf_parser.pdfplumber.open') as mock_open_pdf:
            mock_pdf = mock_open_pdf.return_value.__enter__.return_value
            mock_page = mock_pdf.pages.__iter__.return_value
            mock_page.extract_text.return_value = "គម្រប សូមស្វាគមន៍"
            extracted_text = parse_khmer_text_native("dummy.pdf")
            self.assertEqual(extracted_text, "គម្រប សូមស្វាគមន៍")

    @patch('khmer_pdf_parser.convert_from_path')
    @patch('khmer_pdf_parser.pytesseract.image_to_string')
    def test_parse_khmer_text_scanned(self, mock_ocr, mock_convert):
        # Mock pdf2image.convert_from_path and pytesseract.image_to_string
        mock_convert.return_value = [Image.new('RGB', (100, 100))]
        mock_ocr.return_value = "សូមស្វាគមន៍"
        extracted_text = parse_khmer_text_scanned("dummy_scanned.pdf")
        self.assertEqual(extracted_text, "សូមស្វាគមន៍")

if __name__ == '__main__':
    unittest.main()
