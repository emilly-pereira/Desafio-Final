<h1 align="center">🚀 Desafio Final – Pipeline DevOps</h1>

<p align="center">
  API Flask | CI/CD | GitHub Actions | Docker | Docker Compose | Render | Swagger | Testes Unitários 🧪
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue?logo=python"/>
  <img src="https://img.shields.io/badge/Flask-API-blueviolet?logo=flask"/>
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker"/>
  <img src="https://img.shields.io/badge/CI/CD-GitHub%20Actions-black?logo=githubactions"/>
  <img src="https://img.shields.io/badge/Deploy-Render-46E3B7?logo=render"/>
</p>

---

🧩 Sobre o Projeto
Este projeto apresenta uma API em Flask, totalmente containerizada e integrada a um pipeline CI/CD via GitHub Actions, com deploy automático na plataforma Render.

Aqui você encontra desde a execução local até o fluxo completo em ambiente de produção.
👩‍💻 Tecnologias Utilizadas:

✅ API REST com Flask

🐳 Docker & Docker Compose

⚙️ CI/CD com GitHub Actions

☁️ Deploy automático via plataforma Render

📚 Documentação interativa com Swagger UI

🧪 Testes unitários automatizados 


🌐 Deploy em Produção — Render (Destaque Principal)

O projeto está publicado e executando automaticamente na nuvem através da plataforma Render:

👉 https://desafio-final-kfbn.onrender.com

O Render é responsável por:

Fazer build automático da imagem usando seu Dockerfile

Realizar deploy contínuo a cada push na branch principal

Permitir visualização de logs, eventos de deploy e status do serviço

Gerenciar variáveis de ambiente

Disponibilizar endpoint público para consumo da API

📡 Como o deploy funciona

Você faz um push no GitHub

O Render detecta o commit automaticamente

Ele builda a imagem usando o seu Dockerfile

Sobe o container com sua aplicação Flask

Atualiza o serviço online

📄 Arquivo essencial para o Render

O deploy é feito usando diretamente o:

Dockerfile


O Render lê este arquivo para:

criar a imagem,

instalar dependências,

expor a porta correta,

iniciar o serviço.

🔍 Logs e Diagnóstico (Render Dashboard)

No Render, você tem acesso a:

Logs de build

Logs de execução da API

Status em tempo real

Erros de dependências

Histórico de deploys

Isso é muito útil para debug no backend.


🐳 Como rodar o projeto localmente

Abaixo você encontra todos os comandos essenciais, caso precise testar ANTES de enviar ao Render.

▶️ 1. Rodar normalmente (Python puro)
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


Acesse:
👉 http://127.0.0.1:1313/

🐳 2. Rodar usando Docker
Construir imagem
docker build -t lab_api .

Executar container
docker run -p 1313:1313 lab_api

🐳 3. Rodar usando Docker Compose
docker-compose up --build

📚 Documentação — Swagger

Você possui documentação interativa:

📍 /swagger

Arquivo utilizado:

static/swagger.json

🧪 Testes Automatizados

Para rodar localmente:

python -m unittest discover


Via Docker Compose:

docker-compose run api python -m unittest discover

⚙️ CI/CD — GitHub Actions

Pipeline localizado em:

.github/workflows/python-build.yml


Ele executa:

Instalação das dependências

Testes unitários

Build da aplicação

Validação antes de enviar para o Render

✨ Por que este projeto é relevante?

Este repositório demonstra experiência real com:

Criação de API profissional

Containerização com Docker

Pipeline CI/CD

Deploy automatizado em nuvem

Estrutura limpa, escalável e versão controlada

Documentação técnica com Swagger

Boas práticas DevOps

É um excelente projeto para portfólio.

🤝 Contribuições

Crie um fork

Abra uma branch

Faça alterações

Abra um Pull Request

📬 Contato

Quer falar comigo ou ver mais projetos?
Confira meu perfil no GitHub ou LinkedIn.