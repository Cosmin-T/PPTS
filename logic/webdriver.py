import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from logic.util import *
import time

def initialize_webdriver(URL):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        print('Headless Mode Enabled')

        driver = webdriver.Chrome(options=chrome_options)
        # driver.set_window_size(1400, 1440)
        driver.get(URL)
        print(f'{URL}: Loaded')
        return driver

    except Exception as e:
        print('Error initializing Chrome driver:', str(e))
        return None