import os

def mostrar_cinco_primeiras_linhas(caminho_csv):
    """
    Lê e imprime as 5 primeiras linhas de um arquivo CSV.
    """
    print(f"\n===== Lendo arquivo: {caminho_csv} =====")
    try:
        with open(caminho_csv, "r", encoding="utf-8") as f:
            for i in range(5):
                linha = f.readline()
                if not linha:  # se chegar ao fim do arquivo antes das 5 linhas
                    break
                print(linha.strip())
    except Exception as e:
        print(f"Erro ao ler {caminho_csv}: {e}")

def main():
    # Se os arquivos estiverem em um diretório específico, você pode definir aqui:
    # Por exemplo, pasta 'demonstracoes_contabeis'
    pasta = "demonstracoes_contabeis"

    # Lista dos arquivos a serem lidos (exemplo)
    arquivos = [
        r"C:\temp\padronizados\1T2023_pad.csv",
        r"C:\temp\padronizados\1T2024_pad.csv",
        r"C:\temp\padronizados\2T2023_pad.csv",
        r"C:\temp\padronizados\2T2024_pad.csv",
        r"C:\temp\padronizados\3T2023_pad.csv",
        r"C:\temp\padronizados\3T2024_pad.csv",
        r"C:\temp\padronizados\4T2023_pad.csv",
        r"C:\temp\padronizados\4T2024_pad.csv",
        r"C:\temp\padronizados\Relatorio_cadop_pad.csv"
    ]

    # Percorre cada arquivo, exibe as 5 primeiras linhas
    for nome_arquivo in arquivos:
        caminho_completo = os.path.join(pasta, nome_arquivo)
        mostrar_cinco_primeiras_linhas(caminho_completo)

if __name__ == "__main__":
    main()
