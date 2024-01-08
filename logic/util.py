#util.py

import streamlit as st
from logic.config_ini import *

config = con()

URL = 'https://www.emag.ro/'
API_KEY = config['DEFAULT']['API_KEY']
DETA_KEY = config['DEFAULT']['DETA_KEY']
SITE_KEY = "//script[contains(text(), 'grecaptcha')]"

CROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
CAPSOLVER_EXTENSION_PATH = '/Volumes/Samsung 970 EVO/Documents/Python/PPTS/capsolver_ext'

CAPTCHA_FRAME = '#rcp > div > div.grecaptcha-logo > iframe'
CAPTCHA_ATTRIBUTE = 'data-hcaptcha-response'
CAPTCHA_FORM = '#cpf'
SUBMIT_CAPTCHA_CSS = 'document.getElementById("osub").click();'

WEBSITE_KEY = "f3e47f14-1d61-4170-a312-d2c8c1f91fc2"
CAPSOLVER_API_ENDPOINT = "https://api.capsolver.com/createTask"

ITEM_XPATH = '//*[@id="searchboxTrigger"]'
RESULT_ITEMS_CSS = '#card_grid'
CARD_ITEMS_CSS = '.card-item.card-standard.js-product-data'

CENTERED = 'centered'
WIDE = 'wide'