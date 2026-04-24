import json

import pandas as pd
from factcheckexplorer.factcheckexplorer import FactCheckLib

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

df = df.map(lambda x: x.upper() if isinstance(x, str) else x)

wrong_values = ["ENGANOSO", "INSUSTENTÁVEL", "DISTORCIDO",
                "NÃO_É_BEM_ASSIM", "INCONCLUSIVO", "FORA DE CONTEXTO", "ERRADO", "FAKE", "FALSO", "SEM CONTEXTO", ]

correct_values = ["COMPROVADO", "CONTEXTUALIZANDO"]

df.loc[df["Verdict"].str.contains(
    "|".join(wrong_values), na=False), "Verdict"] = "FALSO"
df.loc[df["Verdict"].str.contains(
    "|".join(correct_values), na=False), "Verdict"] = "VERDADEIRO"

df.to_csv("output_pipe.csv", sep="|", index=False, encoding="utf-8")
