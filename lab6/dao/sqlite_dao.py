import sqlite3
from typing import List

from lab6.dao.common import BasicDao, NotExist
from lab6.data_model.station import Station, Measure


class SQLiteDao(BasicDao):

    def __init__(self, connection_string: str):
        self._connection_string = connection_string
        self._conn = sqlite3.connect(self._connection_string)

    def update_station(self, station: Station) -> None:
        stored_station = self.get_station(station.station_id)
        if stored_station is None:
            raise NotExist

        with self._conn:
            self._conn.execute("UPDATE station SET name = ?, address = ?, city = ? WHERE ID = ?",
                               (station.name, station.address, station.city, station.station_id))

    def get_station(self, station_id: str) -> Station:
        with self._conn:
            cursor = self._conn.cursor()
            cursor.execute("SELECT ID, name, address, city FROM station WHERE ID = ?", (station_id,))
            row = cursor.fetchone()

            if row is None:
                raise NotExist

            return Station(row[0], row[1], row[2], row[3], [])

    def get_station_by_name(self, name: str) -> List[Station]:
        result = []
        with self._conn:
            cursor = self._conn.cursor()
            cursor.execute("SELECT ID, name, address, city FROM station WHERE name = ?", (name,))
            for station_id, name, address, city in cursor:
                result.append(Station(station_id, name, address, city, []))
        return result

    def save_station(self, station: Station) -> None:
        with self._conn:
            self._conn.execute("INSERT INTO station(ID, name, city, address)"
                               "VALUES(?, ?, ?, ?)", (station.station_id, station.name, station.city, station.address))

    def save_measure(self, station_id:str, measure: Measure) -> None:
        with self._conn:
            self._conn.execute("INSERT INTO measure(pm25, no2, o3, so2, pm10, dt, station_id)"
                               "VALUES(?, ?, ?, ?, ?, ?, ?)", (measure.pm25_value, measure.no2_value, measure.o3_value,
                                                               measure.so2_value, measure.pm10_value, measure.dt, station_id))

    def get_measure(self, measure_id: str) -> Measure:
        with self._conn:
            cursor = self._conn.cursor()
            cursor.execute("SELECT pm25, no2, o3, so2, pm10, dt, station_id FROM measure WHERE ID = ?", (measure_id,))

            row = cursor.fetchone()
            if row is None:
                raise NotExist
            pm25_value, no2_value, o3_value, so2_value, pm10_value, dt, station_id = row
            return Measure(pm25_value, no2_value, o3_value, so2_value, pm10_value, dt)

    def get_measure_by_station(self, station_id: str) -> List[Measure]:
        result = []
        with self._conn:
            cursor = self._conn.cursor()
            cursor.execute("SELECT pm25, no2, o3, so2, pm10, dt, station_id FROM measure WHERE station_id = ?", (station_id,))
            for pm25_value, no2_value, o3_value, so2_value, pm10_value, dt, station_id in cursor:
                result.append(Measure(pm25_value, no2_value, o3_value, so2_value, pm10_value, dt))
        return result
