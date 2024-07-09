import streamlit as st
import requests

def pokedex():
    # Main
    st.title("Pokemon Dashboard")

    # Fetching all pokemons from the PokeAPI
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10")
    if response.status_code == 200:
        data = response.json()
        pokemons = data["results"]
        

        cols = st.columns(3)
        
        for index, pokemon in enumerate(pokemons):
            col = cols[index % 3]  # Cycle through columns
            
            with col:
                with st.container(border=True):
                    st.write(pokemon["name"])
                    pokemon_individual_info_url = pokemon["url"]
                    pokemon_info_response = requests.get(pokemon_individual_info_url)
                    if pokemon_info_response.status_code == 200:
                        pokemon_data = pokemon_info_response.json()
                        sprite_front = pokemon_data["sprites"]["front_default"]
                        st.image(sprite_front, width=75)
                    else:
                        st.error(f"Failed to fetch sprite for {pokemon['name']}")
    else:
        st.error("Failed to fetch pokemons from the API")

