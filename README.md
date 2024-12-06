# Projeto Django - Gerenciamento de Carros

Este é um projeto em Django para gerenciar informações de carros, incluindo cadastro, edição, exclusão, relatórios e estatísticas.

---

## 🚀 **Funcionalidades**

- **Cadastrar carros:** Adicionar novos carros ao sistema.
- **Listar carros:** Visualizar todos os carros cadastrados.
- **Editar carros:** Atualizar informações de carros específicos.
- **Excluir carros:** Remover carros do sistema.
- **Gerar relatórios:** Criar relatórios detalhados sobre os carros.
- **Estatísticas:** Visualizar estatísticas relacionadas aos carros cadastrados.

---

## 🛠️ **Tecnologias utilizadas**

- **[Python](https://www.python.org/):** Linguagem de programação principal.
- **[Django](https://www.djangoproject.com/):** Framework para desenvolvimento web.
- **Banco de dados SQLite (padrão):** Configurado por padrão para simplificar o setup inicial.

---

## 📋 **Pré-requisitos**

- Python 3.8 ou superior instalado.
- Git instalado.
- (Opcional) Virtualenv para isolar dependências.

---

## 📦 **Como configurar o projeto**

### 1. Clone o repositório
```bash
git clone https://github.com/nogmois/project.git
cd project


# 1. Clonar o repositório
git clone https://github.com/nogmois/project.git
cd project

# 2. Criar e ativar o ambiente virtual (Linux/macOS)
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Configurar o banco de dados (opcional, caso queira ajustar algo no settings.py)

# 5. Aplicar as migrações
python manage.py makemigrations
python manage.py migrate

# 6. Criar um superusuário (será solicitado nome, email e senha)
python manage.py createsuperuser

# 7. Iniciar o servidor de desenvolvimento
python manage.py runserver

# Acesse em http://127.0.0.1:8000
```

## 🌐 **Rotas disponíveis**

| URL                        | Método       | Descrição                                    |
|----------------------------|--------------|---------------------------------------------|
| `/carros/cadastrar/`       | `GET`/`POST` | Cadastrar novos carros.                     |
| `/carros/`                 | `GET`        | Listar todos os carros cadastrados.         |
| `/carros/<int:pk>/editar/` | `GET`/`POST` | Editar informações de um carro específico.  |
| `/carros/<int:pk>/excluir/`| `POST`       | Excluir um carro específico.                |
| `/carros/relatorio/`       | `GET`        | Gerar relatório com informações dos carros. |
| `/estatisticas/`           | `GET`        | Visualizar estatísticas dos carros cadastrados. |

