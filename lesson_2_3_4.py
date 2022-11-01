from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    browser.switch_to.alert.accept();

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    print(x)
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
