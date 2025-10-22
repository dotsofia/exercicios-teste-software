import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import shutil

def tem_chrome_instalado():
    """Verifica se Chrome está instalado"""
    return shutil.which("google-chrome") is not None or shutil.which("chromium") is not None


@pytest.fixture
def chrome_driver():
    """Fixture que retorna uma instância do Chrome WebDriver"""
    if not tem_chrome_instalado():
        pytest.skip("Chrome não está instalado neste ambiente")
    
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    
    yield driver
    
    driver.quit()