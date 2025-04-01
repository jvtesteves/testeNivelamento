import os
import zipfile
import pdfplumber
import pandas as pd


def extrair_tabela_pdfplumber(pdf_path, csv_output, zip_output):
    """
    Extrai tabelas do PDF do Anexo I, transforma em CSV e compacta em ZIP.
    Etapas:
    1. Abre o PDF e extrai as tabelas com pdfplumber.
    2. Concatena os dados de todas as páginas (eliminando cabeçalhos repetidos).
    3. Substitui abreviações "OD" e "AMB" por descrições completas (se aplicável).
    4. Salva como CSV.
    5. Compacta o CSV em um arquivo ZIP.
    """

    all_rows = []
    first_header = None

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            table = page.extract_table()

            if table:
                if i == 0:
                    all_rows.extend(table)
                    first_header = table[0]
                else:
                    current_header = table[0]
                    if current_header == first_header:
                        all_rows.extend(table[1:])
                    else:
                        all_rows.extend(table)

    if not all_rows:
        print("Nenhuma tabela foi extraída. Verifique a formatação do PDF.")
        return

    # Cria o DataFrame e aplica substituições (caso existam essas colunas)
    df = pd.DataFrame(all_rows[1:], columns=all_rows[0])

    if "OD" in df.columns:
        df["OD"] = df["OD"].replace("OD", "Seg. Odontológica")
    if "AMB" in df.columns:
        df["AMB"] = df["AMB"].replace("AMB", "Seg. Ambulatorial")

    # Salva o CSV
    df.to_csv(csv_output, index=False, encoding="utf-8")
    print(f"CSV gerado: {csv_output}")

    # Compacta o CSV
    with zipfile.ZipFile(zip_output, "w") as zipf:
        zipf.write(csv_output, arcname=os.path.basename(csv_output))

    print(f"ZIP gerado: {zip_output}")


if __name__ == "__main__":
    # Caminhos relativos à raiz do projeto
    pdf_file = "../Part_01/anexos/AnexoI.pdf"
    csv_output = "rol_de_procedimentos.csv"
    zip_output = "Teste_JoaoVictorTavaresEsteves.zip"

    extrair_tabela_pdfplumber(pdf_file, csv_output, zip_output)
