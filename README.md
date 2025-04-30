# Projeto de Processamento e Visualização de Dados da ANS

Este repositório contém um projeto completo envolvendo coleta, transformação, armazenamento e visualização de dados públicos da ANS (Agência Nacional de Saúde Suplementar), utilizando Python, Flask, PostgreSQL e Vue.js. O projeto demonstra um fluxo de trabalho desde a obtenção dos dados brutos até a apresentação interativa via web.

---

## ✔️ Tecnologias utilizadas

- Python 3.11
- Flask
- Pandas
- pdfplumber
- PostgreSQL + pgAdmin
- Vue.js 3
- Axios
- Postman
- PyCharm

---

## 📂 Estrutura do Projeto

```
ans_data_project/  # Nome sugerido para o diretório raiz
├── Part_01_Coleta/
│   ├── web_scrapping.py
│   ├── anexos/
│   │   ├── AnexoI.pdf
│   │   └── AnexoII.pdf
│   └── anexos.zip
│
├── Part_02_Extracao/
│   ├── data_transformation.py
│   ├── rol_de_procedimentos.csv
│   └── AnexoI_Processado.zip # Ex: Nome genérico para o zip de saída
│
├── Part_03_AnaliseDB/
│   ├── csv_standardization.py
│   ├── csvreader.py
│   ├── queries_ans.sql       # Ex: Nome genérico para as queries
│   └── outputs/
│       ├── output_query_a.csv # Ex: Nomes genéricos para os outputs
│       └── output_query_b.csv
│
├── Part_04_API_Frontend/
│   ├── backend/
│   │   ├── main.py
│   │   └── Relatorio_cadop.csv
│   └── frontend/
│       ├── src/
│       │   └── App.vue (customizado)
│       └── ...
│   # A coleção Postman está disponível no repositório para testes da API.
└── README.md
```
*(Nota: Os nomes de diretórios e alguns arquivos na estrutura acima são sugestões para desvincular do contexto de "teste". Se você alterar os nomes no seu repositório, lembre-se de ajustar os caminhos nos scripts e comandos.)*

---

## 📌 Parte 1 — Coleta de Dados ANS

### Objetivo:
Automatizar o download dos Anexos I e II disponibilizados pela ANS e armazená-los de forma organizada.

📄 Arquivo principal:
`Part_01_Coleta/web_scrapping.py`

### O que faz:
- Baixa os PDFs dos Anexos I e II.
- Salva os arquivos em `Part_01_Coleta/anexos/`.
- Compacta a pasta `anexos` no arquivo `anexos.zip`.

### Como executar:
```bash
cd Part_01_Coleta
pip install requests
python web_scrapping.py
```

---

## 🧾 Parte 2 — Extração PDF para CSV

### Objetivo:
Extrair a tabela principal do Anexo I (PDF) e transformá-la em um arquivo CSV estruturado, posteriormente compactado.

📄 Arquivo principal:
`Part_02_Extracao/data_transformation.py`

### Como executar:
```bash
cd Part_02_Extracao
pip install pdfplumber pandas
python data_transformation.py
```

### Resultado:
- `rol_de_procedimentos.csv`
- `AnexoI_Processado.zip` (Nome do ZIP alterado para exemplo genérico)

---

## 🐘 Parte 3 — Análise com PostgreSQL

### Objetivo:
Padronizar, carregar no PostgreSQL e analisar dados contábeis e cadastrais das operadoras da ANS utilizando SQL.

📁 Local: `Part_03_AnaliseDB`

### Componentes:
- `csv_standardization.py`: Padroniza arquivos CSV da ANS antes da carga.
- `csvreader.py`: Permite visualizar amostras dos arquivos padronizados.
- `queries_ans.sql`: Contém as consultas SQL para análise (executadas via pgAdmin ou cliente SQL).
- `outputs/`: Armazena os resultados das consultas exportados em CSV.

---

## 🌐 Parte 4 — API Flask + Frontend Vue.js

### Objetivo:
Desenvolver uma API RESTful (Flask) para busca textual em dados de operadoras ANS e um frontend interativo (Vue.js) para consumir essa API e visualizar os resultados.

---

### 🖥️ Backend (Flask)

📁 Local: `Part_04_API_Frontend/backend`

📄 Arquivo principal: `main.py`
📄 Dados utilizados: `Relatorio_cadop.csv`

### Como executar:
```bash
cd Part_04_API_Frontend/backend
pip install flask flask-cors pandas
python main.py
```
- A API estará disponível em: `http://localhost:5000`
- Exemplo de endpoint de busca: `GET /buscar-operadoras?query=unimed`

---

### 🌍 Frontend (Vue.js)

📁 Local: `Part_04_API_Frontend/frontend`

### Como iniciar:
```bash
cd Part_04_API_Frontend/frontend
npm install
npm run serve
```
- Aplicação acessível em: `http://localhost:8080`
- A interface permite a busca por nome, CNPJ ou registro ANS e exibe uma lista paginada dos resultados.

---
## 📬 Testes de API (Postman)

Uma coleção Postman (`*.postman_collection.json`) está incluída no repositório para facilitar os testes dos endpoints da API Flask.

---

## ✍️ Autor

**João Victor Tavares Esteves**
Engenharia de Computação – Universidade Federal do Ceará
📎 [www.linkedin.com/in/joaovtesteves](https://www.linkedin.com/in/joaovtesteves)
