# Desafio Final — Projeto DevOps / Automação

Este repositório reúne o projeto final do desafio, com automações, scripts, configurações e artefatos desenvolvidos para demonstrar habilidades em DevOps, infraestrutura e automação.

## 🎯 Objetivo  
Desenvolver um projeto prático que reúna conhecimentos de infraestrutura, automação, versionamento, deploy, integração contínua ou outras práticas DevOps aprendidas ao longo do curso / desafio.

## 📂 Estrutura do repositório  
```text
.
├── README.md                # Este arquivo
├── scripts/                 # Scripts em Python, Bash ou outra linguagem
│   ├── script1.py
│   ├── script2.py
│   └── …  
├── infra/                   # Arquivos de infraestrutura (ex: Terraform, Ansible, CloudFormation)
│   └── …  
├── docs/                     # Documentação do projeto
│   └── …  
├── tests/                    # Casos de teste automatizados
│   └── …  
└── .github/                  # Workflows GitHub Actions (CI / CD)
    └── …  
🚀 Como executar / rodar localmente
Clone o repositório:

bash
Copiar código
git clone https://github.com/emilly-pereira/Desafio-Final.git  
cd Desafio-Final  
(Opcional) Crie um ambiente virtual se usar Python / outra linguagem:

bash
Copiar código
python -m venv .venv  
source .venv/bin/activate    # no Linux/macOS  
.venv\Scripts\activate       # no Windows  
Instale dependências (se houver):

bash
Copiar código
pip install -r requirements.txt  
Ou, para outras linguagens, siga instruções específicas nos scripts ou na pasta infra/.

Execute os scripts ou componentes:

Para scripts Python: python scripts/script1.py (ajuste para os nomes reais)

Para IaC / Ansible / Terraform: siga os passos dentro de infra/ (por exemplo terraform init, terraform apply, ou ansible-playbook …).

✅ Funcionalidades (o que o projeto entrega)
Liste aqui as principais funcionalidades ou automações que você implementou. Por exemplo:

Automação de deploy de serviço X

Provisionamento de infraestrutura com Terraform ou Ansible

Scripts utilitários para backup, limpeza, monitoramento

Pipeline de integração contínua usando GitHub Actions

Testes automatizados

(Adapte para o que seu repositório realmente contém)

🧪 Testes
Se existirem testes automatizados:

bash
Copiar código
cd tests  
pytest  
Ou outra ferramenta correspondente (Jest, unittest, etc).

📈 CI / CD
Descrição breve de como está configurado o pipeline do GitHub (ou outra ferramenta):

Build automático de scripts

Testes executados a cada push / PR

Deploy automático (se aplicável)

📚 Documentação
Se você mantiver uma pasta docs/, explique:

O que está documentado ali

Como navegar

Diagramas, fluxos, arquitetura

⚙️ Como contribuir
Fork o repositório

Crie uma branch de feature: git checkout -b feat/nova-funcionalidade

Faça commits claros e descritivos

Abra um Pull Request explicando a mudança

📝 Licença
Este projeto está licenciado sob a licença MIT (ou outra que você escolher). Veja o arquivo LICENSE para mais detalhes.

✉️ Contato
LinkedIn: [Seu LinkedIn]

Email: seu.email@exemplo.com

Se você quiser, posso verificar automaticamente os arquivos reais do repositório (você pode me dar uma listagem via código ou colar os nomes) e gerar um README exato e customizado baseado no que existe — quer que eu faça isso?







Você disse:
tenho esse repositório, acesse ele e de acordo com ele crie um novo readme
https://github.com/emilly-pereira/Desafio-Final.git


O ChatGPT disse:
Perfeito — com base no conteúdo real do repositório Desafio-Final, acessei e extraí as informações necessárias para criar um README atualizado e bem estruturado. Segue o novo README pronto para uso 👇 
GitHub

🚀 Desafio Final — Lab API e Pipeline DevOps Completo
API desenvolvida em Flask com foco em DevOps completo, integrando automação, containerização, CI/CD, deploy em Render, teste automatizado e documentação via Swagger. 
GitHub

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