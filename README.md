# Urdu OCR Project | Code Saviours SI-26 | Eman Fatima

## About

This repository contains my work for the Code Saviours Summer Internship 2026.
The goal of this project is to build an Urdu Optical Character Recognition (OCR) system capable of recognizing Urdu text from images.
I will update this repository every week with my notebook, dataset, code, and project progress.

## Week 1 Research Summary

### What is OCR?
OCR is a technology that converts printed or handwritten text from images into editable digital text.

### Why is Urdu OCR difficult?
Urdu is written from right to left, has connected letters, changing character shapes, and many similar-looking characters, making text recognition more challenging than English.

### Applications
- Digitizing Urdu books and newspapers.
- Converting printed Urdu documents into editable digital text.
  
## Dataset

The dataset for this project consists of Urdu text images collected from multiple sources. These images will be used to train an OCR model to recognize Urdu text from printed images.

### Dataset Sources

- Urdu newspapers
- Urdu books
- Urdu signboards
- Screenshots from Urdu news websites
- Public Urdu OCR datasets
- Synthetic Urdu text images

## Repository Structure

urdu-ocr-codesaviours-si26-eman/
│
├── README.md
├── SI26_Week1_Eman.ipynb
└── data/
    ├── labels.csv
    └── raw/
        ├── newspaper/
        ├── books/
        ├── signboards/
        ├── synthetic/
        └── other/


## Tools & Technologies

- Python
- Google Colab
- GitHub
- Hugging Face
- Pillow (PIL)
- Arabic Reshaper
- Python Bidi
- CSV
- Machine Learning
- Optical Character Recognition (OCR)

## Why We Need a Better Model

We tested Tesseract OCR (with its Urdu language pack) on 5 sample images from our preprocessed dataset to establish a baseline and understand its limitations.

### Results

**Image 1: book (23).png**
- Actual text: ہوٹل کا کھانا معیاری اور بہت مزے کا تھا۔
- Tesseract output: (empty)
- What went wrong: No output at all — complete failure to detect any text.

**Image 2: news (20).png**
- Actual text: 73 سالہ شبیر احمد... (long paragraph)
- Tesseract output: garbled text with wrong characters
- What went wrong: Attempted to read the text and got the general shape right, but substituted wrong letters throughout, especially where Urdu letters connect/join.

**Image 3: book (11).png**
- Actual text: ہوٹل کے واش روم گندے تھے۔ ہوٹل کی صفائی...
- Tesseract output: (empty)
- What went wrong: No output — same complete failure as Image 1.

**Image 4: screenshot (15).png**
- Actual text: زبان اردوئے معلّٰی
- Tesseract output: (empty)
- What went wrong: No output at all — screenshots may have background clutter or unusual fonts adding difficulty.

**Image 5: news (15).png**
- Actual text: انہوں نے کہا کہ وفاق کے جل اصلاحات کے لیے صوبوں...
- Tesseract output: mostly gibberish/disconnected letters, no coherent words
- What went wrong: Output looks like shapes were detected but not mapped into meaningful Urdu words.


## Author

**Eman Fatima**

Code Saviours Summer Internship 2026 (SI-26)

Machine Learning – Urdu OCR Project
