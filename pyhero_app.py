import streamlit as st
from huggingface_hub import HfApi

# Titre de l'application
st.title("PyHero")

# Menu de navigation
st.sidebar.title("Menu")
st.sidebar.markdown(" Sélectionnez une option :")

# Boutons de navigation
if st.sidebar.button("Cours", key="cours_button"):
    # Page de cours
    st.header("Cours")
    st.write("Sélectionnez un cours pour commencer :")
    cours = ["Python pour débutants", "Python pour intermédiaires", "Python pour avancés"]
    selected_cours = st.selectbox("Cours", cours)
    if selected_cours:
        st.write(f"Vous avez sélectionné le cours : {selected_cours}")
        # Ajouter des contenus au cours sélectionné
        if selected_cours == "Python pour débutants":
            st.write("Description du cours :")
            st.write("Ce cours est destiné aux débutants en Python. Nous allons apprendre les bases de la programmation en Python, notamment les variables, les types de données, les opérateurs, les boucles et les fonctions.")
            st.write("Programme du cours :")
            st.write("Semaine 1 : Introduction à Python")
            st.write("Semaine 2 : Variables et types de données")
            st.write("Semaine 3 : Opérateurs et boucles")
            st.write("Semaine 4 : Fonctions")
            st.write("Exemples de code :")
            st.code("print('Hello World!')")
            st.code("x = 5")
            st.code("y = x * 2")
            st.write("Exercices pratiques :")
            st.write("1. Écrire un programme qui affiche 'Hello World!'")
            st.write("2. Écrire un programme qui demande à l'utilisateur de saisir son nom et son âge")

if st.sidebar.button("Projets", key="projets_button"):
    # Page de projets
    st.header("Projets")
    st.write("Sélectionnez un projet pour commencer :")
    projets = ["Projet 1", "Projet 2", "Projet 3"]
    selected_projet = st.selectbox("Projet", projets)
    if selected_projet:
        st.write(f"Vous avez sélectionné le projet : {selected_projet}")
        # Ajouter des contenus au projet sélectionné
        if selected_projet == "Projet 1":
            st.write("Description du projet :")
            st.write("Ce projet consiste à créer un jeu de mots. Nous allons apprendre à utiliser les boucles et les conditions pour créer un jeu de mots interactif.")
            st.write("Programme du projet :")
            st.write("Semaine 1 : Introduction au projet")
            st.write("Semaine 2 : Création du jeu de mots")
            st.write("Semaine 3 : Ajout de fonctionnalités")
            st.write("Exemples de code :")
            st.code("for i in range(10):")
            st.code("print(i)")
            st.write("Ressources supplémentaires :")
            st.write("https://www.example.com")

if st.sidebar.button("Rétroaction", key="retroaction_button"):
    # Page de rétroaction
    st.header("Rétroaction")
    st.write("Sélectionnez une rétroaction pour commencer :")
    retroactions = ["Rétroaction 1", "Rétroaction 2", "Rétroaction 3"]
    selected_retroaction = st.selectbox("Rétroaction", retroactions)
    if selected_retroaction:
        st.write(f"Vous avez sélectionné la rétroaction : {selected_retroaction}")
        # Ajouter des contenus à la rétroaction sélectionnée
        if selected_retroaction == "Rétroaction 1":
            st.write("Description de la rétroaction :")
            st.write("Cette rétroaction consiste à évaluer vos compétences en Python.")

if st.sidebar.button("Hugging Face", key="hugging_face_button"):
    # Page de Hugging Face
    st.header("Hugging Face")
    st.write("Bienvenue sur la page de Hugging Face!")

    # Créez une instance de l'API de Hugging Face
    api = HfApi()

    # Modèles
    st.write("Les modèles sur Hugging Face sont des réseaux de neurones pré-entraînés pour résoudre des tâches spécifiques telles que la classification \
           de texte, la traduction automatique, la reconnaissance d'images, etc.")