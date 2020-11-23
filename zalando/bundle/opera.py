import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

logger = logging.getLogger('TAU')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Opera(executable_path='C:\\operadriver.exe')

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

time.sleep(2)

logger.info('Pobranie inputa wyszukiwania')
inputSearch = WebDriverWait(driver, 10).until(exp.presence_of_element_located((By.CSS_SELECTOR, 'input.z-navicat-header_searchInput')))

logger.info('Wpisanie wartości do wyszukiwania i zatwierdzenie wyszukiwania')
inputSearch.send_keys('Kurtka')
inputSearch.send_keys(Keys.ENTER)

logger.info('Dodanie pierwszego elementu i otwarcie jego podstrony')
elementProduct = WebDriverWait(driver, 10).until(exp.presence_of_element_located((By.CSS_SELECTOR, '.qMZa55.SQGpu8.iOzucJ.JT3_zV.DvypSJ')))
elementProduct.click()

logger.info('Dodanie produktu do koszyka')
buttonAddToCart = WebDriverWait(driver, 10).until(exp.presence_of_element_located((By.CSS_SELECTOR, '.z-pdp__dx_cta_container button')))
buttonAddToCart.click()

logger.info('Wybór rozmiaru produktu')
sizeOption = WebDriverWait(driver, 10).until(exp.presence_of_element_located((By.CSS_SELECTOR, '[name="size-picker-form"] label')))
sizeOption.click()

