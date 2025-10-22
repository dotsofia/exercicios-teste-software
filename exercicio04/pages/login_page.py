from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")
    FLASH_MESSAGE = (By.ID, "error")

    def abrir(self):
        super().abrir("/practice-test-login/")

    def preencher_email(self, email: str):
        self.digitar(self.EMAIL_INPUT, email)

    def preencher_senha(self, senha: str):
        self.digitar(self.PASSWORD_INPUT, senha)

    def clicar_login(self):
        self.clicar(self.LOGIN_BUTTON)

    def fazer_login(self, email: str, senha: str):
        self.preencher_email(email)
        self.preencher_senha(senha)
        self.clicar_login()

    def obter_mensagem_erro(self) -> str:
        txt = self.texto_de(self.FLASH_MESSAGE, timeout=2)
        if txt:
            return txt
        
        return self.driver.page_source
