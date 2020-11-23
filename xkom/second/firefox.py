from selenium import webdriver
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger('TAU')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Firefox(executable_path='C:\\geckodriver.exe')

logger.info('Otwarcie strony w przeglądarce')
driver.get("https://www.x-kom.pl")

logger.info('Maksymalizacja onkna przeglądarki')
driver.maximize_window()

logger.info('Wyszukanie buttona do logowania i klknięci go')
driver.find_element_by_css_selector('.sc-13bjpvm-6.diZAHR a.sc-1h16fat-0.fz2r3r-6.cyvGmw').click()

logger.info('Wyszukanie pola loginu i wpisanie w nim wartości')
loginInput = WebDriverWait(driver, 10).until(exp.presence_of_element_located((By.CSS_SELECTOR, '.sc-1k5v2vw-1.gPbfDu.sc-3ncbnj-3.imstYS')))
loginInput.click()
loginInput.send_keys('dvulfskmfwpogsshnk@upived.com')

logger.info('Wyszukanie pola hasła i wpisanie w nim wartości')
passwordInput = driver.find_element_by_css_selector('.sc-1akovi1-1.cePceK.sc-3ncbnj-3.imstYS')
passwordInput.click()
passwordInput.send_keys('password123')

logger.info('Wyszukanie buttona logowania i wciśnięcie go')
driver.find_element_by_css_selector('button.sc-15ih3hi-0.dscwo7-3.dXIMSw.sc-6i4pc6-0.ipfaBG').click()






