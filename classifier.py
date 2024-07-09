import streamlit as st
import streamlit as st

from transformers import ViTForImageClassification, ViTFeatureExtractor
from PIL import Image
import torch

# Loading in Model
device = "cuda" if torch.cuda.is_available() else "cpu"
model = ViTForImageClassification.from_pretrained( "imjeffhi/pokemon_classifier").to(device)
feature_extractor = ViTFeatureExtractor.from_pretrained('imjeffhi/pokemon_classifier')

def pokemon_classifier():
    st.title("Pokemon Classifier")
    st.write("This is the Pokemon Classifier page")

    # Create an image uploader
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Process the uploaded image
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        # Add your image classification code here
        img = Image.open(uploaded_image)
        extracted = feature_extractor(images=img, return_tensors='pt').to(device)
        predicted_id = model(**extracted).logits.argmax(-1).item()
        predicted_pokemon = model.config.id2label[predicted_id]
        st.write(f"Predicted Pokemon: {predicted_pokemon}")
