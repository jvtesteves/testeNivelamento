import pdfplumber
import pandas as pd
import zipfile
import os

def extrair_tabela_pdfplumber(pdf_path, csv_output, zip_output):
    """
    1) Abre o PDF e extrai a 'tabela' de cada página usando pdfplumber
    2) Concatena todas as linhas num único DataFrame
    3) Faz a substituição das abreviações 'OD' e 'AMB' para descrições completas
    4) Salva como CSV
    5) Compacta o CSV num zip
    """
    all_rows = [] # Para “empilhar” todas as linhas extraídas das tabelas de cada página.
    first_header = None  # Para comparar cabeçalho duplicado nas páginas
    # Assim só considera o cabeçalho da primeira página

    with pdfplumber.open(pdf_path) as pdf:
        for page_index, page in enumerate(pdf.pages):
            # Tenta extrair a tabela da página (retorna lista de listas ou None)
            table = page.extract_table()

            if table:
                # Se for a primeira página, pegamos tudo
                if page_index == 0:
                    all_rows.extend(table)
                    first_header = table[0]  # Salva o cabeçalho da primeira linha
                else:
                    # Verifica se o cabeçalho desta página é o mesmo da primeira
                    current_header = table[0]
                    if current_header == first_header:
                        # Significa que a primeira linha é repetição do cabeçalho
                        all_rows.extend(table[1:])
                    else:
                        all_rows.extend(table)

    # Se nada foi extraído, avisamos e encerramos
    if not all_rows:
        print("Nenhuma tabela foi extraída. Verifique a formatação do PDF.")
        return

    # Converte a lista de listas em um DataFrame pandas
    df = pd.DataFrame(all_rows[1:], columns=all_rows[0])  # a primeira linha de all_rows é cabeçalho

    # Exemplo de substituição de "OD" e "AMB" em colunas específicas.
    # Se "OD" e "AMB" aparecerem em várias colunas, pode ser necessário um approach diferente (ex: replace no DataFrame inteiro).
    if "OD" in df.columns:
        df["OD"] = df["OD"].replace("OD", "Seg. Odontológica")
    if "AMB" in df.columns:
        df["AMB"] = df["AMB"].replace("AMB", "Seg. Ambulatorial")

    # Salva em CSV
    df.to_csv(csv_output, index=False, encoding="utf-8")
    print(f"CSV gerado: {csv_output}")

    # Compacta num arquivo ZIP
    with zipfile.ZipFile(zip_output, "w") as zipf:
        zipf.write(csv_output, arcname=os.path.basename(csv_output))

    print(f"ZIP gerado: {zip_output}")

if __name__ == "__main__":
    pdf_file = "../Part01/anexos/AnexoI.pdf"  # Caminho do nosso Anexo1
    csv_name = "rol_de_procedimentos.csv"
    zip_name = "Teste_JoaoVictorTavaresEsteves.zip"

    extrair_tabela_pdfplumber(pdf_file, csv_name, zip_name)
