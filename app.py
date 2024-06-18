import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
from io import BytesIO
import pickle


encoder_file = 'encoder_dogs_classes_lite.pkl'
model = load_model("dog_breed_classifier_lv2.h5")

# Charger l'encodeur de classes à partir du fichier
with open(encoder_file, 'rb') as f:
    class_encoder = pickle.load(f)

# Afficher les classes d'origine
dog_breeds = class_encoder

def load_and_preprocess_image(file):
    img = Image.open(file)
    img = img.convert('RGB')
    img = img.resize((199, 199))
    return img

# Interface utilisateur Streamlit
st.title('Classification canine')
st.write('Transmettre une image de chien pour une prédiction de la race.')

uploaded_file = st.file_uploader("Choisir l'image pour la classification...", type="jpg")

if uploaded_file is not None:
    # Afficher l'image chargée
    img = load_and_preprocess_image(uploaded_file)
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    st.write("Traitement en cours...")
    
    # Prétraiter l'image
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    
    # Prédire la race
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    predicted_breed = dog_breeds[predicted_index]
    
    # Afficher la prédiction
    st.write(f'Retour: {predicted_breed}')