# settings.py

import streamlit as st

def apply_settings(page_title, layout):
    # Set basic configurations for the Streamlit page.
    st.set_page_config(page_title=page_title,layout=layout)
    # st.title(f"{page_title} ")

    # Use custom CSS to hide the Streamlit's default menu, footer, and header for cleaner UI.
    hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # Insert your CSS style
    custom_css = """
    <style>
        body {
            background-color: #002b36;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #999;
            font-weight: 500;
            transition: color 0.3s;
        }
        .stApp {
            background: linear-gradient(-199deg, #063c40 5%, #1e1e1e 70%);
            border-radius: 10px;
            box-shadow: 3px 3px 20px rgba(0, 0, 0, 0.3);
            padding: 50px;
        }
        button[data-testid="baseButton-secondary"] {
        background-color: #newColor; /* Change #newColor to the color you want */
        color: #FFF;
        border: none;
        border-radius: 12px;
        }

        /* Targeting the first button on hover */
        button[data-testid="baseButton-secondary"]:hover {
            background-color: #newColorLighter; /* Change #newColorLighter to a lighter shade of your new color */
        }

        /* Targeting the second button directly */
        button[data-testid="baseButton-secondaryFormSubmit"] {
            background-color: #063b3f;
            color: #FFF;
            border: none;
            border-radius: 12px;
        }

        /* Targeting the second button on hover */
        button[data-testid="baseButton-secondaryFormSubmit"]:hover {
            background-color: #172a2b;
        }
        .st-emotion-cache-1wmy9hl e1f1d6gn0 {
        border: none;
        background: transparent;
        /* other properties to adjust spacing like margin or padding */
        margin: 0;
        padding: 0;
        }
    </style>

    """
    st.markdown(custom_css, unsafe_allow_html=True)

def setings_search(layout):
    apply_settings("eMag Product Search", layout)

def setings_data(layout):
    apply_settings("eMag Product Management", layout)

def setings_history(layout):
    apply_settings("eMag Product History", layout)