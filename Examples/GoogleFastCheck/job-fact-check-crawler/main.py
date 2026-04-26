import hashlib
import json

import pandas as pd
import psycopg2
from factcheckexplorer.factcheckexplorer import FactCheckLib

wrong_values = ["ENGANOSO", "INSUSTENTÁVEL", "DISTORCIDO",
                "NÃO_É_BEM_ASSIM", "INCONCLUSIVO", "FORA DE CONTEXTO", "ERRADO", "FAKE", "FALSO", "SEM CONTEXTO", ]

correct_values = ["COMPROVADO", "CONTEXTUALIZANDO"]


def get_connection():
    print("Estabelecendo conexão com o banco de dados PostgreSQL.")
    return psycopg2.connect(
        host="localhost",
        database="fact-checker-db",
        user="postgres",
        password="Master@123",
        port="5432"
    )


def preprocess_data(df):
    print("Aplicando limpeza e padronização aos dados (UpperCase e mapeamento de Veridict).")
    df = df.map(lambda x: x.upper() if isinstance(x, str) else x)

    df.loc[df["Verdict"].str.contains(
        "|".join(wrong_values), na=False), "Verdict"] = "FALSO"
    df.loc[df["Verdict"].str.contains(
        "|".join(correct_values), na=False), "Verdict"] = "VERDADEIRO"

    return df


def insert_data(conn, df):
    print("Inserindo dados na tabela trained_claim_reviews com validação de checksum para evitar duplicidade.")
    cur = conn.cursor()
    inserted_count = 0

    try:
        for _, row in df.iterrows():
            # Gerar checksum para o texto da Claim
            claim_text = str(row['Claim'])
            checksum = hashlib.md5(claim_text.encode('utf-8')).hexdigest()

            # Verifica se o checksum já existe para evitar duplicidade
            cur.execute(
                "SELECT 1 FROM public.trained_claim_reviews WHERE checksum = %s", (checksum,))

            if cur.fetchone() is None:
                cur.execute(
                    """INSERT INTO public.trained_claim_reviews 
                       (publisher, rating, text, checksum, error_rate) 
                       VALUES (%s, %s, %s, %s, %s)""",
                    (row['Source Name'][:255], row['Verdict']
                     [:255], claim_text[:255], checksum, 0)
                )
                inserted_count += 1

        conn.commit()
        print(f"Sucesso: {inserted_count} novos registros inseridos.")
    except Exception as e:
        conn.rollback()
        print(f"Erro na inserção: {e}")
    finally:
        cur.close()


def get_fact_check_data():
    fact_check = FactCheckLib(
        query="eleições",
        language="pt",
        num_results=200
    )

    raw = fact_check.fetch_data()
    clean = fact_check.clean_json(raw)
    data = fact_check.extract_info(clean)

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    df = pd.DataFrame(data)

    df = preprocess_data(df)

    conn = None
    try:
        conn = get_connection()
        insert_data(conn, df)
        print("Processamento via API concluído.")
    except Exception as e:
        print(f"Erro no fluxo de API: {e}")
    finally:
        if conn:
            conn.close()


def get_fact_by_pgsql():
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT p.name, cr.textual_rating, c.text
            FROM claims c
            INNER JOIN claim_reviews cr ON c.id = cr.claim_id
            INNER JOIN publishers p ON p.id = cr.publisher_id
        """)
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns=['Source Name', 'Verdict', 'Claim'])
        cur.close()

        df = preprocess_data(df)
        insert_data(conn, df)
        print("Sincronização entre tabelas locais concluída.")
    except Exception as e:
        print(f"Erro ao processar dados via PostgreSQL: {e}")
    finally:
        if conn:
            conn.close()


get_fact_check_data() # dados da api fact check
get_fact_by_pgsql() # dados que o usuário pesquisou
get_fact_uol() # dados do uol
