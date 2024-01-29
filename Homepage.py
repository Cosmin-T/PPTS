# Homepage.py

import sys
import streamlit as st
print(sys.path)
from logic.util import *
from logic.settings import *
import requests

# For future usage
def homepage_lottie(lottie_url):
    r = requests.get(lottie_url)
    if r.status_code != 200:
        print(f"Failed to load {lottie_url}")
        return None
    return r.json()

def welcome():
    st.markdown("---")
    css = """
    .big-title {
    font-size: 180px;
    }
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='big-title'>Welcome!</h1>", unsafe_allow_html=True)
    for _ in range(10):
        _ = st.markdown("#")
    st.markdown("---")
    st.markdown("##### © CosminT")
    ct =(f'Copyright (c) 2024 CosminT, Romania. \nAll Rights Reserved.')
    st.text(ct)


if __name__ == "__main__":
    apply_settings('Product Price Tracker',CENTERED)
    welcome()
    # homepage_lottie('https://lottie.host/e5ceac0e-c034-40a8-8c4b-0c572e4e6800/lY54apUbbl.json')