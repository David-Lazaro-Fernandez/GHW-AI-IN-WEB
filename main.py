import streamlit as st
from classifier import pokemon_classifier
from pokedex import pokedex

# Sidebar
with st.sidebar:
    pg = st.navigation([
        st.Page(pokedex, title="Pokedex", icon="📱"),
        st.Page(pokemon_classifier, title="Pokemon Classificator", icon="🔍"),
    ])

pg.run()

