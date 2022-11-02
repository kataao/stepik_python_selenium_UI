from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestReg(unittest.TestCase):
    def steps(self, link):
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".first_block input.first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block input.second").send_keys("Ivanov")
        browser.find_element(By.CSS_SELECTOR, ".first_block input.third").send_keys("Ivan.Ivanov@example.com")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        actual_welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        expected_welcome_text = "Congratulations! You have successfully registered!"
        self.assertEqual(actual_welcome_text, expected_welcome_text,
                         f"Actual welcome text '{actual_welcome_text}' "
                         f"doesn't correspond to expected '{expected_welcome_text}")
        browser.quit()

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.steps(link)

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.steps(link)


if __name__ == "__main__":
    unittest.main()

