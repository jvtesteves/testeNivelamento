# Teste nivelamento - João Victor Tavares Esteves

Este repositório contém as quatro atividades do Teste de Nivelamento, desenvolvidas com foco em manipulação de dados públicos da ANS (Agência Nacional de Saúde Suplementar).

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
- VSCode / PyCharm

---

## 📂 Estrutura do Projeto

```
testeNivelamento/
├── atividade1/         # Download dos anexos (web_scrapping.py)
├── atividade2/         # Extração e transformação de dados PDF → CSV + ZIP
├── atividade3/         # PostgreSQL: carga e queries
├── backend/            # Flask API (atividade 4)
├── frontend/           # Vue.js interface (atividade 4)
└── README.md
```

---

## 📌 Atividade 1 — Download dos Anexos

### Objetivo:
Fazer o download automático dos anexos disponibilizados pela ANS e compactá-los em um único arquivo ZIP.

### Como foi feito:

Um script Python foi desenvolvido para realizar o processo completo:

📄 `atividade1/web_scrapping.py`

- Baixa os arquivos:
  - Anexo I (Rol de Procedimentos)
  - Anexo II (Diretrizes de Utilização)
- Salva os PDFs na pasta `anexos/`
- Compacta ambos no arquivo `Anexos.zip`

### Como executar:

```bash
pip install requests
python web_scrapping.py
```

### Resultado:

- `anexos/AnexoI.pdf`
- `anexos/AnexoII.pdf`
- `Anexos.zip`

---

## 🧾 Atividade 2 — Processamento de dados PDF

### Objetivo:
Extrair as tabelas do Anexo I (PDF) e gerar um arquivo CSV + ZIP.

### Como executar:

1. Instale os requisitos:
   ```bash
   pip install pdfplumber pandas
   ```

2. Rode o script:
   ```bash
   python data_transformation.py
   ```

3. Resultado:
   - `rol_de_procedimentos.csv`
   - `Teste_JoaoVictorTavaresEsteves.zip`

---

## 🐘 Atividade 3 — Análise com PostgreSQL (pgAdmin)

### Objetivo:
Carregar os dados padronizados da ANS no banco e realizar análises SQL.

### Tabelas criadas:
- `demonstracoes_contabeis`
- `operadoras_ativas`

### Execução:

1. Os dados foram carregados via comandos `COPY` no **pgAdmin**.
2. Foram realizadas consultas SQL para:
   - Top 10 operadoras com maiores despesas em 2024
   - Comparativo de despesas do último trimestre (2024 vs 2023)

### Scripts:
Os scripts SQL utilizados estão reunidos no arquivo:
```
atividade3/consultas_postgresql.sql
```

---

## 🌐 Atividade 4 — API com Flask + Frontend Vue.js

### Objetivo:
Desenvolver uma interface web para consulta textual no cadastro de operadoras ANS.

### Backend (Flask):

1. Executar a API:
   ```bash
   cd backend
   pip install flask pandas flask-cors
   python main.py
   ```
2. Endpoint:
   ```
   GET http://localhost:5000/buscar-operadoras?query=unimed
   ```

### Frontend (Vue.js):

1. Criar projeto Vue (caso ainda não tenha):
   ```bash
   vue create frontend
   cd frontend
   npm install axios
   npm run serve
   ```

2. Acesse a interface em:
   ```
   http://localhost:8080/
   ```

3. Permite buscar por nome, CNPJ, ou registro ANS e ver os resultados em tela.

---

## 📬 Postman

Uma coleção com requisições GET foi criada e exportada como:

```
postman/TesteANS_JoaoVictor.postman_collection.json
```

Ela demonstra o uso da API de busca com diferentes termos.

---

## ✍️ Autor

**João Victor Tavares Esteves**  
Engenharia de Computação – Universidade Federal do Ceará  
Contato: [www.linkedin.com/in/joaovtesteves](https://www.linkedin.com/in/joaovtesteves)
