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
Este projeto foi criado como um Desafio Final com objetivo de demonstrar a aplicação prática de conceitos DevOps em um fluxo completo:

✅ API REST com Flask

🐳 Docker & Docker Compose

⚙️ CI/CD com GitHub Actions

☁️ Deploy automático via plataforma Render

📚 Documentação interativa com Swagger UI

🧪 Testes unitários automatizados 
GitHub

📁 Estrutura do Projeto
text
Copiar código
Desafio-Final/
│
├── .github/workflows/           # Pipelines CI/CD configurados
│   └── python-build.yml
├── static/                      # Arquivos estáticos (Swagger UI / docs)
│   └── swagger.json
├── testes/                      # Testes unitários
│   └── test_app.py
├── app.py                       # API principal
├── requirements.txt             # Dependências Python
├── Dockerfile                   # Imagem base container
└── docker-compose.yml           # Orquestração via Docker Compose
GitHub

▶️ Como rodar o projeto
✅ Instalação local (Python)
bash
Copiar código
# Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows

# Instale dependências
pip install -r requirements.txt

# Execute a API
python app.py
🔥 Após iniciado, acesse:
📍 http://127.0.0.1:1313/ 
GitHub

🐳 Rodando com Docker
bash
Copiar código
# Construindo a imagem Docker
docker build -t lab_api .

# Executando o container
docker run -p 1313:1313 lab_api
Ou, para Docker Compose:

bash
Copiar código
docker-compose up --build
GitHub

🧪 Testes automatizados
Executar testes localmente:
bash
Copiar código
python -m unittest discover
Executar testes via Docker Compose:
bash
Copiar código
docker-compose run api python -m unittest discover
GitHub

🖥️ Documentação — Swagger UI
A documentação interativa está disponível via Swagger:

👉 Rota padrão:

bash
Copiar código
/swagger/
Arquivo usado:

arduino
Copiar código
static/swagger.json
GitHub

☁️ Deploy contínuo (Streaming no Render)
O deploy é feito automaticamente usando o arquivo Dockerfile, com versão publicada em:

🔗 https://desafio-final-kfbn.onrender.com 
GitHub

⚙️ Na plataforma Render, você também consegue acessar logs, monitorar deploys e configurar variáveis de ambiente. 
GitHub

✅ CI/CD com GitHub Actions
O pipeline automatizado executa os seguintes passos:

Etapa	Status Esperado
✅ Checkout do código	Faz o pull e clone
✅ Setup da runtime (Python)	Configura ambiente
✅ Instalação de dependências	Instala via pip
✅ Execução dos testes	Geração de resultados
✅ Build / packaging	Preparar imagem/app
✅ Deploy / artefatos	Build para deploy
GitHub

Arquivo de pipeline:

bash
Copiar código
.github/workflows/python-build.yml
GitHub

✨ Funcionalidades da API
Endpoint	Método	Descrição
/	GET	Verifica status da API
/items	GET	Retorna lista de itens
/login	POST	Gera token JWT para autenticação
/protected	GET	Requer token para acesso
/swagger/	GET	Documentação interativa
GitHub

🧰 Tecnologias utilizadas
Categoria	Ferramenta / Framework
💻 Linguagem	Python
☁️ API Framework	Flask
📦 Containerização	Docker / Docker Compose
⚙️ CICD	GitHub Actions
📚 Documentação	Swagger UI / JSON
🧪 Testes	unittest
🌐 Deploy	Render
GitHub

🔍 Dicas úteis
Adicione variáveis de ambiente no Render Dashboard para produção. 
GitHub

Estruture endpoints adicionais conforme necessidade (CRUDs, integração com banco etc.). 
GitHub

🤝 Como contribuir
Faça um fork deste repositório.

Crie um novo branch com sua feature:

bash
Copiar código
git checkout -b feature/nome-da-feature
Faça commits claros e coerentes.

Envie um Pull Request descrevendo as modificações.

📫 Contato
Caso queira falar comigo ou ver outros projetos:

🔗 LinkedIn e contato informados no perfil do GitHub. 
GitHub