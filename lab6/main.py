from lab6.connectors.dati_trentino import DatiTrentinoConnector

connector = DatiTrentinoConnector()

data = connector.get_air_quality_data()

print(data[0])
print(data[0].measurement)
