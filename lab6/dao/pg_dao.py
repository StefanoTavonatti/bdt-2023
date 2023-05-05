from typing import List

import psycopg2

from lab6.dao.common import BasicDao
from lab6.data_model.station import Measure, Station


class PgDao(BasicDao):

    def __init__(self, host: str, dbname: str, user: str, password: str):
        self._conn = psycopg2.connect(f"host={host} dbname={dbname} user={user} password={password}")

    def save_station(self, station: Station) -> None:
        with self._conn:
            with self._conn.cursor() as cur:

                params ={
                    "ID": station.station_id,
                    "name": station.name,
                    "city": station.city,
                    "address": station.address
                }

                cur.execute("""
                    INSERT INTO station(ID, name, city, address)
                    VALUES(%(ID)s, %(name)s, %(city)s, %(address)s)
                """, params)

    def update_station(self, station: Station) -> None:
        pass

    def get_station(self, station_id: str) -> Station:
        pass

    def get_station_by_name(self, name: str) -> List[Station]:
        pass

    def save_measure(self, station_id: str, measure: Measure) -> None:
        pass

    def get_measure(self, measure_id: str) -> Measure:
        pass

    def get_measure_by_station(self, station_id: str) -> List[Measure]:
        pass