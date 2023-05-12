from typing import List

from lab6.cache.common import BasicStationCache
from lab6.connectors.common import BasicConnector
from lab6.connectors.dati_bolzano import DatiBolzanoConnector
from lab6.connectors.dati_trentino import DatiTrentinoConnector
from lab6.dao.common import BasicDao, NotExist
from lab6.data_model.station import Station, Measure


class AirQualityManager:

    def __init__(self, bolzano_connector: DatiBolzanoConnector, trento_connector: DatiTrentinoConnector, dao: BasicDao, cache: BasicStationCache):
        self._bolzano_connector = bolzano_connector
        self._trento_connector = trento_connector
        self._dao = dao
        self._cache = cache

    def _download_latest_data(self, connector: BasicConnector) -> List[Station]:
        return connector.get_latest_air_quality_data()

    def _store_stations(self, stations: List[Station]):
        for station in stations:
            try:
                stored_station = self._dao.get_station(station.station_id)
                self._dao.update_station(station)
            except NotExist:
                self._dao.save_station(station)

            self._store_measures(station)
            self._cache.put(station)

    def _store_measures(self, station: Station):
        for measure in station.measurement:
            self._dao.save_measure(station.station_id, measure)

    def start_computation(self):
        trento_data = self._download_latest_data(self._trento_connector)
        self._store_stations(trento_data)
