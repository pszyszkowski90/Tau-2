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
driver.get("https://www.x-kom.pl")

logger.info('Maksymalizacja onkna przeglądarki')
driver.maximize_window()

logger.info('Pobranie inputa wyszukiwania')
inputSearch = WebDriverWait(driver, 10).until(exp.presence_of_element_located((By.CSS_SELECTOR, 'input.sc-1hdf4hr-0.oGSDO')))

logger.info('Wpisanie wartości do wyszukiwania i zatwierdzenie wyszukiwania')
inputSearch.send_keys('Komputer')
inputSearch.send_keys(Keys.ENTER)

logger.info('Dodanie pierwszego elementu z listy do koszyka')
buttonAddToCart = WebDriverWait(driver, 10).until(exp.presence_of_element_located((By.CSS_SELECTOR, 'button.sc-15ih3hi-0.sc-1yu46qn-4.dmXSQX.sc-1j3ie3s-1.kqBTOy')))
buttonAddToCart.click()

logger.info('Zamknięcie potwierdzenia dodania do koszyka')
buttonClose = WebDriverWait(driver, 10).until(exp.presence_of_element_located((By.CSS_SELECTOR, 'button.sc-15ih3hi-0.an0bcv-4.an0bcv-12.dfoidd')))
buttonClose.click()

