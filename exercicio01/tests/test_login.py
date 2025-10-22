# tests/test_login.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE = "https://practicetestautomation.com/practice-test-login/"

def wait_for(driver, locator, timeout=5):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def submit_form(driver, username="", password=""):
    u = driver.find_element(By.ID, "username")
    p = driver.find_element(By.ID, "password")
    u.clear(); p.clear()
    if username:
        u.send_keys(username)
    if password:
        p.send_keys(password)
    driver.find_element(By.ID, "submit").click()

def get_flash_text(driver):
    try:
        el = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "error"))  # some pages use #error
        )
        return el.text
    except Exception:
        return driver.page_source

def test_login_success(chrome_driver):
    driver = chrome_driver
    driver.get(BASE)
    submit_form(driver, username="student", password="Password123")

    WebDriverWait(driver, 5).until(EC.title_contains("Logged In"))
    assert "Logged In Successfully" in driver.page_source or "Logged In Successfully" in get_flash_text(driver)

def test_login_invalid_email(chrome_driver):
    driver = chrome_driver
    driver.get(BASE)
    submit_form(driver, username="wrong@example.com", password="Password123")
    txt = get_flash_text(driver)
    assert "Your username is invalid" in txt or "Your username is invalid!" in txt or "invalid" in txt.lower()

def test_login_wrong_password(chrome_driver):
    driver = chrome_driver
    driver.get(BASE)
    submit_form(driver, username="student", password="WrongPass")
    txt = get_flash_text(driver)
    assert "Your password is invalid" in txt or "Your password is invalid!" in txt or "invalid" in txt.lower()

def test_login_empty_fields(chrome_driver):
    driver = chrome_driver
    driver.get(BASE)
    submit_form(driver, username="", password="")
    txt = get_flash_text(driver)
    # Either a specific validation message or some invalid message should appear
    assert txt and ("invalid" in txt.lower() or "required" in txt.lower() or "please" in txt.lower())

def test_error_messages_displayed(chrome_driver):
    driver = chrome_driver
    driver.get(BASE)
    # Invalid username
    submit_form(driver, username="baduser", password="Password123")
    txt1 = get_flash_text(driver)
    # Invalid password
    driver.get(BASE)
    submit_form(driver, username="student", password="badpass")
    txt2 = get_flash_text(driver)
    assert ("username" in txt1.lower() or "invalid" in txt1.lower())
    assert ("password" in txt2.lower() or "invalid" in txt2.lower())
