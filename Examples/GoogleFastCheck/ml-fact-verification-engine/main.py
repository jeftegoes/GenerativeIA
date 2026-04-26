import logging
import os
from typing import Tuple

import pandas as pd
import psycopg2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

QUERY = "SELECT id, error_rate, publisher, rating, text FROM trained_claim_reviews"

def get_db_connection():
    print("Estabelecendo conexão com o banco de dados PostgreSQL.")
    return psycopg2.connect(
        host="localhost",
        database="fact-checker-db",
        user="postgres",
        password="Master@123",
        port="5432"
    )


def load_training_data() -> pd.DataFrame:
    logger.info("Conectando ao PostgreSQL e carregando dados...")
    with get_db_connection() as conn:
        df = pd.read_sql(QUERY, conn)

    if df.empty:
        raise ValueError("Nenhum dado retornado da tabela trained_claim_reviews.")

    df = df.dropna(subset=["text", "rating"])
    if df.empty:
        raise ValueError("Não há registros válidos com texto e rating.")

    return df


def prepare_dataset(df: pd.DataFrame) -> Tuple[pd.Series, pd.Series, LabelEncoder]:
    logger.info("Preparando dataset para treinamento...")
    texts = df["text"].astype(str)
    labels = df["rating"].astype(str)

    encoder = LabelEncoder()
    encoded_labels = encoder.fit_transform(labels)

    logger.info("Classes detectadas: %s", list(encoder.classes_))
    return texts, encoded_labels, encoder


def train_text_model(texts: pd.Series, labels: pd.Series) -> Pipeline:
    logger.info("Treinando modelo de classificação de texto...")
    pipeline = Pipeline(
        [
            (
                "tfidf",
                TfidfVectorizer(
                    max_features=20000,
                    ngram_range=(1, 2),
                    stop_words="english",
                ),
            ),
            ("clf", LogisticRegression(max_iter=1000, solver="liblinear")),
        ]
    )

    pipeline.fit(texts, labels)
    return pipeline


def evaluate_model(model: Pipeline, texts: pd.Series, labels: pd.Series, encoder: LabelEncoder) -> None:
    logger.info("Avaliando desempenho do modelo...")
    predictions = model.predict(texts)
    accuracy = accuracy_score(labels, predictions)
    logger.info("Acurácia: %.4f", accuracy)
    report = classification_report(labels, predictions, target_names=encoder.classes_, zero_division=0)
    logger.info("Relatório de classificação:\n%s", report)


def predict_rating(model: Pipeline, encoder: LabelEncoder, text: str) -> str:
    if not text or not text.strip():
        raise ValueError("Texto de entrada vazio.")

    label_idx = model.predict([text])[0]
    return encoder.inverse_transform([label_idx])[0]


def ask_user_and_predict(model: Pipeline, encoder: LabelEncoder) -> None:
    print("\nDigite um texto de notícia / fato e pressione Enter para receber o veredito previsto.")
    print("Digite 'sair' para encerrar.")
    while True:
        entry = input("Texto> ").strip()
        if entry.lower() in {"sair", "exit", "quit"}:
            print("Encerrando.")
            break
        if not entry:
            print("Por favor insira um texto válido.")
            continue

        try:
            predicted = predict_rating(model, encoder, entry)
            print(f"Veredito previsto: {predicted}\n")
        except Exception as exc:
            logger.error("Erro ao prever: %s", exc)
            print("Não foi possível prever o veredito. Verifique o texto e tente novamente.")


def main() -> None:
    df = load_training_data()
    texts, labels, encoder = prepare_dataset(df)

    # TfidfVectorizer + LogisticRegression
    x_train, x_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.2, random_state=42, stratify=labels
    )

    model = train_text_model(x_train, y_train)
    evaluate_model(model, x_test, y_test, encoder)

    ask_user_and_predict(model, encoder)


if __name__ == "__main__":
    main()
