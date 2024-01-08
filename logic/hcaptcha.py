
import time
import sys
import re
import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.util import *
from twocaptcha import TwoCaptcha

def recaptcha(driver):
    solver = TwoCaptcha(API_KEY)

    try:
        time.sleep(10)

        script_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, SITE_KEY)))
        script = script_element.get_attribute('innerHTML')
        site_key = re.search("sitekey':'(.*?)'", script).group(1)
        print('Site Key:', site_key)

        print('Solving reCAPTCHA...')
        solved_captcha = solver.recaptcha(
            sitekey=site_key,
            url=driver.current_url
        )
        if solved_captcha:
            print(f'Solved: {solved_captcha}')

        print('Attempting to inject the token...')

        try:
            driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML = "{solved_captcha["code"]}";')
            print('Success: Token injected')
        except Exception as e:
            print("Failed to inject token:", e)

        time.sleep(5)

        print('Pressing Submit')
        if driver.execute_script(SUBMIT_CAPTCHA_CSS):
            print('Clicked Verify Button')

    except Exception as e:
        print("Encountered an error:", e)
