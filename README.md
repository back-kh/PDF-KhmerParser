# Khmer PDF Parser

A straightforward Python script designed for students and researchers to extract Khmer text from PDF files. It adeptly handles both native (text-based) and scanned (image-based) PDFs by extracting selectable text or performing Optical Character Recognition (OCR), respectively. Leveraging established methods and libraries, the script ensures efficient processing of scanned and image-based documents, though native PDF extraction may face limitations with subscripts and segmentation.

Additionally, it supports advanced text processing functionalities such as keyword extraction and document retrieval, making it fast and portable for preprocessing tasks. For more complex tasks that require deeper analysis or handling intricate document structures, consider employing advanced and computationally intensive training methods, such as deep learning-based OCR models or custom-trained language processing algorithms.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Logging](#logging)
- [Testing](#testing)

## Features
```bash
- Dual Parsing Capability:
  - Native PDFs: Extract selectable Khmer text directly.
  - Scanned PDFs: Performs OCR to extract Khmer text from Scanned PDF File.
  - Text Image: Performs OCR to extract Khmer text from images
- Simple Command-Line Interface: Specify the input PDF file as a positional argument.

- Automatic Output Naming: Generates a `.txt` file with the same base name as the input PDF.

- Robust Error Handling: Provides informative messages for common errors.

- Logging: Tracks the script's execution flow for easier debugging.
```
## Project Structure
```bash
PDF-KhmerParser/
│
├── Sample/
│   ├── native_sample.pdf        # Sample native PDF with Khmer text
│   └── scanned_sample.pdf       # Sample scanned PDF with Khmer text
│
├── Extracted Text/
│   ├── native_sample.txt        # Output for native PDF
│   └── scanned_sample.txt       # Output for scanned PDF
│
├── PDF-KhParser - Scanned.py    # The main Python for Scanned PDF script
├── TextImage-KhParser.py        # The main Python for Text Images script
├── PDF-KhParser - Native 1.py   # The main Python for Native PDF script
├── PDF-KhParser - Native 2.py   # The main Python for Native PDF script
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── LICENSE                      # License file
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/back-kh/PDF-KhmerParser.git
cd PDF-KhmerParser
```
### 2. Install Python Dependencies
Ensure you have Python 3.6+ installed. Then, install the required Python packages using pip:
```bash
pip install -r requirements.txt
```
### 3. Install Tesseract OCR
Tesseract OCR is required for extracting text from scanned PDFs. Follow the instructions based on your operating system.
```bash
-Ubuntu:
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-khm

-macOS (using Homebrew):

brew install tesseract
brew install tesseract-lang

-Windows:
Download Tesseract Installer:

Visit the UB Mannheim Tesseract Releases (https://digi.bib.uni-mannheim.de/tesseract/) and download the latest installer.
Run the Installer:

Follow the installation prompts. By default, Tesseract will be installed in C:\Program Files\Tesseract-OCR\.
Install Khmer Language Pack:

Download khm.traineddata from the tessdata repository.
Place the khm.traineddata file in the tessdata folder, typically located at C:\Program Files\Tesseract-OCR\tessdata\.
```
## Usage
### 1. Basic Usage for Scanned PDF
Extract Khmer text from a Scanned PDF by specifying the input file. The script will automatically generate a .txt file with the extracted text.
```bash
python PDF-KhParser-Scanned.py path/input.pdf
```
Example:
```bash
python PDF-KhParser-Scanned.py Sample/Sample_PDF_Scanned.pdf
```
Output:

A file named Sample/Sample_Scanned.txt will be created with the extracted Khmer text.
### 2. Basic Usage for Text Image File
Extract Khmer text from a Text Image by specifying the input file (JPG,PNG). The script will automatically generate a .txt file with the extracted text.
```bash
python TextImage-KhParser.py path/input.jpg
```
Example:
```bash
python TextImage-KhParser.py Sample/Sample_TextImage.jpg
```
### 3. Basic Usage for Native PDF
Extract Khmer text from a Native PDF by specifying the input file. The script will automatically generate a .txt file with the extracted text.
```bash
python PDF-KhParser-Native 1.py path/input.pdf
```
or
```bash
python PDF-KhParser-Native 2.py path/input.pdf
```
Example:
```bash
python PDF-KhParser-Native 1.py Sample/Sample_PDF_Native.pdf
```
Output:

A file named Sample/Sample_Native.txt will be created with the extracted Khmer text.

Output Should be:
```bash
" ប្រទេសកម្ពុជាមានប្រវត្តិសាស្ត្រយូរអង្វែងដែលចាប់ផ្តើមនៅសតវត្សទី១ ព្រមទាំងមានវប្បធម៌ និងសិល្បៈចម្រើនយ៉ាងច្រើន។ ប្រទេសកម្ពុជាមានភាសាខ្មែរដែលមានអក្សរដែលមានភាព សម្បូរបែប និងវប្បធម៌ជាតិ និងអន្តរជាតិ។ 
ប្រជាជនកម្ពុជាស្ថិតនៅក្នុង សង្គមដែលមានការរួមបញ្ចូលគ្នា ដោយមានការកសាងសន្តិភាព និងការអភិវឌ្ឍន៍ជាច្រើនក្នុង វិស័យសេដ្ឋកិច្ច និងសង្គម។
ការអប់រំនិងការអភិវឌ្ឍន៍ បច្ចេកវិទ្យា កំបានក្លាយជាភាគីសំខាន់ ក្នុងការជួយសម្រលការរីកចម្រើន និងការបង្កើនគុណភាពជីវិតសម្រាប់ប្រជាជន។ "
```

### Logging
```bash
khmer_pdf_parser_native.txt
khmer_pdf_parser_scanned.txt
khmer_image_recognizer.txt
```
### Testing
Execute the following command to run all unit tests:
```bash
python -m unittest discover Test\tests.py
```
