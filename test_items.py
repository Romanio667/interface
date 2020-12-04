import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_guest_should_see_login_link(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(5)  
    button1 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'[type="submit"].btn.btn-lg'))
    )    
    x=browser.find_element_by_css_selector('[type="submit"].btn.btn-lg')
    assert x is not None, 'Кнопки нет'
    button1.click()