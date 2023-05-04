from datetime import datetime

from lab6.connectors.dati_trentino import DatiTrentinoConnector
from lab6.connectors.dati_bolzano import DatiBolzanoConnector
from lab6.dao.common import NotExist
from lab6.dao.file_dao import FileDao
from lab6.dao.sqlite_dao import SQLiteDao

connector = DatiTrentinoConnector()

# dao = FileDao("my_db")
#
# data = connector.get_air_quality_data()
#
# print(data[0])
# print(data[0].measurement)
#
connector=DatiBolzanoConnector()
from_date=datetime(2023, 4, 20)
to_date=datetime(2023, 4, 21)
data = connector.get_air_quality_data(from_date, to_date)
dao = SQLiteDao("lab6.db")
# print(len(data))
for station in data:
    try:
        stored_station = dao.get_station(station.station_id)
        dao.update_station(station)
    except NotExist:
        dao.save_station(station)

    for measure in station.measurement:
        dao.save_measure(station.station_id, measure)

# stations = dao.get_station_by_name("Parco S. Chiara")
stations = dao.get_station("trento-Parco S. Chiara")
print(stations)