<h1 align="center">🚀 Lab API – Pipeline DevOps Completo</h1>

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

## 📌 Sobre o Projeto

Este projeto foi desenvolvido para estudos práticos de **DevOps**, integrando:

- API Flask
- Docker & Docker Compose
- Pipeline CI/CD com GitHub Actions
- Deploy automático no Render
- Testes Unitários
- Documentação interativa via Swagger

---

## 📁 Estrutura do Projeto

lab_api/
├─ .github/workflows/
│ └─ python-build.yml
├─ static/
│ └─ swagger.json
├─ tests/
│ └─ test_app.py
├─ app.py
├─ requirements.txt
├─ Dockerfile
└─ docker-compose.yml

yaml
Copiar código

---

# 🚀 Como Rodar o Projeto

## ▶ Rodar localmente (Python)

```bash
pip install -r requirements.txt
python app.py
Acesse:

cpp
Copiar código
http://127.0.0.1:1313/
▶ Rodar usando Docker
bash
Copiar código
docker build -t lab_api .
docker run -p 1313:1313 lab_api
▶ Rodar com Docker Compose
bash
Copiar código
docker-compose up --build
🧪 Testes Unitários
▶ Rodar localmente
bash
Copiar código
python -m unittest discover
▶ Rodar via Docker Compose
bash
Copiar código
docker-compose run api python -m unittest discover
🔍 Testando a API Manualmente (URLs)
Rota	Método	Descrição	Exemplo
/	GET	Verifica status da API	/
/items	GET	Lista de itens	/items
/login	POST	Gera token JWT	/login
/protected	GET	Requer token	/protected
/swagger/	GET	Documentação	/swagger/

🌐 Deploy no Render
O projeto faz deploy automático através do Dockerfile.

URL do serviço:
👉 https://desafio-final-kfbn.onrender.com

Logs:
Render → Seu Serviço → Logs

📘 Swagger UI
Documentação disponível em:

bash
Copiar código
/swagger/
Arquivo usado:

arduino
Copiar código
static/swagger.json
🤖 Pipeline CI/CD (GitHub Actions)
O workflow realiza:

✔ Checkout do código
✔ Setup Python
✔ Instala dependências
✔ Executa testes unitários
✔ Build da aplicação
✔ Upload de artifacts

Arquivo:

bash
Copiar código
.github/workflows/python-build.yml
🐳 Comandos Docker
bash
Copiar código
docker build -t lab_api .
docker run -p 1313:1313 lab_api
docker-compose up --build
docker-compose down
docker ps
docker stop <id>
🧰 Comandos Git
bash
Copiar código
git status
git add .
git commit -m "mensagem"
git push origin main
git pull
git checkout -b feature/nova-feature
