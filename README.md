
# ✂️ GetBarber API

API REST desenvolvida em **Django + Django REST Framework** para gerenciamento de barbearias, serviços, agendamentos e usuários.

---

## 🚀 Tecnologias utilizadas

- Python 3
- Django
- Django REST Framework (DRF)
- Django REST Framework Authtoken
- SQLite (padrão, mas pode ser trocado por PostgreSQL/MySQL facilmente)
- drf-yasg (Swagger/OpenAPI) — (Se estiver implementado)
- Django CORS Headers

---

## 📚 Funcionalidades principais

- 📑 Cadastro e autenticação de usuários (Token Authentication)
- ✂️ CRUD de Barbearias
- 💈 CRUD de Serviços oferecidos
- 🧑‍💼 CRUD de Funcionários (Employee)
- 📆 Agendamento de horários
- 🔐 Autenticação e autorização nas rotas
- 🗒️ Documentação automática da API (se usando Swagger ou Redoc)

---

## 🔗 Rotas principais

### 🔐 **Autenticação**
| Método | Endpoint                         | Descrição                      |
|--------|-----------------------------------|---------------------------------|
| POST   | `/api/v1/accounts/register/`     | Registrar usuário               |
| POST   | `/api/v1/accounts/login/`        | Login e retorna Token           |
| POST   | `/api/v1/accounts/logout/`       | Logout (revoga Token)           |

### 🏢 **Barbearia**
| Método | Endpoint                         | Descrição                      |
|--------|-----------------------------------|---------------------------------|
| GET    | `/api/v1/barbershop/`            | Lista barbearias                |
| POST   | `/api/v1/barbershop/`            | Cria uma barbearia              |
| GET    | `/api/v1/barbershop/{id}/`       | Detalhe de uma barbearia        |
| PUT    | `/api/v1/barbershop/{id}/`       | Atualiza uma barbearia          |
| DELETE | `/api/v1/barbershop/{id}/`       | Deleta uma barbearia            |

### 🧑‍💼 **Funcionário**
| Método | Endpoint                         | Descrição                      |
|--------|-----------------------------------|---------------------------------|
| GET    | `/api/v1/employee/`              | Lista funcionários              |
| POST   | `/api/v1/employee/`              | Cria um funcionário             |
| GET    | `/api/v1/employee/{id}/`         | Detalhe de um funcionário       |
| PUT    | `/api/v1/employee/{id}/`         | Atualiza um funcionário         |
| DELETE | `/api/v1/employee/{id}/`         | Deleta um funcionário           |

### 🗓️ **Agendamento**
| Método | Endpoint                         | Descrição                      |
|--------|-----------------------------------|---------------------------------|
| GET    | `/api/v1/schedules/`             | Lista agendamentos              |
| POST   | `/api/v1/schedules/`             | Cria um agendamento             |

---

## 🛠️ Instalação e execução local

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/Augustodalmas/API-GetBarber.git
cd API-GetBarber
```

### 2️⃣ Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Crie um superusuário

```bash
python manage.py createsuperuser
```

### 6️⃣ Rode o servidor

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/admin para o painel administrativo.


---

## 🔑 Autenticação

Utiliza **Token Authentication**.

### ▶️ Exemplo de uso no Postman:

- Faça login no endpoint `/api/v1/accounts/login/`.
- Você receberá um token:

```json
{
  "token": "seu_token_aqui"
}
```

- Em cada requisição autenticada, vá na aba **Authorization** do Postman:

- Tipo: `Token`
- Token: `seu_token_aqui`

Ou nos headers:

```http
Authorization: Token seu_token_aqui
```
