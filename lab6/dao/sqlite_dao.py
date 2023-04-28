import sqlite3
from typing import List

from lab6.dao.common import BasicDao
from lab6.data_model.station import Station


class SQLiteDao(BasicDao):

    def update_station(self, station: Station) -> None:
        pass

    def get_station(self, station_id: int) -> Station:
        pass

    def get_station_by_name(self, name: str) -> List[Station]:
        pass

    def __init__(self, connection_string: str):
        self._connection_string = connection_string
        self._conn = sqlite3.connect(self._connection_string)

    def save_station(self, station: Station) -> None:
        with self._conn:
            self._conn.execute("INSERT INTO station(name, city, address)"
                               "VALUES(?, ?, ?)", (station.name, station.city, station.address))
