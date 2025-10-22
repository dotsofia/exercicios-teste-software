import os
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

BASE_URL = "https://practicetestautomation.com"

def test_login_com_sucesso(chrome_driver):
    driver = chrome_driver
    login = LoginPage(driver, base_url=BASE_URL)
    dashboard = DashboardPage(driver, base_url=BASE_URL)

    login.abrir()
    login.fazer_login("student", "Password123")

    assert dashboard.esta_logado(), "Esperava estar logado mas o Dashboard não indica login"
    msg = dashboard.obter_mensagem_boas_vindas()
    assert "Logged In Successfully" in msg or "Logged In" in driver.page_source

def test_login_email_invalido(chrome_driver):
    driver = chrome_driver
    login = LoginPage(driver, base_url=BASE_URL)
    login.abrir()
    login.fazer_login("invalido@example.com", "Password123")
    err = login.obter_mensagem_erro()
    assert "Your username is invalid" in err or "invalid" in err.lower()

def test_login_senha_incorreta(chrome_driver):
    driver = chrome_driver
    login = LoginPage(driver, base_url=BASE_URL)
    login.abrir()
    login.fazer_login("student", "SenhaErrada")
    err = login.obter_mensagem_erro()
    assert "Your password is invalid" in err or "invalid" in err.lower()

def test_login_campos_vazios(chrome_driver):
    driver = chrome_driver
    login = LoginPage(driver, base_url=BASE_URL)
    login.abrir()
    login.fazer_login("", "")
    err = login.obter_mensagem_erro()
    assert err and ("invalid" in err.lower() or "required" in err.lower() or "please" in err.lower())
