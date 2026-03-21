# PokéDex Manager

> Sistema de gerenciamento de coleções de Pokémon com Django, MySQL e Docker

Um projeto backend completo que permite cadastrar treinadores, montar suas parties com até 6 pokémons cada, e consumir dados reais da PokeAPI. Implementa autenticação JWT, API REST completa e interface web estilizada.

---

## 📋 Índice

- [Tecnologias](#tecnologias)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Começando](#começando)
- [Variáveis de Ambiente](#variáveis-de-ambiente)
- [Endpoints da API](#endpoints-da-api)
- [Entidades](#entidades)
- [Troubleshooting](#troubleshooting)

---

## 🛠 Tecnologias

- **Python** 3.13
- **Django** 6.0
- **MySQL** 8.0
- **Docker** & Docker Compose
- **Django REST Framework** (API REST)
- **JWT** para autenticação (djangorestframework-simplejwt)
- **PokeAPI** (https://pokeapi.co)

---

## ✨ Funcionalidades

- ✅ CRUD completo de Treinadores
- ✅ Gerenciamento de Party (até 6 pokémons por treinador)
- ✅ Busca de pokémons em tempo real via PokeAPI
- ✅ Autenticação via JWT (registro e login)
- ✅ Interface web responsiva com tema Pokédex
- ✅ API REST documentada
- ✅ Migrações automáticas do banco de dados

---

## 📁 Estrutura do Projeto

```
pokedex-manager/
├── core/                      # Configurações do Django
│   ├── settings.py           # Variáveis e apps instalados
│   ├── urls.py               # Rotas principais
│   ├── asgi.py
│   └── wsgi.py
├── treinadores/              # App de Treinadores
│   ├── models.py             # Modelo de dados
│   ├── views.py              # Lógica de negócio
│   ├── serializers.py        # Serialização para API
│   ├── urls.py               # Rotas específicas
│   └── migrations/
├── party/                    # App de Party
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── migrations/
├── services/                 # Integrações externas
│   └── pokeapi.py           # Chamadas à PokeAPI
├── templates/                # Templates HTML
│   ├── base.html
│   ├── treinadores/
│   └── party/
├── static/                   # Arquivos estáticos
│   └── css/style.css
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Começando

### Opção 1: Com Docker (Recomendado)

#### Pré-requisitos
- Docker Desktop instalado e em execução

#### Passos:

1. **Clone o repositório**
```bash
git clone https://github.com/josehmelo/wsBackend-Fabrica26.1.git
cd wsBackend-Fabrica26.1/pokedex-manager
```

2. **Suba os containers**
```bash
docker-compose up --build -d
```

3. **Execute as migrações** (primeira execução)
```bash
docker-compose exec web python manage.py migrate
```

4. **Acesse a aplicação**
```
http://localhost:8000/treinadores/
```

> A aplicação estará disponível automaticamente. O banco de dados e migrations são configurados na primeira execução.

**Parar os containers:**
```bash
docker-compose down
```

---

### Opção 2: Ambiente Local (Windows/Mac/Linux)

#### Pré-requisitos
- Python 3.13 ou superior
- MySQL 8.0 (instalado e rodando)
- pip e venv

#### Passos:

1. **Clone o repositório**
```bash
git clone https://github.com/josehmelo/wsBackend-Fabrica26.1.git
cd wsBackend-Fabrica26.1/pokedex-manager
```

2. **Crie e ative o ambiente virtual**

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure o banco de dados**

Abra o `.env` (ou crie-o baseado no exemplo abaixo) e defina:
```
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
DB_NAME=pokedex_db
DB_USER=seu-usuario
DB_PASSWORD=sua-senha
DB_HOST=127.0.0.1
DB_PORT=3306
```

5. **Rode as migrations**
```bash
python manage.py migrate
```

6. **Inicie o servidor**
```bash
python manage.py runserver
```

7. **Acesse no navegador**
```
http://127.0.0.1:8000/treinadores/
```

---

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

| Variável | Tipo | Padrão | Descrição |
|---|---|---|---|
| `SECRET_KEY` | string | - | Chave secreta do Django (gere uma segura) |
| `DEBUG` | boolean | `True` | Modo debug (use `False` em produção) |
| `DB_NAME` | string | `pokedex_db` | Nome do banco de dados |
| `DB_USER` | string | `pokedex_user` | Usuário do MySQL |
| `DB_PASSWORD` | string | - | Senha do MySQL |
| `DB_HOST` | string | `db` (Docker) | Host do banco (`db` para Docker, `127.0.0.1` para local) |
| `DB_PORT` | integer | `3306` | Porta do MySQL |

**Exemplo (.env):**
```env
SECRET_KEY=django-insecure-sua-chave-segura-aqui
DEBUG=True
DB_NAME=pokedex_db
DB_USER=pokedex_user
DB_PASSWORD=senhaSegura123!
DB_HOST=127.0.0.1
DB_PORT=3306
```

---

## 📡 Endpoints da API

### Autenticação - Treinadores

| Método | Endpoint | Descrição | Autenticação |
|---|---|---|---|
| POST | `/api/treinadores/registro/` | Registrar novo treinador | Não |
| POST | `/api/treinadores/login/` | Login e obter JWT | Não |
| GET | `/api/treinadores/perfil/` | Ver perfil autenticado | JWT |
| PUT | `/api/treinadores/perfil/` | Atualizar perfil | JWT |

### Gerenciamento de Party

| Método | Endpoint | Descrição | Autenticação |
|---|---|---|---|
| GET | `/api/party/<id>/` | Listar party do treinador | JWT |
| POST | `/api/party/<id>/adicionar/` | Adicionar pokémon | JWT |
| DELETE | `/api/party/<id>/pokemon/<pk>/` | Remover pokémon da party | JWT |
| PATCH | `/api/party/<id>/pokemon/<pk>/` | Editar anotações | JWT |

---

## 📊 Entidades

### Modelo: Treinador

| Campo | Tipo | Validações | Descrição |
|---|---|---|---|
| `id` | Integer | PK | Identificador único |
| `nome` | CharField(100) | Obrigatório | Nome do treinador |
| `idade` | Integer | Obrigatório | Idade do treinador |
| `email` | EmailField | Único, Obrigatório | Email de cadastro |
| `senha` | CharField(128) | Hash PBKDF2 | Criptografada |
| `data_cadastro` | DateTime | Auto | Timestamp de criação |

### Modelo: Party

| Campo | Tipo | Validações | Descrição |
|---|---|---|---|
| `id` | Integer | PK | Identificador único |
| `treinador` | ForeignKey | Obrigatório | Referência ao Treinador |
| `pokemon_id` | Integer | Obrigatório | ID na PokeAPI |
| `pokemon_name` | CharField(100) | Obrigatório | Nome do pokémon |
| `pokemon_tipo` | CharField(50) | Obrigatório | Tipo principal |
| `pokemon_imagem_url` | URLField | Obrigatório | URL do sprite |
| `data_captura` | DateTime | Auto | Timestamp de adição |
| `anotacoes` | TextField | Opcional, Máx 500 | Notas do treinador |

---

## 🌐 API Externa

O projeto consome dados da **[PokeAPI](https://pokeapi.co/)** — uma API pública, gratuita e sem autenticação necessária.

**Exemplo de integração:**
```bash
GET https://pokeapi.co/api/v2/pokemon/pikachu
```

Detalhes completos em: https://pokeapi.co/docs/v2

---

## 🔧 Troubleshooting

### Docker

**Erro: "Connection refused" ao conectar no MySQL**
- Aguarde 10-15 segundos após executar `docker-compose up` — o MySQL leva tempo para iniciar
- Verifique se o container está rodando: `docker-compose ps`
- Veja os logs: `docker-compose logs web`

**Erro: "Port 3306 already in use"**
- Outro MySQL está rodando. Libere a porta ou mude em `docker-compose.yml`:
```yaml
ports:
  - "3307:3306"  # Mude 3307 para outra porta livre
```

### Ambiente Local

**Erro: "ModuleNotFoundError: No module named 'django'"**
- Ative o ambiente virtual: `venv\Scripts\activate` (Windows)
- Reinstale as dependências: `pip install -r requirements.txt`

**Erro: "MySQL server has gone away"**
- Verifique se MySQL está rodando
- Windows: `services.msc` → procure MySQL
- Mac: Verifique no System Preferences → MySQL
- Linux: `sudo systemctl status mysql`

**Erro: "Access denied for user"**
- Verifique as credenciais no `.env`
- Confirme que o usuário existe no MySQL:
```sql
SELECT user, host FROM mysql.user;
```

**Migrações não foram aplicadas**
- Execute manualmente: `python manage.py migrate`
- Crie superusuário (admin): `python manage.py createsuperuser`

---

## 📝 Autor

Desenvolvido como projeto de backend com Python e Django.

---

**Última atualização:** Março 2026
