import streamlit as st
from random import choice
import urllib.parse

st.title("RYM Random Genre Picker")

def generate_rym_url(genre_name):
    formatted = genre_name.lower().replace(" ", "-")
    encoded = urllib.parse.quote(formatted)
    return f"https://rateyourmusic.com/genre/{encoded}/"

try:
    with open("genres.txt", "r", encoding="utf-8") as file:
        genre_list = file.read().splitlines()

    if genre_list:
        st.success(f"{len(genre_list)} genres have been loaded.")
        if st.button("Generate Random Genre"):
            selected_genre = choice(genre_list)
            rym_url = generate_rym_url(selected_genre)
            st.markdown(f"[**{selected_genre}**]({rym_url})", unsafe_allow_html=True)
    else:
        st.warning("The file is empty.")

except FileNotFoundError:
    st.error("The file 'genres.txt' was not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")
