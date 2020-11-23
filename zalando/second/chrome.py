import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import logging

logger = logging.getLogger('TAU')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Chrome(ChromeDriverManager().install())

logger.info('Otwarcie strony w przeglądarce')
driver.get("https://www.zalando.pl/")

logger.info('Maksymalizacja onkna przeglądarki')
driver.maximize_window()

logger.info('Wyszukanie buttona do logowania i kliknięcie go')
driver.find_element_by_css_selector('a[href="/myaccount/"]').click()

logger.info('Wyszukanie pola loginu i wpisanie w nim wartości')
loginInput = WebDriverWait(driver, 10).until(exp.presence_of_element_located((By.ID, 'login.email')))
loginInput.click()
loginInput.send_keys('ngrmnanygopzqytejr@twzhhq.online')

logger.info('Wyszukanie pola hasła i wpisanie w nim wartości')
passwordInput = driver.find_element_by_id('login.password')
passwordInput.click()
passwordInput.send_keys('password123')

logger.info('Wyszukanie buttona logowania i wciśnięcie go')
driver.find_element_by_css_selector('[data-testid="login_button"]').click()

