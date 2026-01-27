from selenium.webdriver.common.by import By

# Eu criei essa classe para guardar os endereços dos botões do site
class PaginaLogin:
    def __init__(self, driver):
        self.driver = driver
        
        # Guardei aqui os IDs que eu achei inspecionando o site no Chrome
        self.input_usuario = (By.ID, "user-name")
        self.input_senha = (By.ID, "password")
        self.botao_de_login = (By.ID, "login-button")

    # Esta função faz todo o trabalho de digitar e clicar
    def entrar_com_credenciais(self, usuario, senha):
        print(f"Tentando logar com o usuário: {usuario}")
        
        # Uso o '*' para o Selenium ler o (By.ID, "nome") de uma vez só
        self.driver.find_element(*self.input_usuario).send_keys(usuario)
        self.driver.find_element(*self.input_senha).send_keys(senha)
        self.driver.find_element(*self.botao_de_login).click()