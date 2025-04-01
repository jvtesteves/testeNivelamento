import requests
import os
import zipfile
import shutil

def baixar_e_zipar_anexos():
    """
    Faz o download dos Anexos I e II em PDF e gera um arquivo ZIP com a pasta "anexos".
    """
    # Links diretos dos PDFs
    anexo1_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    anexo2_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"

    # Caminhos base
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Diretório atual do script
    pasta_anexos = os.path.join(base_dir, "anexos")
    zip_path = os.path.join(base_dir, "anexos.zip")

    # Cria a pasta "anexos" se não existir
    os.makedirs(pasta_anexos, exist_ok=True)

    # Caminhos dos arquivos PDF dentro da pasta "anexos"
    anexo1_path = os.path.join(pasta_anexos, "AnexoI.pdf")
    anexo2_path = os.path.join(pasta_anexos, "AnexoII.pdf")

    # Baixar Anexo I
    print("Baixando Anexo I...")
    resp1 = requests.get(anexo1_url)
    if resp1.status_code == 200:
        with open(anexo1_path, "wb") as f:
            f.write(resp1.content)
        print(f"Anexo I salvo em: {anexo1_path}")
    else:
        print(f"Falha ao baixar Anexo I. Status code: {resp1.status_code}")
        return

    # Baixar Anexo II
    print("Baixando Anexo II...")
    resp2 = requests.get(anexo2_url)
    if resp2.status_code == 200:
        with open(anexo2_path, "wb") as f:
            f.write(resp2.content)
        print(f"Anexo II salvo em: {anexo2_path}")
    else:
        print(f"Falha ao baixar Anexo II. Status code: {resp2.status_code}")
        return

    # Remove o ZIP anterior se existir
    if os.path.exists(zip_path):
        os.remove(zip_path)

    # Compactar a pasta "anexos" inteira em "anexos.zip"
    print(f"Gerando arquivo ZIP: {zip_path}...")
    shutil.make_archive(base_name=os.path.splitext(zip_path)[0], format="zip", root_dir=pasta_anexos)
    print(f"Concluído! Arquivo ZIP gerado: {zip_path}")


if __name__ == "__main__":
    baixar_e_zipar_anexos()
