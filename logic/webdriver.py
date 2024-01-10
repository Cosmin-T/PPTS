import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from logic.util import *
import time

def initialize_webdriver(URL):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')

        chrome_service = Service(executable_path=CROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        # driver.set_window_size(1400, 1440)
        driver.get(URL)
        print(f'{URL}: Loaded')
        return driver

    except Exception as e:
        print('Error initializing Chrome driver:', str(e))
        return None