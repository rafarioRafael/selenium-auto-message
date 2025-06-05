# Utilizando Selenium para mandar mensagens
## Automoção de mensagem para o aplicativo Whatsapp

# 🤖 Zap Sender com Selenium

Este projeto automatiza o envio de mensagens no WhatsApp Web usando Python + Selenium.

## 🚀 Funcionalidades

- Envio automatizado de mensagens personalizadas
- Escolha aleatória de mensagens a partir de um arquivo JSON
- Carregamento de contatos a partir de um arquivo CSV
- Perfil persistente do navegador (não precisa logar toda vez)
- Possibilidade de agendamento (com `schedule`)

## 📁 Estrutura de Arquivos

├── frases/
│ └── goodnight.json # Frases de boa noite que serão enviadas
├── contatos.csv # Lista de nomes de contatos
├── whatsapp.py # Código principal
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto

## 📋 Exemplo de `contatos.csv`

```csv
nome
Fulano
Beltrano

pip install -r requirements.txt