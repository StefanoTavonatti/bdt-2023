import json
from typing import Optional

import redis

from lab6.cache.common import BasicStationCache
from lab6.data_model.station import Station


class RedisCache(BasicStationCache):

    def __init__(self, host: str, port: int, db: int):
        self._conn = redis.Redis(host=host, port=port, db=db)

    def get(self, station_id: str) -> Optional[Station]:
        raw_object = self._conn.get(f"station:{station_id}")
        if raw_object is None:
            return None
        else:
            station = Station.from_repr(json.loads(raw_object))
            return station


    def put(self, station: Station, ex: Optional[int] = None):
        self._conn.set(f"station:{station.station_id}", json.dumps(station.to_repr()), ex=ex)