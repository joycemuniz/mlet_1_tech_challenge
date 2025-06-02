
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


### 🔐 Login

Para a realização de login e obtenção do token utilize o usuário padrão "admin" e senha "admin".

```http
POST /login
Content-Type: application/json
```

**Exemplo de corpo da requisição:**

```json
{
  "username": "admin",
  "password": "admin"
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

🔗 [https://mlet-1-tech-challenge.vercel.app/apidocs/](https://mlet-1-tech-challenge.vercel.app/apidocs/)

---

## 🌐 Deploy

A aplicação está disponível em:

🔗 [https://mlet-1-tech-challenge.vercel.app/](https://mlet-1-tech-challenge.vercel.app/)

---

## 👥 Equipe

| Integrante                   | RM      | Contato                               |
|-----------------------------|---------|----------------------------------------|
| **Joyce Muniz de Oliveira** | 364278  | [joyce.muniz@hotmail.com](mailto:joyce.muniz@hotmail.com) |
| **Laís Lobo Teixeira**      | 363124  | [laisloboteixeira@gmail.com](mailto:laisloboteixeira@gmail.com) |
| **Bruno Oliveira Fermino**  | 363137  | [of.bruno9@hotmail.com](mailto:of.bruno9@hotmail.com) |
| **Victor Rodrigues Linhati**| 363151  | [victor_linhati@hotmail.com](mailto:victor_linhati@hotmail.com) |

---
## 📊 Dashboard Vitivinícola

Foi desenvolvido um dashboard interativo com Power BI para visualização dos dados.


### 🔗 Acesso ao Relatório Online
[Abrir no Power BI](https://app.powerbi.com/view?r=eyJrIjoiZmNmZmY0MDItOTUzZi00N2Q5LTk3NjYtZmVlNmUxOTkwZjExIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9)

### ▶️ Prévia

![ezgif com-speed (1)](https://github.com/user-attachments/assets/8b9477fa-1729-4bb2-823f-bf7be2edb082)

---

## 🧠 Futuras Extensões

- Cache dos dados em banco SQL ou NoSQL
- Protótipo de modelo preditivo baseado nos dados coletados

---

## 📈 Arquitetura do Projeto

![arquitetura_tech_challenge_1](https://github.com/user-attachments/assets/f9ec0c80-88c0-48b8-9273-a8068a5c1321)


---

## 🎥 Demonstração em Vídeo

📽️ Link: [https://youtu.be/seu_video_demo](https://youtu.be/seu_video_demo) *(substituir pelo link real)*
