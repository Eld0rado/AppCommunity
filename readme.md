# Dog Breed Classifier

Cette application utilise Streamlit pour fournir une interface utilisateur permettant de classifier les races de chiens à partir d'images.

## Prérequis

- Python et pip

## Installation

1. Clonez le dépôt ou téléchargez le code source

   ```bash
   git clone https://github.com/Eld0rado/AppCommunity.git
   cd AppCommunity
   ```

2. Créez un environnement virtuel (optionnel)

   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows: env\Scripts\activate
   ```

3. Installez les dépendances nécessaires.

   ```bash
   pip install -r requirements.txt
   ```

## Fichiers nécessaires

- `dog_breed_classifier_lv2.h5` : Le fichier du modèle pré-entraîné.
- `encoder_dogs_classes_lite.pkl` : Le fichier de l'encodeur des 57 classes.

## Exécution de l'application

1. Lancez l'application Streamlit.

   ```bash
   streamlit run app.py
   ```

2. Une fois que l'application est lancée, ouvrez votre navigateur et accédez à l'adresse retournée.

3. Téléchargez une image de chien en utilisant le bouton de téléchargement et l'application prévoira la race du chien.

## Déploiement 

Créer votre repository Github avec ce code, executez l'application, accédez à l'interface, cliquez sur Deploy et suivez la procédure.  