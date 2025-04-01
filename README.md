# Teste de Nivelamento - João Victor Tavares Esteves

Este repositório contém a implementação das quatro atividades propostas no Teste de Nivelamento, utilizando dados públicos da ANS (Agência Nacional de Saúde Suplementar). O projeto cobre desde coleta e transformação de dados até visualização web por meio de API e frontend Vue.js.

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
- PyCharm / VSCode

---

## 📂 Estrutura do Projeto

```
testeNivelamento/
├── Part_01/           # Download automático dos anexos ANS
│   ├── web_scrapping.py
│   ├── anexos/
│   │   ├── AnexoI.pdf
│   │   └── AnexoII.pdf
│   └── anexos.zip
│
├── Part_02/           # Extração do Anexo I PDF → CSV + ZIP
│   ├── data_transformation.py
│   ├── rol_de_procedimentos.csv
│   └── Teste_JoaoVictorTavaresEsteves.zip
│
├── Part_03/           # Banco de dados PostgreSQL (via pgAdmin)
│   ├── csv_standardization.py
│   ├── csvreader.py
│   ├── queries_parte_3.sql
│   └── outputs/
│       ├── output_atv_3_a.csv
│       └── output_atv_3_b.csv
│
├── Part_04/           # Backend Flask + Frontend Vue.js
│   ├── backend/
│   │   ├── main.py
│   │   └── Relatorio_cadop.csv
│   └── frontend/
│       ├── src/
│       │   └── App.vue (customizado)
│       └── ...
│
└── README.md
```

---

## 📌 Atividade 1 — Download dos Anexos da ANS

### Objetivo:
Automatizar o download dos Anexos I e II disponibilizados pela ANS e armazená-los de forma organizada.

📄 Arquivo principal:  
`Part_01/web_scrapping.py`

### O que faz:
- Baixa os PDFs dos Anexos I e II
- Salva os arquivos em `Part_01/anexos/`
- Compacta a pasta inteira no arquivo `anexos.zip`

### Como executar:
```bash
cd Part_01
pip install requests
python web_scrapping.py
```

---

## 🧾 Atividade 2 — Processamento de dados PDF

### Objetivo:
Extrair a tabela principal do Anexo I (PDF) e transformá-la em um arquivo CSV, posteriormente compactado.

📄 Arquivo principal:  
`Part_02/data_transformation.py`

### Como executar:
```bash
cd Part_02
pip install pdfplumber pandas
python data_transformation.py
```

### Resultado:
- `rol_de_procedimentos.csv`
- `Teste_JoaoVictorTavaresEsteves.zip`

---

## 🐘 Atividade 3 — Análise com PostgreSQL (pgAdmin)

### Objetivo:
Padronizar e analisar dados contábeis e cadastrais das operadoras da ANS.

📁 Local: `Part_03`

### Componentes:
- `csv_standardization.py` → padroniza arquivos da ANS
- `csvreader.py` → exibe amostras dos arquivos padronizados
- `queries_parte_3.sql` → consultas SQL para análise no pgAdmin
- `outputs/` → contém os resultados salvos em CSV das queries

---

## 🌐 Atividade 4 — Consulta interativa com Flask + Vue.js

### Objetivo:
Desenvolver uma API Flask para busca textual em dados de operadoras ANS, e um frontend Vue.js para interação.

---

### 🖥️ Backend (Flask)

📁 Local: `Part_04/backend`

📄 Arquivo principal: `main.py`  
📄 Dados utilizados: `Relatorio_cadop.csv`

### Como executar:
```bash
cd Part_04/backend
pip install flask flask-cors pandas
python main.py
```

- API rodando em: `http://localhost:5000`
- Endpoint de busca:  
  ```
  GET /buscar-operadoras?query=unimed
  ```

---

### 🌍 Frontend (Vue.js)

📁 Local: `Part_04/frontend`

### Como iniciar:
```bash
cd Part_04/frontend
npm install
npm run serve
```

- Acesse: [http://localhost:8080](http://localhost:8080)
- Interface com:
  - Campo de busca por nome, CNPJ ou registro ANS
  - Lista dos 10 primeiros resultados (Nome Fantasia, Razão Social, UF, etc)

---

## 📬 Postman

Uma coleção com testes GET pode ser utilizada para validar a API Flask (buscas com diferentes termos).
Teste ANS João Victor Tavares Esteves.postman_collection.json

---

## ✍️ Autor

**João Victor Tavares Esteves**  
Engenharia de Computação – Universidade Federal do Ceará  
📎 [www.linkedin.com/in/joaovtesteves](https://www.linkedin.com/in/joaovtesteves)
