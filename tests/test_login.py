# Importo o mapa que eu fiz na pasta 'pages'
from pages.login_page import PaginaLogin

def test_login_com_sucesso(navegador):
    # Crio um objeto da minha página para poder usar as funções dela
    login = PaginaLogin(navegador)
    
    # Passo 1: Entrar no site da loja
    navegador.get("https://www.saucedemo.com/")
    
    # Passo 2: Usar a função de login que eu criei no arquivo login_page.py
    # Vou usar o usuário padrão que o site fornece para testes
    login.entrar_com_credenciais("standard_user", "secret_sauce")
    
    # Passo 3: Conferir se o login deu certo olhando a URL
    # Se aparecer 'inventory', eu sei que entrei na loja
    resultado_esperado = "inventory.html"
    assert resultado_esperado in navegador.current_url
    
    print(f"Sucesso: A URL contém '{resultado_esperado}' e o login funcionou!")