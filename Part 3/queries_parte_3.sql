-- ======================================================
-- 1) CRIAÇÃO DAS TABELAS
-- ======================================================
CREATE TABLE operadoras_ativas (
                                   registro_ans             VARCHAR(6) PRIMARY KEY,
                                   cnpj                     VARCHAR(14),
                                   razao_social             VARCHAR(140),
                                   nome_fantasia            VARCHAR(140),
                                   modalidade               VARCHAR(50),
                                   logradouro               VARCHAR(40),
                                   numero                   VARCHAR(20),
                                   complemento              VARCHAR(40),
                                   bairro                   VARCHAR(30),
                                   cidade                   VARCHAR(30),
                                   uf                       VARCHAR(2),
                                   cep                      VARCHAR(8),
                                   ddd                      VARCHAR(4),
                                   telefone                 VARCHAR(20),
                                   fax                      VARCHAR(20),
                                   endereco_eletronico      VARCHAR(255),
                                   representante            VARCHAR(50),
                                   cargo_representante      VARCHAR(40),
                                   regiao_de_comercializacao SMALLINT,
                                   data_registro_ans        DATE
);

CREATE TABLE demonstracoes_contabeis (
                                         data               DATE,
                                         reg_ans            INTEGER,
                                         cd_conta_contabil  VARCHAR(9),
                                         descricao          VARCHAR(150),
                                         vl_saldo_inicial   NUMERIC,
                                         vl_saldo_final     NUMERIC
);

-- ======================================================
-- 2) IMPORTAÇÃO DE DADOS (COPY)
--    Ajuste os caminhos conforme a localização real dos arquivos
-- ======================================================

COPY demonstracoes_contabeis
    FROM 'C:/temp/padronizados/4T2024_pad.csv'
    WITH (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'UTF8');

COPY demonstracoes_contabeis
    FROM 'C:/temp/padronizados/3T2024_pad.csv'
    WITH (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'UTF8');

COPY demonstracoes_contabeis
    FROM 'C:/temp/padronizados/2T2024_pad.csv'
    WITH (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'UTF8');

COPY demonstracoes_contabeis
    FROM 'C:/temp/padronizados/1T2024_pad.csv'
    WITH (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'UTF8');

COPY demonstracoes_contabeis
    FROM 'C:/temp/padronizados/4T2023_pad.csv'
    WITH (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'UTF8');

COPY demonstracoes_contabeis
    FROM 'C:/temp/padronizados/3T2023_pad.csv'
    WITH (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'UTF8');

COPY demonstracoes_contabeis
    FROM 'C:/temp/padronizados/2T2023_pad.csv'
    WITH (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'UTF8');

COPY demonstracoes_contabeis
    FROM 'C:/temp/padronizados/1T2023_pad.csv'
    WITH (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'UTF8');

COPY operadoras_ativas
    FROM 'C:/temp/padronizados/Relatorio_cadop_pad.csv'
    WITH (FORMAT csv, DELIMITER ';', HEADER, ENCODING 'UTF8');

-- ======================================================
-- 3) QUERIES ANALÍTICAS
-- ======================================================

-- Query 1: Encontrar as 10 operadoras com maiores despesas no último trimestre.
-- Neste exemplo, consideramos registros com data '2024-10-01' ou '2023-10-01' como pertencentes ao último trimestre.
WITH ult_trimestre AS (
    -- Seleciona os registros da tabela "demonstracoes_contabeis" com as datas indicadas,
    -- e filtra somente aqueles cuja descrição contenha o texto especificado.
    SELECT *
    FROM demonstracoes_contabeis
    WHERE data IN ('2024-10-01', '2023-10-01')
      AND descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    )
SELECT
    -- Seleciona o nome fantasia da operadora
    op.nome_fantasia,
    -- Calcula a despesa total do trimestre, somando a diferença entre o saldo inicial e final de cada registro
    SUM(dc.vl_saldo_inicial - dc.vl_saldo_final) AS despesa_trimestre
FROM ult_trimestre dc
         JOIN operadoras_ativas op
    -- Realiza a junção entre os registros do último trimestre e os dados cadastrais,
    -- fazendo o mesmo ajuste para garantir a correspondência dos códigos de operadora.
              ON op.registro_ans = LPAD(dc.reg_ans::text, 6, '0')
GROUP BY op.nome_fantasia
ORDER BY despesa_trimestre DESC  -- Ordena as operadoras da maior para a menor despesa do trimestre
    LIMIT 10;  -- Retorna somente as 10 operadoras com maiores despesas no último trimestre


-- Query 2: Encontrar as 10 operadoras com maiores despesas durante o ano de 2024.
-- Aqui, a despesa é calculada subtraindo o valor do saldo final do saldo inicial.
-- Somente são considerados os registros que possuem a descrição:
-- "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR".
WITH dados_2024 AS (
    -- Seleciona todos os registros da tabela "demonstracoes_contabeis" referentes ao ano de 2024
    -- e que contenham na descrição o texto especificado (usando ILIKE para ignorar maiúsculas/minúsculas).
    SELECT *
    FROM demonstracoes_contabeis
    WHERE DATE_PART('year', data) = 2024
      AND descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    )
SELECT
    -- Seleciona o nome fantasia da operadora
    op.nome_fantasia,
    -- Calcula a despesa total do ano, somando a diferença entre o saldo inicial e o final de cada registro
    SUM(dc.vl_saldo_inicial - dc.vl_saldo_final) AS despesa_ano
FROM dados_2024 dc
         JOIN operadoras_ativas op
    -- Realiza a junção entre os registros contábeis (dc) e os dados cadastrais das operadoras (op)
    -- O campo "registro_ans" de operadoras_ativas é comparado com "reg_ans" dos registros,
    -- garantindo que ambos tenham 6 dígitos com a função LPAD.
              ON op.registro_ans = LPAD(dc.reg_ans::text, 6, '0')
GROUP BY op.nome_fantasia
ORDER BY despesa_ano DESC  -- Ordena as operadoras da maior para a menor despesa
    LIMIT 10;  -- Retorna somente as 10 operadoras com maiores despesas