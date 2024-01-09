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
        print('Headless Mode Enabled')

        chrome_driver_path = ChromeDriverManager().install()
        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        driver.set_window_size(1400, 1440)
        driver.get(URL)
        print(f'{URL}: Loaded')
        return driver

    except Exception as e:
        print('Error getting Chrome driver:', str(e))
        return None