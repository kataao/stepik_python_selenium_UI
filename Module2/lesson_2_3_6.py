from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    window2 = browser.window_handles[1]
    browser.switch_to.window(window2)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    print(x)
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    text = browser.switch_to.alert.text
    print(text)
    print(text.split(': ')[1])
    #pyperclip.copy(text.split(': ')[1])

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
