import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("select_browser", "get_driver")
class TestFrontEnd:

    def test_headerlinks(self):
        """Navigation bar links not broken. Clicked --> homepage"""
        header_nav_home = self.wait_css("ul.nav.navbar-nav.pull-center.dynamic_menu_texts>li>a[href='/']")
        header_nav_home.click()
        assert self.driver.current_url == 'https://courses.letskodeit.com/'

    def test_radio(self):
        """
        All buttons unselected at start
        if selected others are unselected
        another one selected, previous is unselected
        """
        cars_radio_buttons = self.wait_all_css(".left-align[id='radio-btn-example'] input")
        for x in cars_radio_buttons:
            assert not x.is_selected()
        cars_radio_buttons[0].click()
        i = 0
        while i < len(cars_radio_buttons):
            if cars_radio_buttons[i].is_selected():
                for x in cars_radio_buttons[i+1:]:
                    assert not x.is_selected()
                    break
            i +=1
        cars_radio_buttons[1].click()
        assert not cars_radio_buttons[0].is_selected()

    def test_checkbox(self):
        """
        All checkboxes are unchecked at start
        Get unchecked only when clicked on
        """
        cars_checkbox = self.wait_all_css("#checkbox-example-div label")
        for x in cars_checkbox:
            assert not x.is_selected()
            x.click()
        for x in cars_checkbox:
            assert x.is_selected()

        cars_checkbox[0].click()
        assert not cars_checkbox[0].is_selected()
        assert cars_checkbox[1].is_selected() and cars_checkbox[2].is_selected()

    def test_window_switch(self):
        """ Click a button -> go to the newly opened window -> select 'Python' from dropdown"""

        btn_openwindow = self.wait_css("#openwindow")
        btn_openwindow.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

        # selecting from down with and without importing Select
        # interesting part is page reloading after the first selection
        drop_down = self.wait_css(".form-control.categories.dynamic-text.m-l")
        drop_down.click()
        drop_option = self.wait_css(".form-control.categories.dynamic-text.m-l option:nth-child(5)")

        html = self.wait_css("html")  # with Select
        drop_option.click()  # without Select
        print('CLICKED')
        WebDriverWait(self.driver, 10).until(EC.staleness_of(html))  # with Select
        print('STALE')
        drop_down = self.wait_css(".form-control.categories.dynamic-text.m-l") # with Select
        print('DROPDOWN FOUND AGAIN')
        select_item = Select(drop_down)
        #Q Select(drop_down).select_by_visible_text didn't work
        select_item.select_by_visible_text("Python") # with Select

    def test_auto_suggest(self):
        input_field = self.wait_css("#autosuggest")
        input_field.send_keys("Py")
        expected = ['Selenium WebDriver Python', 'Appium Python', 'Python']
        suggestions = self.wait_all_css("#ui-id-1 a")
        for x in suggestions:
            assert x.get_attribute("innerHTML") in expected





































































