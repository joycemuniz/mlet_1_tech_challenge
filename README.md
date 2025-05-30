
# 🍇 API Vitivinícola - Tech Challenge FIAP

Este projeto foi desenvolvido como parte do **Tech Challenge da especialização em Machine Learning Engineering (FASE 1)** da FIAP. O objetivo é criar uma **API pública** capaz de realizar scraping em tempo real dos dados de **vitivinicultura** disponibilizados pela [Embrapa](http://vitibrasil.cnpuv.embrapa.br/) e disponibilizá-los por meio de endpoints no formato JSON.

## 📌 Sumário

- [🚀 Objetivo](#-objetivo)
- [🛠️ Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [📂 Estrutura do Projeto](#-estrutura-do-projeto)
- [⚙️ Instalação e Execução](#️-instalação-e-execução)
- [🔐 Autenticação](#-autenticação)
- [📡 Endpoints da API](#-endpoints-da-api)
- [📌 Categorias Disponíveis](#-categorias-disponíveis)
- [📅 Parâmetros de Ano](#-parâmetros-de-ano)
- [🧩 Exemplos de Requisições](#-exemplos-de-requisições)
- [📊 Swagger UI](#-swagger-ui)
- [🌐 Deploy](#-deploy)
- [👥 Equipe](#-equipe)
- [🧠 Futuras Extensões](#-futuras-extensões)
- [📈 Arquitetura do Projeto](#-arquitetura-do-projeto)
- [🎥 Demonstração em Vídeo](#-demonstração-em-vídeo)

---

## 🚀 Objetivo

Criar uma API RESTful que consulte dados diretamente do site da Embrapa, abrangendo as seguintes seções:

- Produção  
- Processamento  
- Comercialização  
- Importação  
- Exportação  

A API realiza scraping em tempo real e retorna os dados em formato JSON.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Flask
- BeautifulSoup
- Requests
- Flasgger (documentação Swagger)
- Flask-JWT-Extended (autenticação JWT)
- Vercel (Deploy)
- SQLAlchemy (registro de usuários)
- SQLite (banco local para autenticação)

---

## 📂 Estrutura do Projeto

```
📦 mlet_1_tech_challenge/
├── app.py                  # Ponto de entrada da API
├── auth.py                 # Registro, login e autenticação JWT
├── config.py               # Configurações da aplicação
├── requirements.txt        # Dependências
├── Swagger.yaml            # Documentação
├── scrapper/
│   ├── comercializacao.py
│   ├── exportacao.py
│   ├── importacao.py
│   ├── processamento.py
│   └── producao.py
├── vercel.json
└── README.md
```

---

## ⚙️ Instalação e Execução

```bash
git clone https://github.com/joycemuniz/mlet_1_tech_challenge.git
cd mlet_1_tech_challenge
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

---

## 🔐 Autenticação

A API exige autenticação via **JWT (JSON Web Token)** para acessar os endpoints protegidos.

### 📥 Registro

```http
POST /register
Content-Type: application/json
```

**Exemplo de corpo da requisição:**

```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

### 🔐 Login

```http
POST /login
Content-Type: application/json
```

**Exemplo de corpo da requisição:**

```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

### ✅ Resposta

```json
{
  "access_token": "..."
}
```

### 📌 Autorização

Use o token JWT retornado no header das requisições:

```http
Authorization: Bearer <access_token>
```

---

## 📡 Endpoints da API

| Método | Rota                             | Descrição                                                   |
|--------|----------------------------------|-------------------------------------------------------------|
| GET    | `/producao`                      | Retorna dados de produção por intervalo de anos.            |
| GET    | `/processamento/{categoria}`     | Retorna dados de processamento por categoria e ano.         |
| GET    | `/comercializacao`               | Retorna dados de comercialização por intervalo de anos.     |
| GET    | `/importacao/{categoria}`        | Retorna dados de importação por categoria e ano.            |
| GET    | `/exportacao/{categoria}`        | Retorna dados de exportação por categoria e ano.            |
| POST   | `/register`                      | Registra novo usuário.                                      |
| POST   | `/login`                         | Autentica usuário e retorna o JWT.                          |

---

## 📌 Categorias Disponíveis

### 🔹 **Processamento**
`GET /processamento/{categoria}`  
Categorias válidas:
- `viniferas`
- `americanas_hibridas`
- `uvas_mesa`
- `sem_classificacao`

### 🔹 **Importação**
`GET /importacao/{categoria}`  
Categorias válidas:
- `vinhos_mesa`
- `espumantes`
- `uvas_frescas`
- `uvas_passas`
- `sucos`

### 🔹 **Exportação**
`GET /exportacao/{categoria}`  
Categorias válidas:
- `vinhos_mesa`
- `espumantes`
- `uvas_frescas`
- `sucos`

---

## 📅 Parâmetros de Ano

Todos os endpoints de consulta aceitam os seguintes parâmetros opcionais:

- `ano_inicio` — valor mínimo: `1970`
- `ano_fim` — valor máximo: `2024`

---

## 🧩 Exemplos de Requisições

```http
GET /producao?ano_inicio=2000&ano_fim=2020
GET /processamento/viniferas?ano_inicio=2010
GET /comercializacao
GET /importacao/sucos
GET /exportacao/espumantes?ano_inicio=1995&ano_fim=2005
```

---

## 📊 Swagger UI

Acesse a documentação interativa da API em:

```
http://localhost:5000/apidocs/
```

---

## 🌐 Deploy

A aplicação está disponível em:

🔗 [https://vitivinicultura-api.vercel.app](https://vitivinicultura-api.vercel.app)

---

## 👥 Equipe

| Integrante                   | RM      | Contato                               |
|-----------------------------|---------|----------------------------------------|
| **Joyce Muniz de Oliveira** | 364278  | [joyce.muniz@hotmail.com](mailto:joyce.muniz@hotmail.com) |
| **Laís Lobo Teixeira**      | 363124  | [laisloboteixeira@gmail.com](mailto:laisloboteixeira@gmail.com) |
| **Bruno Oliveira Fermino**  | 363137  | [of.bruno9@hotmail.com](mailto:of.bruno9@hotmail.com) |
| **Victor Rodrigues Linhati**| 363151  | [victor_linhati@hotmail.com](mailto:victor_linhati@hotmail.com) |

---

## 🧠 Futuras Extensões

- Cache dos dados em banco SQL ou NoSQL
- Dashboard interativo no Power BI
- Protótipo de modelo preditivo baseado nos dados coletados
- Observabilidade com logs estruturados

---

## 📈 Arquitetura do Projeto

_(Inserir imagem ou diagrama de arquitetura aqui, se disponível)_

---

## 🎥 Demonstração em Vídeo

📽️ Link: [https://youtu.be/seu_video_demo](https://youtu.be/seu_video_demo) *(substituir pelo link real)*