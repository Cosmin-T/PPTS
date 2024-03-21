
import pandas as pd
import pygwalker as pyg
import time
import datetime
import streamlit.components.v1 as stc
from st_aggrid import AgGrid
from deta import Deta
from logic.util import *
from logic.util import *
import re
import locale

def dashboard():
    deta = Deta(DETA_KEY)
    db = deta.Base('CostCleverTrack')
    items = db.fetch().items

    cleaned_items = []

    for item in items:
        clean_price = re.sub(r'[^0-9,]', '', item['Price']).replace(',', '.')

        try:
            item_price = float(clean_price)
            item['Price'] = item_price
            cleaned_items.append(item)
        except ValueError:
            print(f"Error: Could not convert '{item['Price']}' to a float.")
            return False

    if cleaned_items:
        items_df = pd.DataFrame(items)
        pyg_html = pyg.walk(items_df).to_html()

        if isinstance(pyg_html, str):
            custom_style = """
            <style>
            body, html {
                background-color: #1a1a1a !important; /* or use the specific color code for zinc-900 */
                color: #ffffff !important;
            }
            /* Add additional global styles for table, tr, td, th, etc., if necessary */
            </style>
            """

            head_index = pyg_html.find('</head>')
            if head_index != -1:
                    pyg_html = pyg_html[:head_index] + custom_style + pyg_html[head_index:]
            else:
                    pyg_html = custom_style + pyg_html

            stc.html(pyg_html, scrolling=True, height=893)
        else:
            print("Error: pyg.walk did not return a string.")