from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)

    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("Ivanov")
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("Ivan.Ivanov@example.com")
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
