import requests
import os
import zipfile

def baixar_e_zipar_anexos():
    """
    Faz o download dos Anexos I e II em PDF e gera um arquivo ZIP com ambos.
    """
    # Links diretos dos PDFs
    # Criação das variáveis para facilitar acesso dos links
    anexo1_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    anexo2_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"

    # Pastas e nomes de arquivo
    pasta_anexos = "anexos"
    os.makedirs(pasta_anexos, exist_ok=True)  # Cria a pasta se não existir

    anexo1_path = os.path.join(pasta_anexos, "AnexoI.pdf")
    anexo2_path = os.path.join(pasta_anexos, "AnexoII.pdf")

    # Baixa e salva o Anexo I
    print("Baixando Anexo I...")
    resp1 = requests.get(anexo1_url)
    if resp1.status_code == 200:
        with open(anexo1_path, "wb") as f:
            f.write(resp1.content)
        print(f"Anexo I salvo em: {anexo1_path}")
    else:
        print(f"Falha ao baixar Anexo I. Status code: {resp1.status_code}")
        return  # Encerra se não conseguir baixar

    # Baixa e salva o Anexo II
    print("Baixando Anexo II...")
    resp2 = requests.get(anexo2_url)
    if resp2.status_code == 200:
        with open(anexo2_path, "wb") as f: #salvar PDFs sem corromper o arquivo
            f.write(resp2.content)
        print(f"Anexo II salvo em: {anexo2_path}")
    else:
        print(f"Falha ao baixar Anexo II. Status code: {resp2.status_code}")
        return  # Encerra se não conseguir baixar

    # Compactar os PDFs em um arquivo ZIP
    zip_filename = "Anexos.zip"
    print(f"Gerando arquivo ZIP: {zip_filename}...")

    with zipfile.ZipFile(zip_filename, "w") as zipf:
        zipf.write(anexo1_path, arcname="AnexoI.pdf")
        zipf.write(anexo2_path, arcname="AnexoII.pdf")

    print(f"Concluído! Arquivo ZIP gerado: {zip_filename}")


if __name__ == "__main__":
    baixar_e_zipar_anexos()
