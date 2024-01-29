import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

URL = 'http://localhost:8501/Search'
CROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
SEARCH_XPATH = '//*[@id="root"]/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[4]/div/div/div[2]/div/div[1]/div/input'
ITEMS = ['Macbook Air M2' + ' / ' + 'Macbook Air M3' + ' / ' + 'Iphone 15 Pro Max' + ' / ' + 'Iphone 15 pro']
TRY_AGAIN_XPATH = '//*[@id="root"]/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div[5]/div/div/div/div/div'
ADD_XPATH = '//*[@id="bui7__anchor"]/button'
CLEAR_XPATH = '//*[@id="bui3__anchor"]/button'



def main(URL):

    def sequence():
        print('Attenpting to click search')
        search_itmes = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, SEARCH_XPATH)))
        print('Clicked')
        search_itmes.send_keys(item + Keys.ENTER)
        print(f'Searching for: {item}')
        time.sleep(60)
        add_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ADD_XPATH)))
        add_btn.click()
        print('Presssed ADD')
        time.sleep(15)
        clear_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, CLEAR_XPATH)))
        clear_btn.click()
        time.sleep(15)

    command = ["/usr/local/bin/python3", "-m", "streamlit", "run", "/Volumes/Samsung 970 EVO/Documents/Python/PPTS/Homepage.py"]
    try:
        process = subprocess.Popen(command)

        chrome_options = Options()
        # chrome_options.add_argument('--headless')

        chrome_service = Service(executable_path=CROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.set_window_size(1400, 1440)
        driver.get(URL)
        print(f'{URL}: Loaded')

        time.sleep(5)

        for item in ITEMS:
            sequence()

            try:
                TRY_AGAIN = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, TRY_AGAIN_XPATH)))
                if TRY_AGAIN:
                    while True:
                        try:
                            sequence()
                            break
                        except:
                            sequence()
            except Exception as e:
                print("TRY_AGAIN not found, proceeding to next item")


    except Exception as e:
        print('Error initializing Chrome driver:', str(e))

    finally:
        driver.quit()
        process.terminate()
        print('Done Running')

if __name__ == "__main__":
    main(URL)