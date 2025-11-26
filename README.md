# 🚀 Desafio Final — API Flask com Deploy Contínuo no Render

Este projeto implementa uma **API REST em Flask**, containerizada com Docker, testada automaticamente com GitHub Actions e implantada na nuvem via **Render** com deploy contínuo.  
O objetivo principal é demonstrar um fluxo **DevOps completo e funcional**.

---

# 🌐 Deploy em Produção — Render (Destaque Principal)

🔗 **URL pública:**  
👉 https://desafio-final-kfbn.onrender.com

O Render é responsável por:

- 🚀 Build automático a cada push na branch principal  
- 🔄 Deploy contínuo usando o `Dockerfile`  
- 📊 Dashboard com logs de build e execução  
- 🔐 Gerenciamento de variáveis de ambiente  
- 🌍 Serviço disponível 24h  

## ⚙️ Como o Deploy Funciona

1. Um commit é enviado para o GitHub  
2. O Render detecta a mudança automaticamente  
3. Realiza o build usando o `Dockerfile`  
4. Inicia o container na nuvem  
5. Atualiza o serviço instantaneamente  

### 🧩 Arquivo chave do Render

Dockerfile

yaml
Copiar código

Ele define:

- Instalação das dependências  
- Exposição da porta  
- Execução da aplicação  
- Build completo do container  

---

# 🧱 Estrutura do Projeto

```text
Desafio-Final/
│
├── .github/workflows/           # Pipeline CI/CD
│   └── python-build.yml
├── static/                      # Arquivos Swagger
│   └── swagger.json
├── testes/                      # Testes unitários
│   └── test_app.py
├── app.py                       # API principal em Flask
├── requirements.txt             # Dependências Python
├── Dockerfile                   # Configuração de build para Docker/Render
└── docker-compose.yml           # Orquestração local
🛠️ Como Rodar Localmente
Abaixo estão todos os comandos que você precisa para testar o projeto antes de enviar ao Render.

▶️ 1. Execução Local (Python)
Criar ambiente virtual
bash
Copiar código
python -m venv .venv
Ativar ambiente
Windows:

bash
Copiar código
.venv\Scripts\activate
Linux/macOS:

bash
Copiar código
source .venv/bin/activate
Instalar dependências
bash
Copiar código
pip install -r requirements.txt
Iniciar a API
bash
Copiar código
python app.py
📍 Acesse no navegador:
http://127.0.0.1:1313/

🐳 2. Execução via Docker
Construir imagem
bash
Copiar código
docker build -t lab_api .
Rodar container
bash
Copiar código
docker run -p 1313:1313 lab_api
🐳 3. Execução via Docker Compose
bash
Copiar código
docker-compose up --build
📚 Documentação da API — Swagger
Disponível em:

📍 /swagger

Usa o arquivo:

arduino
Copiar código
static/swagger.json
Permite testar endpoints com interface visual.

🧪 Testes Automatizados
Executar localmente:

bash
Copiar código
python -m unittest discover
Via Docker Compose:

bash
Copiar código
docker-compose run api python -m unittest discover
⚙️ CI/CD — GitHub Actions
Pipeline localizado em:

bash
Copiar código
.github/workflows/python-build.yml
Ele faz:

🧩 Instalação das dependências

🧪 Execução dos testes

🏗️ Validação do código

🔧 Preparação para deploy

👩‍💻 Tecnologias Utilizadas
Categoria	Ferramenta
API	Flask
Backend	Python
Documentação	Swagger
Testes	unittest
Containerização	Docker
Orquestração local	Docker Compose
Deploy	Render
CI/CD	GitHub Actions

