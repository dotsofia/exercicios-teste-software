from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple, Optional

class BasePage:
    """Métodos utilitários comuns a todas as páginas."""
    def __init__(self, driver: WebDriver, base_url: str = ""):
        self.driver = driver
        self.base_url = base_url.rstrip("/")

    def abrir(self, path: str = "") -> None:
        url = f"{self.base_url}/{path.lstrip('/')}" if path else self.base_url
        self.driver.get(url)

    def _wait(self, locator: Tuple[By, str], timeout: int = 8):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def encontrar(self, locator: Tuple[By, str], timeout: int = 8):
        return self._wait(locator, timeout)

    def clicar(self, locator: Tuple[By, str], timeout: int = 8) -> None:
        el = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        el.click()

    def digitar(self, locator: Tuple[By, str], texto: str, timeout: int = 8) -> None:
        el = self._wait(locator, timeout)
        el.clear()
        el.send_keys(texto)

    def texto_de(self, locator: Tuple[By, str], timeout: int = 8) -> Optional[str]:
        try:
            el = self._wait(locator, timeout)
            return el.text
        except Exception:
            return None
