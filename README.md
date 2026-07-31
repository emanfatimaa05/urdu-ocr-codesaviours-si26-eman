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

## Week 3 — Dataset Expansion & Dataset Class

- Expanded the dataset from 103 to 205 images across 6 categories:
  - Books (printed/Naskh)
  - Newspaper (Nastaliq)
  - Screenshots
  - Signboards
  - Synthetic
  - Handwritten
- Updated `data/labels.csv` with matching transcriptions for all new images
- Built a PyTorch `UrduOCRDataset` class (`__len__`, `__getitem__`) using `TrOCRProcessor` for image and text preprocessing
- Verified dataset loads correctly with proper tensor shapes:
  - `pixel_values`: `torch.Size([3, 384, 384])`
  - `labels`: `torch.Size([128])`
- Created train/test split: 164 training samples, 41 testing samples
- Notebook: `week3_dataset.ipynb`

  # Week 4 — Model Training & Evaluation

## Fine-Tuning the TrOCR Model

In Week 4, I fine-tuned Microsoft's **TrOCR Base Printed** model using my custom Urdu OCR dataset created during the previous weeks. The model was trained using PyTorch on Google Colab with GPU support.

### Training Configuration

- Model: Microsoft TrOCR Base Printed
- Framework: PyTorch
- Optimizer: AdamW
- Learning Rate: 5e-5
- Batch Size: 4
- Training Samples: 164
- Testing Samples: 41
- Epochs: 15
- Platform: Google Colab (GPU)

### Training Summary

The model successfully completed all 15 training epochs. During training, the loss gradually decreased, showing that the model was learning from the provided dataset.

### Evaluation Results

The trained model was evaluated on 41 unseen test images.

**Accuracy:** 0.0% (0/41 correct)

Although the model completed training successfully, most predictions were either empty or contained unreadable characters. This indicates that the model requires additional improvements before achieving usable OCR performance.

### Challenges

- Small dataset size (205 images)
- Complex Urdu script and ligatures
- Multiple fonts and handwriting styles
- Limited fine-tuning
- Tokenizer/model compatibility issues

### Future Improvements

- Increase the dataset size
- Collect more handwritten Urdu samples
- Improve preprocessing techniques
- Fine-tune for additional epochs
- Experiment with different hyperparameters
- Use a tokenizer better suited for Urdu text

**Notebook:** `week4_training.ipynb`

---

# Week 5 — Deployment

In Week 5, I deployed the Urdu OCR project as an interactive web application so users can upload Urdu text images and receive OCR predictions directly through a browser.

## Features

- Upload Urdu text images
- Automatic text extraction
- Simple and user-friendly interface
- Public deployment using Streamlit

## Live Demo

**Streamlit App**

https://urdu-ocr-codesaviours-si26-eman-bgk7cpwecpv7avzuqwdscg.streamlit.app

## Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- TrOCR
- Streamlit
- Google Colab
- GitHub

---

## Updated Repository Structure

```text
urdu-ocr-codesaviours-si26-eman/
│
├── README.md
├── SI26_Week1_Eman.ipynb
├── SI26_Week2_Eman.ipynb
├── week3_dataset.ipynb
├── week4_training.ipynb
├── app.py
├── requirements.txt
├── check_missing.py
│
└── data/
    ├── labels.csv
    └── raw/
        ├── books/
        ├── newspaper/
        ├── handwritten/
        ├── signboards/
        ├── screenshots/
        └── synthetic/
```

---

## Credits

**Eman Fatima**

Built during the **Code Saviours (SMC-PRIVATE) Limited ML/AI Internship Programme — Batch SI-26**


Machine Learning – Urdu OCR Project
