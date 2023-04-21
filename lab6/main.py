from datetime import datetime

from lab6.connectors.dati_trentino import DatiTrentinoConnector
from lab6.connectors.dati_bolzano import DatiBolzanoConnector
from lab6.dao.file_dao import FileDao

connector = DatiTrentinoConnector()

dao = FileDao("my_db")

data = connector.get_air_quality_data()

print(data[0])
print(data[0].measurement)

connector=DatiBolzanoConnector()
from_date=datetime(2023, 4, 20)
to_date=datetime(2023, 4, 21)
data1= connector.get_air_quality_data(from_date,to_date)

dao.save_station(data1[0])