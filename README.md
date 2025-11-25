🚀 Desafio Final — API Flask com Deploy Contínuo no Render

Este projeto implementa uma API REST em Flask, containerizada com Docker, testada automaticamente com GitHub Actions e implantada na nuvem via Render com deploy contínuo.
O foco principal é demonstrar um fluxo DevOps completo e funcional.

🌐 Deploy em Produção — Render (Destaque Principal)

🔗 URL pública:
👉 https://desafio-final-kfbn.onrender.com

O Render é responsável por:

🚀 Build automático a cada push na branch principal

🔄 Deploy contínuo usando o Dockerfile

📊 Dashboard com logs de build e execução

🔐 Gerenciamento de variáveis de ambiente

🌍 Entrega da API online 24h

⚙️ Como o Deploy Funciona

Você envia um commit para o GitHub

O Render detecta automaticamente a alteração

Ele executa o build da imagem usando o Dockerfile

Sobe o container em produção

Atualiza o endpoint imediatamente

🧩 Arquivo essencial usado no Render
Dockerfile


É o coração do deploy — o Render usa exatamente esse arquivo para:

Construir a imagem

Instalá dependências

Expor portas

Executar o serviço

📡 Logs no Render

No Render Dashboard, você pode visualizar:

Logs de build

Logs de execução

Histórico de deploys

Erros e eventos

Status da aplicação

Tudo em tempo real — ótimo para debugging.

🧱 Estrutura do Projeto
Desafio-Final/
│
├── .github/workflows/           # Pipeline CI/CD
│   └── python-build.yml
├── static/                      # Arquivos Swagger
│   └── swagger.json
├── testes/                      # Testes unitários
│   └── test_app.py
├── app.py                       # Código principal da API
├── requirements.txt             # Dependências Python
├── Dockerfile                   # Usado para build e deploy
└── docker-compose.yml           # Uso local com Docker Compose

🛠️ Como Rodar Localmente

Abaixo estão todos os comandos essenciais para testar antes do deploy.

▶️ 1. Rodar Localmente (Python)
Criar ambiente virtual
python -m venv .venv

Ativar ambiente

Windows:

.venv\Scripts\activate


Linux/macOS:

source .venv/bin/activate

Instalar dependências
pip install -r requirements.txt

Rodar a API
python app.py


📍 Acesse:
http://127.0.0.1:1313/

🐳 2. Rodar com Docker
Criar imagem
docker build -t lab_api .

Rodar container
docker run -p 1313:1313 lab_api

🐳 3. Rodar com Docker Compose
docker-compose up --build

📚 Documentação da API — Swagger

📍 /swagger

Swagger carregado automaticamente a partir de:

static/swagger.json


Interface gráfica disponível para testar todos os endpoints.

🧪 Testes Automatizados

Executar localmente:

python -m unittest discover


Executar via Docker Compose:

docker-compose run api python -m unittest discover

⚙️ Pipeline CI/CD — GitHub Actions

Pipeline localizado em:

.github/workflows/python-build.yml


Ele realiza:

🧩 Instalação de dependências

🧪 Execução dos testes unitários

🔍 Verificações antes do deploy

🏗️ Build automatizado

👩‍💻 Tecnologias Utilizadas
Categoria	Ferramenta
API	Flask
Tests	unittest
Containerização	Docker
Orquestração local	Docker Compose
Deploy	Render
CI/CD	GitHub Actions
Documentação	Swagger
✨ Destaques do Projeto

API real rodando em produção

Uso profissional de Docker e pipelines

Deploy automático sem precisar acessar servidor

Testes automatizados garantindo qualidade

Código organizado e documentado

Ideal para portfólio DevOps