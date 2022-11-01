from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    print(x)

    # Посчитать математическую функцию от x
    y = calc(x)
    print(y)

    # Проскроллить страницу вниз
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Ввести ответ в текстовое поле
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    # Отметить checkbox "I'm the robot"
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    # Выбрать radiobutton "Robots rule!"
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    # Нажать Submit
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
