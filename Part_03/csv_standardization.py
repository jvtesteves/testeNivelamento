import os
import pandas as pd

arquivos = [
    r"C:/Users/joaov/Downloads/arqs/2023/1T2023/1T2023.csv",
    r"C:/Users/joaov/Downloads/arqs/2023/2T2023/2T2023.csv",
    r"C:/Users/joaov/Downloads/arqs/2023/3T2023/3T2023.csv",
    r"C:/Users/joaov/Downloads/arqs/2023/4T2023/4T2023.csv",  # <- esse tem dia/mês/ano
    r"C:/Users/joaov/Downloads/arqs/2024/1T2024/1T2024.csv",
    r"C:/Users/joaov/Downloads/arqs/2024/2T2024/2T2024.csv",
    r"C:/Users/joaov/Downloads/arqs/2024/3T2024/3T2024.csv",
    r"C:/Users/joaov/Downloads/arqs/2024/4T2024/4T2024.csv",
    r"C:/Users/joaov/Downloads/arqs/Relatorio_cadop.csv"
]

pasta_destino = r"C:/temp/padronizados"
os.makedirs(pasta_destino, exist_ok=True)

def padronizar_demonstrativos(df: pd.DataFrame, dayfirst_flag=False) -> pd.DataFrame:
    """
    Ajusta o DataFrame referente aos demonstrativos contábeis
    para que as colunas fiquem padronizadas:
    DATA;REG_ANS;CD_CONTA_CONTABIL;DESCRICAO;VL_SALDO_INICIAL;VL_SALDO_FINAL
    """
    colunas_atuais = list(df.columns)
    colunas_esperadas = [
        "DATA", "REG_ANS", "CD_CONTA_CONTABIL", "DESCRICAO",
        "VL_SALDO_INICIAL", "VL_SALDO_FINAL"
    ]

    # Renomear colunas
    mapeamento = dict(zip(colunas_atuais, colunas_esperadas))
    df.rename(columns=mapeamento, inplace=True)

    # Padronizar datas
    if "DATA" in df.columns:
        df["DATA"] = pd.to_datetime(
            df["DATA"],
            errors="coerce",
            dayfirst=dayfirst_flag  # ajusta com base no parâmetro
        )
        df["DATA"] = df["DATA"].dt.strftime("%Y-%m-%d")  # converte para YYYY-MM-DD

    # Tratar colunas numéricas
    numeric_cols = ["REG_ANS", "VL_SALDO_INICIAL", "VL_SALDO_FINAL"]
    for col in numeric_cols:
        if col in df.columns:
            # Remove possíveis caracteres
            df[col] = (df[col]
                       .str.replace(r'R\$', '', regex=True)
                       .str.replace(r'\s+', '', regex=True)
                       .str.replace('.', '', regex=False)
                       .str.replace(',', '.', regex=False)
                       )
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove linhas totalmente vazias
    df.dropna(how="all", inplace=True)

    return df

def padronizar_operadoras(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ajusta o DataFrame referente aos dados cadastrais das operadoras
    para que as colunas fiquem padronizadas.
    """
    colunas_atuais = list(df.columns)
    colunas_esperadas = [
        "Registro_ANS", "CNPJ", "Razao_Social", "Nome_Fantasia", "Modalidade",
        "Logradouro", "Numero", "Complemento", "Bairro", "Cidade", "UF",
        "CEP", "DDD", "Telefone", "Fax", "Endereco_eletronico",
        "Representante", "Cargo_Representante", "Regiao_de_Comercializacao", "Data_Registro_ANS"
    ]
    mapeamento = dict(zip(colunas_atuais, colunas_esperadas))
    df.rename(columns=mapeamento, inplace=True)

    if "Data_Registro_ANS" in df.columns:
        df["Data_Registro_ANS"] = pd.to_datetime(
            df["Data_Registro_ANS"],
            errors="coerce",
            dayfirst=False  # ou True, dependendo do formato de data do seu CSV de operadoras
        )
        df["Data_Registro_ANS"] = df["Data_Registro_ANS"].dt.strftime("%Y-%m-%d")

    return df

for caminho in arquivos:
    nome_arquivo = os.path.basename(caminho)
    nome_arquivo_sem_extensao, ext = os.path.splitext(nome_arquivo)

    # Nome do CSV padronizado de saída
    novo_nome = f"{nome_arquivo_sem_extensao}_pad.csv"
    caminho_saida = os.path.join(pasta_destino, novo_nome)

    print(f"Processando {caminho} -> {caminho_saida}")

    # Ler CSV (tudo como texto inicial)
    df = pd.read_csv(caminho, sep=";", encoding="utf-8", dtype=str)

    # Verifica se é demonstrativo ou operadoras
    primeiras_colunas = [c.upper() for c in df.columns[:3]]

    if any(x in primeiras_colunas for x in ["DATA", "REG_ANS", "CD_CONTA_CONTABIL"]):
        # É demonstrativo contábil
        # Se for o 4T2023, definimos dayfirst=True
        if "4T2023" in nome_arquivo_sem_extensao:
            df = padronizar_demonstrativos(df, dayfirst_flag=True)
        else:
            df = padronizar_demonstrativos(df, dayfirst_flag=False)
    else:
        # É cadastro de operadoras
        df = padronizar_operadoras(df)

    df.to_csv(caminho_saida, sep=";", index=False, encoding="utf-8")

print("Processo de padronização finalizado!")
