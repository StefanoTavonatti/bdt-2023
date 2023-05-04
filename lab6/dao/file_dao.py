import json
import os
from typing import List

from lab6.dao.common import BasicDao
from lab6.data_model.station import Station


class FileDao(BasicDao):

    def update_station(self, station: Station) -> None:
        pass

    def get_station(self, station_id: int) -> Station:
        pass

    def get_station_by_name(self, name: str) -> List[Station]:
        pass

    def __init__(self, db_file: str):
        self._db_file = db_file

    def save_station(self, station: Station) -> None:

        stored_data = []

        # check if file self._db_file exists
        if os.path.isfile(self._db_file):
            with open(self._db_file, "r") as fin:
                raw_data = json.load(fin)
                stored_data = [Station.from_repr(x) for x in raw_data]

        stored_data.append(station)

        with open(self._db_file, "w") as f:
            data_write = [x.to_repr() for x in stored_data]
            f.write(json.dumps(data_write))