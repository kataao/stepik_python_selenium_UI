from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами
    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    print(x)

    # Посчитать математическую функцию от x
    y = calc(x)
    print(y)

    # Ввести ответ в текстовое поле
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    # Отметить checkbox "I'm the robot"
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    # Выбрать radiobutton "Robots rule!"
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    # Нажать Submit
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
