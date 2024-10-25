# PDF Splitter: Divide Large PDFs into Parts

This project provides a simple way to split large PDF files into multiple smaller files with a custom number of pages per part. It’s especially useful for handling lengthy PDFs, allowing for easier sharing and management.

## Features

- Split PDF files into multiple parts based on a specified number of pages.
- Customize the number of pages in the first and subsequent parts.
- Save each part in a specified directory with custom filenames.

## How It Works

The script uses Python's `PyPDF2` library to load and split a PDF file. The first part of the PDF is saved with a specified page count (e.g., 82 pages), while the rest are saved with another specified page count (e.g., 84 pages), ensuring flexibility in dividing content.

## Requirements

- Python 3.x
- [PyPDF2 library](https://pypi.org/project/PyPDF2/)

Install the `PyPDF2` library with:
```bash
pip install PyPDF2

