from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Permite requisições vindas do frontend

# Carregar o CSV ao iniciar o servidor
operadoras_df = pd.read_csv("Relatorio_cadop.csv", sep=";", encoding="utf-8")

@app.route("/buscar-operadoras", methods=["GET"])
def buscar_operadoras():
    query = request.args.get("query", "").lower()

    if not query:
        return jsonify({"erro": "Parâmetro 'query' não fornecido."}), 400

    # Realizar uma busca textual usando os nomes corretos das colunas
    resultados = operadoras_df[
        operadoras_df["Nome_Fantasia"].str.lower().str.contains(query, na=False) |
        operadoras_df["Razao_Social"].str.lower().str.contains(query, na=False) |
        operadoras_df["CNPJ"].astype(str).str.contains(query, na=False) |
        operadoras_df["Registro_ANS"].astype(str).str.contains(query, na=False)
        ]

    # Converter resultado para JSON (limitando para 10 resultados)
    resultados_json = resultados.head(10).fillna("").astype(str).to_dict(orient="records")

    return jsonify(resultados_json)

if __name__ == "__main__":
    app.run(debug=True)
