Projeto de Automacao de Testes - SauceDemo
Este repositorio contem a automacao de testes para o fluxo de login do site SauceDemo. O projeto foi desenvolvido como parte dos meus estudos em QA e automacao com Python e Selenium.

Objetivo
Validar se o login no sistema funciona corretamente utilizando credenciais validas, garantindo que o usuario seja redirecionado para a pagina de inventario da loja.

Tecnologias
Linguagem: Python 3.14

Automacao: Selenium WebDriver

Framework de Teste: Pytest

Arquitetura: Page Object Model (POM)

Gerenciamento de Driver: WebDriver Manager

Estrutura do Projeto
pages/: Contem os locators (IDs dos elementos) e as acoes da pagina de login.

tests/: Contem os scripts de teste que validam o comportamento do site.

conftest.py: Configuracao de abertura e fechamento do navegador (setup e teardown).

requirements.txt: Lista de bibliotecas instaladas no projeto.

Como rodar os testes
Ativar o ambiente virtual: .\venv\Scripts\activate

Instalar as dependencias: pip install -r requirements.txt

Executar os testes: pytest -s -v