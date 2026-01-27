from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# --- CONFIGURAÇÃO INICIAL ---
# Aqui eu configuro o navegador. Uso o ChromeDriverManager para não ter que baixar o driver na mão.
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# --- MEU TESTE DE LOGIN ---
def test_fazer_login_no_saucedemo():
    # 1. Abrindo o site
    print("Iniciando o teste: Abrindo o site da loja...")
    navegador.get("https://www.saucedemo.com/")
    navegador.maximize_window()
    
    # Coloquei um tempo de espera para eu conseguir ver o que está acontecendo
    time.sleep(1)

    # 2. Localizando os campos e preenchendo
    # Eu inspecionei o site e vi que os IDs são 'user-name' e 'password'
    print("Digitando os dados de acesso...")
    campo_usuario = navegador.find_element(By.ID, "user-name")
    campo_senha = navegador.find_element(By.ID, "password")
    botao_login = navegador.find_element(By.ID, "login-button")

    campo_usuario.send_keys("standard_user")
    campo_senha.send_keys("secret_sauce")
    
    # 3. Clicando para entrar
    print("Clicando no botão de login...")
    botao_login.click()
    
    time.sleep(2)

    # 4. Verificando se deu certo (Assert)
    # Se o login funcionar, a URL tem que conter a palavra 'inventory'
    url_atual = navegador.current_url
    print(f"Validando a URL atual: {url_atual}")
    
    assert "inventory" in url_atual, f"Erro: Era esperado estar na página de produtos, mas estou em {url_atual}"

    print("Sucesso: O login funcionou perfeitamente!")

    # 5. Finalizando
    navegador.quit()

# Se eu quiser rodar esse arquivo direto pelo Python, eu chamo a função aqui
if __name__ == "__main__":
    test_fazer_login_no_saucedemo()