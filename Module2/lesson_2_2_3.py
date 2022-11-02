from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму заданных чисел
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    print(num1)
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    print(num2)
    x = int(num1) + int(num2)
    print(x)

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(str(x))

    # Нажать Submit
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
