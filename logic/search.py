
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from deta import Deta
import datetime
from logic.util import *
from logic.hcaptcha import *
from st_aggrid import AgGrid
import pandas as pd

def process_product(product_element):
    try:
        name = product_element.find_element(By.CLASS_NAME, 'card-v2-title').text
        rating = product_element.find_element(By.CLASS_NAME, 'average-rating').text
        price = product_element.find_element(By.CLASS_NAME, 'product-new-price').text
        availability = product_element.find_element(By.CLASS_NAME, 'card-estimate-placeholder').text

        if availability == '':
            availability = "în stoc"

    except NoSuchElementException:
        name, rating, price, availability = "N/A", "N/A", "N/A", "N/A"

    return {
        "Product Name": name,
        "Rating": rating,
        "Availability": availability,
        "Price": price,
        "Date": datetime.datetime.now().strftime("%Y-%m-%d")
    }

def data(driver, results_items_css, card_items_css):
    container = driver.find_element(By.CSS_SELECTOR, results_items_css)
    product_elements = container.find_elements(By.CSS_SELECTOR, card_items_css)

    progress_bar = st.progress(0)
    status_text = st.empty()
    status_text.info(f'Appending {len(product_elements)} products.')

    deta = Deta(DETA_KEY)
    db = deta.Base('CostCleverItems')
    all_items = db.fetch().items
    existing_product_names = {item['Product Name'] for item in all_items}

    duplicates_count = 0
    added_count = 0

    for i, product_element in enumerate(product_elements):
        product_data = process_product(product_element)
        if "N/A" not in product_data.values():
            if product_data['Product Name'] not in existing_product_names:
                db.put(product_data)
                existing_product_names.add(product_data['Product Name'])
                added_count += 1
                # status_text.text(f'Adding: {product_data["Product Name"]}')
            else:
                duplicates_count += 1

            progress_bar.progress((i + 1) / len(product_elements))
            time.sleep(0.1)
    progress_bar.empty()


    success_placeholder = st.empty()
    if added_count > 0:
        success_placeholder.success(f'Successfully added {added_count} new products.')

    warning_placeholder = st.empty()
    if duplicates_count > 0:
        warning_placeholder.warning(f'{duplicates_count} duplicates found and ignored.')

    time.sleep(0.5)
    status_text.empty()
    time.sleep(3)
    success_placeholder.empty()
    time.sleep(1)
    warning_placeholder.empty()

def search_items(driver, search_item_xpath, search_items, results_items_css, card_items_css):
    for search_it in search_items:
        try:
            search = driver.find_element(By.XPATH, search_item_xpath)
            if search:
                search.clear()
                search.send_keys(search_it + Keys.ENTER)
                time.sleep(1)

                data(driver, results_items_css, card_items_css)

        except NoSuchElementException:
            captcha_error = st.error('Captcha detected. Attempting to solve...')
            if captcha_error:
                # time.sleep(500)
                recaptcha(driver)
                captcha_error.empty()
                captha_succcess = st.success('Captcha solved. Searching again...')
                time.sleep(3)
                captha_succcess.empty()
            search.send_keys(search_it + Keys.ENTER)

        finally:
            driver.quit()
            print('Driver exited successfully.')

def delete_db_items():
    deta = Deta(DETA_KEY)
    db = deta.Base('CostCleverItems')
    items = db.fetch().items
    for item in items:
        db.delete(item['key'])
    delete = st.success('Done')
    time.sleep(2)
    delete.empty()

def show_db_items():
    deta = Deta(DETA_KEY)
    db = deta.Base('CostCleverItems')
    items = db.fetch().items
    if items:
        items_df = pd.DataFrame(items)
        items_df['Index'] = range(1, len(items_df) + 1)
        cols_to_include = ['Index', 'Product Name', 'Price', 'Availability', 'Rating', 'Date']
        items_df = items_df[cols_to_include]
        with st.expander('Show',  expanded=not items_df.empty):
            AgGrid(items_df, fit_columns_on_grid_load=True)
    else:
        information_2 = st.warning('No items found, you need to add some.')
        time.sleep(7)
        information_2.empty()

def reformat(search_items):
    result_string = ''
    for item in search_items:
        result_string += item + ' / '
    result = st.code(result_string.rstrip(' / '))
    return result
