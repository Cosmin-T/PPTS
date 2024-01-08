
import pandas as pd
import pygwalker as pyg
import time
import datetime
from deta import Deta
from logic.util import *
from logic.util import *
from st_aggrid import AgGrid



def addtotrack():
    deta = Deta(DETA_KEY)
    db = deta.Base('CostCleverItems')
    db2 = deta.Base('CostCleverTrack')

    items = db.fetch().items
    for item in items:
        db2.put(item)

    success = st.success('Done')
    time.sleep(2)
    success.empty()


def track():
    deta = Deta(DETA_KEY)
    db = deta.Base('CostCleverTrack')
    items = db.fetch().items
    if items:
        items_df = pd.DataFrame(items)
        items_df['Index'] = range(1, len(items_df) + 1)
        cols_to_include = ['Index', 'Product Name', 'Price', 'Availability', 'Rating', 'Date']
        items_df = items_df[cols_to_include]
        with st.expander('Show All Items', expanded=not items_df.empty):
            AgGrid(items_df, fit_columns_on_grid_load=True)
    else:
        information_2 = st.warning('No items found, you need to add some.')
        time.sleep(7)
        information_2.empty()


def search_db2_item(pname, pprice, pdata):
    deta = Deta(DETA_KEY)
    db = deta.Base('CostCleverTrack')
    items = db.fetch().items
    found_items = []
    progress_bar = st.progress(0)

    for i, item in enumerate(items):
        if is_item_match(item, pname, pprice, pdata):
            found_items.append(item)

    display_found_items(found_items, pname)

    progress_bar.progress(1)
    time.sleep(0.1)
    progress_bar.empty()


def delete_db2_items():
    deta = Deta(DETA_KEY)
    db = deta.Base('CostCleverTrack')
    items = db.fetch().items
    for item in items:
        db.delete(item['key'])
    delete = st.success('Done')
    time.sleep(2)
    delete.empty()


def delete_db2_searched_items(pname, pprice, pdata):
    deta = Deta(DETA_KEY)
    db = deta.Base('CostCleverTrack')
    items = db.fetch().items
    for i, item in enumerate(items):
        if is_item_match(item, pname, pprice, pdata):
            db.delete(item['key'])
    delete = st.success('Done')
    time.sleep(2)
    delete.empty()


def is_item_match(item, pname, pprice, pdata):
    item_name_lower = item['Product Name'].lower()
    pname_lower = pname.lower()


    name_condition = True
    for part in pname_lower.split():
        if part not in item_name_lower:
            name_condition = False
            break

    clean_price = item['Price'].replace(' Lei', '').replace('.', '').replace(',', '.')
    item_price = float(clean_price)
    price_condition = (item_price >= pprice[0] and item_price <= pprice[1])

    clean_date = datetime.datetime.strptime(item['Date'], '%Y-%m-%d').date()
    date_condition = (clean_date >= pdata[0] and clean_date <= pdata[1])

    return name_condition and price_condition and date_condition


def display_found_items(found_items, pname):
    if found_items:
        items_df = pd.DataFrame(found_items)
        items_df.reset_index(inplace=True)
        items_df['Index'] = range(1, len(items_df) + 1)
        items_df.rename(columns={'index': '#'}, inplace=True)
        cols_to_include = ['#', 'Product Name', 'Price', 'Availability', 'Rating', 'Date']
        items_df = items_df[cols_to_include]
        with st.expander('Show',  expanded=not items_df.empty):
            AgGrid(items_df, fit_columns_on_grid_load=True,
                   gridOptions={
                       'columnDefs': [{'field': col, 'width': 100 if col == '#' else 200} for col in items_df.columns]
                   })
            show_price_summary(found_items, pname)
    else:
        st.error('No items found.')


def show_price_summary(found_items, pname):
    highest_price_item = max(found_items, key=lambda x: float(x['Price'].replace(' Lei', '').replace('.', '').replace(',', '.')))
    lowest_price_item = min(found_items, key=lambda x: float(x['Price'].replace(' Lei', '').replace('.', '').replace(',', '.')))
    average_price = "".join(["{:,}".format(sum(int(item['Price'].replace(' Lei', '').replace('.', '').replace(',', '')) for item in found_items) // len(found_items) // 100).replace(',', '.'), ",", str(sum(int(item['Price'].replace(' Lei', '').replace('.', '').replace(',', '')) for item in found_items) // len(found_items) % 100).rjust(2, '0'), " Lei"])


    st.markdown("---")
    st.markdown(f"## Price Summary for '{pname}'")

    bento_style = """
    <style>
        .stPriceSummary {
            display: flex;
            justify-content: space-between;
            padding: 0 1rem;
        }
        .priceContainer {
            background: linear-gradient(200deg, #063c40 20%, #2c2b2d 90%); /* Gradient background similar to the .stApp */
            color: #fff;
            border: 1px solid #444;
            border-radius: 8px;
            padding: 1rem;
            flex: 1;
            margin: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.5);
            text-align: center;
            min-width: 0;
        }
        .stPriceSummary > div:not(:first-child) {
            margin-left: 20px;
        }
        .stPriceSummary > div:not(:last-child) {
            margin-right: 20px;
        }
        .priceDetail { /* New class for the price and date details */
            display: block; /* This ensures that the span acts like a div and respects the line breaks */
            white-space: nowrap; /* Prevent wrapping of content */
        }
    </style>
    """
    st.markdown(bento_style, unsafe_allow_html=True)

    bento_html = f"""
    <div class="stPriceSummary">
        <div class="priceContainer">
            <h4>Highest Price</h4>
            <span class="priceDetail">{highest_price_item['Price']}</span><br>
            <span class="priceDetail">{highest_price_item['Date']}</span>
        </div>
        <div class="priceContainer">
            <h4>Lowest Price</h4>
            <span class="priceDetail">{lowest_price_item['Price']}</span><br>
            <span class="priceDetail">{lowest_price_item['Date']}</span>
        </div>
        <div class="priceContainer">
            <h4>Average Price</h4>
            <span class="priceDetail">{average_price}</span><br>
            <!-- If you have a date for the average price, include it here -->
        </div>
    </div>
    """
    st.markdown(bento_html, unsafe_allow_html=True)