from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    SUCCESS_TEXT_LOCATOR = (By.XPATH, "//*[contains(text(),'Logged In Successfully')]")
    FLASH_MESSAGE = (By.XPATH, "//*[contains(text(),'Logged In Successfully') or contains(text(),'Welcome')]")

    def esta_logado(self) -> bool:
        try:
            el = self.encontrar(self.SUCCESS_TEXT_LOCATOR, timeout=3)
            return el is not None
        except Exception:
            return False

    def obter_mensagem_boas_vindas(self) -> str:
        txt = self.texto_de(self.FLASH_MESSAGE, timeout=3)
        return txt or ""
