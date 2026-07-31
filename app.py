import streamlit as st
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch
import gdown
import os

st.set_page_config(page_title="Urdu OCR — Code Saviours SI-26")

MODEL_DIR = "urdu_ocr_model"
DRIVE_FOLDER_ID = "1YSn8DiGFFPW2YwcnwenStQsgfkTzoD8T"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_DIR):
        gdown.download_folder(id=DRIVE_FOLDER_ID, output=MODEL_DIR, quiet=False)

    processor = TrOCRProcessor.from_pretrained(MODEL_DIR)
    model = VisionEncoderDecoderModel.from_pretrained(MODEL_DIR)
    model.eval()
    return processor, model

processor, model = load_model()

st.title("Urdu OCR — Code Saviours SI-26")
st.write("Upload an image containing Urdu text and get the extracted text.")

uploaded_file = st.file_uploader("Upload Urdu Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Extracting text..."):
        pixel_values = processor(image, return_tensors="pt").pixel_values
        with torch.no_grad():
            generated_ids = model.generate(pixel_values, max_new_tokens=64, num_beams=4)
        text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    st.subheader("Extracted Urdu Text")
    st.write(text if text else "Could not extract text from this image")
