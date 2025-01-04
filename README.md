# Khmer PDF Parser

A Python script to extract Khmer text from PDF files. It handles native (text-based) and scanned (image-based) PDFs by extracting selectable text or performing OCR respectively.
This code is for academic purposes for students and those working on Khmer Text and Document Processing. 

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Sample Files](#sample-files)
- [Error Handling](#error-handling)
- [Logging](#logging)
- [Testing](#testing)

## Features
```bash
- Dual Parsing Capability:
  - Native PDFs: Extract selectable Khmer text directly.
  - Scanned PDFs: Performs OCR to extract Khmer text from images.

- Simple Command-Line Interface: Specify the input PDF file as a positional argument.

- Automatic Output Naming: Generates a `.txt` file with the same base name as the input PDF.

- Robust Error Handling: Provides informative messages for common errors.

- Logging: Tracks the script's execution flow for easier debugging.
```
## Project Structure
```bash
khmer_pdf_parser/
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
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── LICENSE                      # License file
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-github-username/khmer_pdf_parser.git
cd khmer_pdf_parser

2. Install Python Dependencies
Ensure you have Python 3.6+ installed. Then, install the required Python packages using pip:

pip install -r requirements.txt

3. Install Tesseract OCR
Tesseract OCR is required for extracting text from scanned PDFs. Follow the instructions based on your operating system.

-Ubuntu:

sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-khm

-macOS (using Homebrew):

brew install tesseract
brew install tesseract-lang

-Windows:
Download Tesseract Installer:

Visit the UB Mannheim Tesseract Releases and download the latest installer.
Run the Installer:

Follow the installation prompts. By default, Tesseract will be installed in C:\Program Files\Tesseract-OCR\.
Install Khmer Language Pack:

Download khm.traineddata from the tessdata repository.
Place the khm.traineddata file in the tessdata folder, typically located at C:\Program Files\Tesseract-OCR\tessdata\.

##Usage
Basic Usage
Extract Khmer text from a PDF by specifying the input file. The script will automatically generate a .txt file with the extracted text.

python khmer_pdf_parser.py path/to/your/input.pdf

Example:

python khmer_pdf_parser.py sample_pdfs/native_sample.pdf

Output:

A file named sample_pdfs/native_sample.txt will be created with the extracted Khmer text.

Specify OCR Language (Optional)
If you have installed a different Khmer language pack or want to specify a different language code, use the --lang flag:

python khmer_pdf_parser.py path/to/your/input.pdf --lang khm

Sample Files
1. sample_pdfs/native_sample.pdf
A native PDF containing selectable Khmer text.

Example Content:

នេះគឺជាឧទាហរណ៍អត្ថបទខ្មែរដែលមាននៅក្នុងឯកសារ PDF ធម្មតា។
2. sample_pdfs/scanned_sample.pdf
A scanned PDF containing Khmer text as images.

Example Content:

Image-based representation of the following text:
នេះគឺជាឧទាហរណ៍អត្ថបទខ្មែរដែលមាននៅក្នុងឯកសារ PDF ដែលបានស្កែន។

Run Tests
Execute the following command to run all unit tests:
python -m unittest discover tests
