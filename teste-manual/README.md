Repositório de testes manuais criado para demonstrar conhecimentos em QA, incluindo escrita de casos de teste, documentação de bugs e rastreabilidade entre projetos.

Objetivo
Simular entregas reais de um analista de QA Jr, cobrindo desde o planejamento dos testes até o registro de evidências e bugs.

Ferramentas utilizadas

Jira
GitHub
Markdown


Estrutura do projeto
qa-manual-test-project/
├── casos-de-testes/
│   ├── calculadora_1rm/     -- casos de teste da calculadora de periodizacao
│   └── login/               -- casos de teste do sistema de login e cadastro
└── evidencias/              -- prints e registros do Jira

Projetos testados
Calculadora de Periodizacao e 1RM
Programa em Python para calcular cargas de treino com base no 1RM do usuário e gerar um plano de periodização semanal.
Repositório do código-fonte: https://github.com/lucasmontenegrodev/logica-programacao-python
Arquivo testado: Projetos/calculadora_periodizacao_1rm.py
Sistema de Login e Cadastro
Plano de teste manual cobrindo os fluxos de autenticação de um sistema web, incluindo cadastro, login, logout e recuperação de senha.
Aplicação utilizada: https://practice.expandtesting.com/login
O projeto de automação com Cypress cobrindo os mesmos cenários está disponível em:
https://github.com/lucasmontenegrodev/qa-cypress-login

Cobertura atual
ModuloCasos de testeTipos cobertosCalculadora de periodizacaoA definirFuncional, negativo, bordaLogin e cadastro16Positivo, negativo, seguranca, borda

Status
Projeto em desenvolvimento para fins de aprendizado e portifolio.