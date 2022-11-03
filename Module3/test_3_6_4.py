import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from selenium.webdriver.support.wait import WebDriverWait

lesson_ids = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]


@pytest.mark.parametrize('lesson_id', lesson_ids)
def test_stepic_feedback(browser, lesson_id):
    browser.implicitly_wait(10)
    link = f"https://stepik.org/lesson/{lesson_id}/step/1"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#ember32").click()
    browser.find_element(By.NAME, "login").send_keys("######")
    browser.find_element(By.NAME, "password").send_keys("######")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar__profile-img")))
    if browser.find_element(By.CSS_SELECTOR, ".attempt__actions button[type='button']").text == "Submit":
        print("\nsolve again was not displayed")
    else:
        browser.find_element(By.CSS_SELECTOR, ".again-btn").click()
        print("\nsolve again clicked")
    print("waited for log in")
    textarea = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
    print("waited textarea")
    textarea.send_keys(math.log(int(time.time())))
    print("sent keys to textarea")
    submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission")))
    submit.click()
    print("waited for Submit and clicked")
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".attempt-message_correct")))
    print("waited for correct label")
    actual_result = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    print("got actual test result")
    expected_result = "Correct!"
    assert actual_result == expected_result, \
        f"Actual message is '{actual_result}', expected is '{expected_result}'"
