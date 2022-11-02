from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/cats.html")

    browser.find_element(By.ID, "button")

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
