import pytest
from selenium import webdriver
from waits import Wait


def pytest_addoption(parser):
    parser.addoption("--browser", help="Specifies which browser carries the test")


@pytest.fixture(scope="session")
def select_browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def get_driver(request, select_browser):
    if select_browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif select_browser.lower() == "firefox":
        driver = webdriver.Firefox()
    else:
        print("I used to love ol' good FF")
        driver = webdriver.Chrome()

    request.cls.driver = driver
    wait = Wait(driver, 10)
    request.cls.wait = wait
    request.cls.wait_css = wait.wait_css
    request.cls.wait_all_css = wait.wait_all_css
    driver.get("https://courses.letskodeit.com/practice")

    yield #driver Seems like not needed ?
    driver.quit()


