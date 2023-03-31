from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class Wait(WebDriverWait):
    def wait_css(self, selector, timeout=10):
        return self.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_all_css(self, selector, timeout=10):
        return self.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))


"""
class Wait:
    def __init__(self):
        self.wait = Wait
"""






