# Search.py

import streamlit as st
from logic.search import *
from logic.webdriver import *
from logic.data_track import *
from logic.history import *
from logic.settings import *
import datetime

def search_data():
    headers = {
        'authorization': st.secrets['API_KEY'],
        'deta': st.secrets['DETA_KEY'],
    }
    try:
        driver = initialize_webdriver(URL)

        with st.form(clear_on_submit=True, key='products'):
            inf = st.info('Use the reformat form to convert "," into "/". Ex {test, test, test} will show as: {test / test / test}.')
            ITEMS = st.text_input('Reformat', placeholder='Type in multiple products separated by commas...')
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                if len(ITEMS) > 0:
                    with st.spinner('Loading...'):
                        itemss_list = [item.strip() for item in ITEMS.split(',')]
                        reformat(itemss_list)
                else:
                    st.error("Please Enter Product Name")

        with st.form(clear_on_submit=True, key='search'):
            inf2 = st.info('Once copied use it to do multi-product-search in the search form.')
            ITEM = st.text_input('Search', placeholder='Type product names separated by "/"...')

            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns(12)

            with col1:
                search_button = st.form_submit_button(label='🔎')
            if search_button:
                if len(ITEM) > 0:
                    with st.spinner('Loading...'):
                        items_list = [item.strip() for item in ITEM.split('/')]
                        search_items(driver, ITEM_XPATH, items_list, RESULT_ITEMS_CSS, CARD_ITEMS_CSS)
                else:
                    st.error("Please Enter Product Name")

            with col12:
                clear_button = st.form_submit_button("❌", help="Will delete all the items retrieved from eMag")
            if clear_button:
                with st.spinner('Clearing...'):
                    delete_db_items()

        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

        with col2:
            if st.button("➕", help="Will add all the items retrieved from eMag to Data-Tracker"):
                with st.spinner('Adding...'):
                    addtotrack()
        with col8:
            if st.button('⭕️', help="Will delete all items from Data-Tracker"):
                with st.spinner('Deleting...'):
                    delete_db2_items()

        st.markdown("---")
        st.write("## Items")
        information_1 = st.warning('The Items table is interactive. You can rearange, sort, filter, pin and export data. Right click on any cell to export')
        show_db_items()
        time.sleep(15)
        information_1.empty()
        time.sleep(15)
        inf.empty()
        inf2.empty()
    except Exception as e:
        print(f'Error: {e}')
        st.error('Please try again.')

if __name__ == '__main__':
    apply_settings('eMag Product Search',CENTERED)
    search_data()
