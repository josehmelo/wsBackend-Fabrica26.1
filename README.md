# wsBackend-Fabrica26.1
Repositório para o desafio Fabrica de Software Backend 2026.1

# PokéDex Manager

Sistema de gerenciamento de coleções de Pokémon desenvolvido com Django, MySQL e Docker. Permite cadastrar treinadores, montar suas parties com dados reais consumidos da PokeAPI e gerenciar tudo através de uma interface web estilizada.

---

## Tecnologias

- Python 3.13
- Django 6.0
- MySQL 8.0
- Docker e Docker Compose
- Django REST Framework
- JWT (djangorestframework-simplejwt)
- PokeAPI (https://pokeapi.co)

---

## Funcionalidades

- CRUD completo de Treinadores
- Gerenciamento de Party (até 6 pokémons por treinador)
- Busca de pokémons em tempo real via PokeAPI
- Autenticação via JWT (registro e login)
- Interface web com tema inspirado na Pokédex oficial
- API REST documentada via Django REST Framework

---

## Estrutura do Projeto
```
pokedex-manager/
├── core/                  # configurações do projeto
├── treinadores/           # app de treinadores
├── party/                 # app de party de pokémons
├── services/              # consumo da PokeAPI
│   └── pokeapi.py
├── templates/             # templates HTML
│   ├── base.html
│   ├── treinadores/
│   └── party/
├── static/                # arquivos estáticos
│   └── css/
│       └── style.css
├── .env.example           # exemplo de variáveis de ambiente
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```

---

## Como rodar com Docker (recomendado)

### Pré-requisitos
- Docker Desktop instalado e rodando

### Passo a passo

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/pokedex-manager.git
cd pokedex-manager/pokedex-manager
```

2. Crie o arquivo `.env` baseado no exemplo
```bash
cp .env.example .env
```

3. Suba os containers
```bash
docker-compose up --build
```

4. Acesse no navegador
```
http://localhost:8000/treinadores/
```

> O banco de dados e as migrations são configurados automaticamente.

---

## Como rodar localmente

### Pré-requisitos
- Python 3.13+
- MySQL rodando localmente ou via Docker

### Passo a passo

1. Crie e ative o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
```

2. Instale as dependências
```bash
pip install -r requirements.txt
```

3. Configure o `.env`
```bash
cp .env.example .env
```
Edite o `.env` e altere `DB_HOST=db` para `DB_HOST=127.0.0.1`

4. Rode as migrations
```bash
python manage.py migrate
```

5. Inicie o servidor
```bash
python manage.py runserver
```

6. Acesse no navegador
```
http://127.0.0.1:8000/treinadores/
```

---

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

| Variável | Descrição | Exemplo |
|---|---|---|
| `SECRET_KEY` | Chave secreta do Django | `sua-chave-aqui` |
| `DEBUG` | Modo debug | `True` |
| `DB_NAME` | Nome do banco | `pokedex_db` |
| `DB_USER` | Usuário do banco | `pokedex_user` |
| `DB_PASSWORD` | Senha do banco | `pokedex_password` |
| `DB_HOST` | Host do banco | `db` (Docker) ou `127.0.0.1` (local) |
| `DB_PORT` | Porta do banco | `3306` |

---

## Endpoints da API

### Treinadores
| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/api/treinadores/registro/` | Registrar novo treinador |
| POST | `/api/treinadores/login/` | Login e obter tokens JWT |
| GET | `/api/treinadores/perfil/` | Ver perfil autenticado |

### Party
| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/api/party/<id>/` | Listar party do treinador |
| POST | `/api/party/<id>/adicionar/` | Adicionar pokémon via PokeAPI |
| DELETE | `/api/party/<id>/remover/<pk>/` | Remover pokémon da party |
| PATCH | `/api/party/<id>/atualizar/<pk>/` | Atualizar anotações |

---

## Entidades

### Treinador
| Campo | Tipo | Descrição |
|---|---|---|
| nome | CharField | Nome do treinador |
| email | EmailField | Email único |
| senha | CharField | Senha criptografada |
| bio | TextField | Biografia opcional |
| data_cadastro | DateTimeField | Data de cadastro automática |

### Party
| Campo | Tipo | Descrição |
|---|---|---|
| treinador | ForeignKey | Treinador dono da party |
| pokemon_id | IntegerField | ID na PokeAPI |
| pokemon_name | CharField | Nome do pokémon |
| pokemon_tipo | CharField | Tipo principal |
| pokemon_imagem_url | URLField | URL do sprite |
| data_captura | DateTimeField | Data de adição automática |
| anotacoes | TextField | Anotações opcionais |

---

## API Externa

Este projeto consome a [PokeAPI](https://pokeapi.co/api/v2/pokemon/) — uma API pública, gratuita e sem necessidade de autenticação.

Exemplo de chamada:
```
GET https://pokeapi.co/api/v2/pokemon/pikachu
```

---

## Autor

Desenvolvido por **José Henrique** como projeto de workshop de backend com Python e Django.
