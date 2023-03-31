import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#service = Service(executable_path ="C:\chromedriver.exe") Seems like it's not even needed any more.

def get_url():
    url = "https://www.demoblaze.com/"
    global driver
    driver = webdriver.Chrome()
    driver.get(url)

class DetailedException(Exception): #May this be usefull for some advanced exception managment?
    def __init__(self, arg):
        self.arg = arg

def headless_scrshot():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    headless_driver = webdriver.Chrome(options=options)

    try:
        headless_driver.get("https://www.demoblaze.com/")
        headless_driver.maximize_window()
        headless_driver.find_element(By.TAG_NAME, "body").screenshot("fullscreen.png")
    finally:
        headless_driver.quit()

def xpath_locate():
    get_url()

    try: # I would like to get rid of multiple try-except
        head_elem_cart = driver.find_element(By.XPATH, "//a[@id='cartur']")
    except:
        raise DetailedException('XPath: No such element!')

    else:
        print('XPath: Element is located')

    try:
        head_elem_contact = driver.find_element(By.XPATH, "//a[@data-target='#exampleModal']")
    except:
        raise DetailedException('XPath: No such element!')
    else:
        print('XPath: Element is located')

def link_check():
    #get_url()

    try:
        cat_div = driver.find_element(By.CSS_SELECTOR, "div.list-group")

    except:
        print('CSS: No such element!')
    else:
        print('CSS: Element is located')

    try: # Second one is NOT working.
        #OK cat_elem_laptops = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a#itemc.list-group-item:nth-child(3)")))
        #?cat_elem_laptops = driver.find_elemet(By.CSS_SELECTOR, "a.list-group-item:nth-of-type(3)")
        cat_elem_laptops = driver.find_element(By.CSS_SELECTOR, "[onclick=\"byCat(\'notebook\')\"]")
    except:
        print('CSS: No such element!')
    else:
        print('CSS: Element is located', cat_elem_laptops.get_attribute("href"))

    #****** Test whether 'Laptops' leads to a new page*****
    cat_elem_laptops.click()
    assert WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='tbodyid']/*")))
    assert WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='carousel-inner']/*")))
    print('"Laptops" page loading complete: products & header carousel are present')


def highest_price():
    #get_url()

    prices = []
    items = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,"//*[@class='card-block']/h5")))
    for x in items:
        prices.append(x.get_attribute("innerHTML").strip("$"))
    max_price = max(prices)
    print('Highest price is', max_price)


headless_scrshot()
xpath_locate()
highest_price()
link_check()






