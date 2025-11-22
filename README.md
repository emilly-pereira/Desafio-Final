# Lab API - Pipeline DevOps (Build / Test / Deploy)

Projeto de exemplo para o laboratório: contém API Flask, Dockerfile, docker-compose, testes unitários e documentação via Swagger.

## Estrutura
```
lab_api/
├─ .github/
│  └─ workflows/
│     └─ python-build.yml
├─ static/
│  └─ swagger.json
├─ tests/
│  └─ test_app.py
├─ app.py
├─ requirements.txt
├─ Dockerfile
└─ docker-compose.yml
```

## Comandos Git (básicos)
- `git status`
- `git add .`
- `git commit -m "mensagem"`
- `git push origin main`
- `git checkout -b feature/minha-feature`
- `git pull`
- Criar o arquivo de workflow: o caminho deve ser `.github/workflows/python-build.yml`

## Comandos Docker / Docker Compose
- Build da imagem local: `docker build -t lab_api .`
- Rodar container: `docker run -p 1313:1313 lab_api`
- Usando docker-compose:
  - `docker-compose up` (ou `docker-compose up --build` para rebuild)
  - `docker-compose down`
  - `docker-compose build`
- Listar containers: `docker ps`
- Parar container: `docker stop <container_id>`

## Comandos Linux úteis (exemplos)
- `ls -la`
- `pwd`
- `cd /caminho/para/pasta`
- `mkdir nome_da_pasta`
- `rm -rf pasta_ou_arquivo`
- `cat arquivo.txt`
- `tail -f /var/log/syslog`
- `chmod +x script.sh`
- `ssh usuario@host`

## GitHub Actions (exemplo de workflow)
O arquivo `.github/workflows/python-build.yml` está incluído e realiza:
- checkout do código
- setup do python
- instalar dependências
- rodar testes
- construir pacote e upload do artifact

## Testes unitários
- Para rodar localmente: `python -m unittest discover`
- Se usando docker-compose:
  - `docker-compose run api python -m unittest discover`

## Swagger
- Após subir a API, abra: `http://localhost:1313/swagger`

## Imagem fornecida (anexo)
Arquivo anexo recebido: `/mnt/data/744927f9-a4c8-4a9b-8ba7-96b09d7b18f8.png`

## Observações / dicas
- Não esqueça de trocar `JWT_SECRET_KEY` em produção.
- Se for publicar no GitHub, adicione um workflow de CI (já incluido no repositório).
- Caso queira performs testes com `pytest` substitua os testes por estilo pytest.