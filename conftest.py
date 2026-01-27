import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Essa função serve para preparar o navegador antes de cada teste começar
@pytest.fixture
def navegador():
    # Passo 1: O programa baixa o driver do Chrome sozinho (facilitando minha vida)
    print("\n--- Abrindo o navegador Chrome ---")
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)
    
    # Eu gosto de deixar a tela cheia para evitar que botões sumam
    driver.maximize_window()
    
    # Aqui o código 'entrega' o navegador pronto para o teste usar
    yield driver 
    
    # Passo final: Depois que o teste acaba, ele fecha o navegador sozinho
    print("--- Fechando o navegador ---")
    driver.quit()