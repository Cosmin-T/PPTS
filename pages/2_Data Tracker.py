# DataTracker.py

import streamlit as st
from logic.search import *
from logic.webdriver import *
from logic.data_track import *
from logic.history import *
from logic.settings import *
import datetime

def data_track():
    with st.form('product_input_form2', clear_on_submit=False):
        PNAME = st.text_input('Product Name', placeholder='Type in the product you want to search for...')
        PPRICE = st.slider('Product Price', min_value=0, max_value=20000, value=(0, 8000))
        PDATE = st.date_input('Product Date', value=(datetime.datetime.now().date(), datetime.datetime.now().date()))

        col1, col2, col3, col4, col5, col6, col7 , col8, col9, col10, col11, col12 = st.columns(12)

        with col1:
            submit = st.form_submit_button('🔎')
        with col12:
            delete = st.form_submit_button("❌", help="Will delete all the items retrieved from the search.")


        if delete:
            with st.spinner('Deleting...'):
                delete_db2_searched_items(PNAME, PPRICE, PDATE)

        if submit:
            if len(PNAME) > 0 or len(PPRICE) > 0:
                if isinstance(PDATE, tuple) and len(PDATE) == 2:
                    with st.spinner('Searching...'):
                        search_db2_item(PNAME, PPRICE, PDATE)
                else:
                    st.error("Please Enter Valid Dates")
            else:
                st.error("Please Enter Product Name")

if __name__ == "__main__":
    apply_settings('eMag Product Management', CENTERED)
    data_track()