from factcheckexplorer.factcheckexplorer import FactCheckLib

fact_check = FactCheckLib(
    query="eleições",
    language="pt",
    num_results=200
)

fact_check.process()
