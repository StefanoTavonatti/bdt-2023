from abc import ABC, abstractmethod
from typing import List

from lab6.data_model.station import Station, Measure


class NotExist(Exception):
    pass


class BasicDao(ABC):

    @abstractmethod
    def save_station(self, station: Station) -> None:
        pass

    @abstractmethod
    def update_station(self, station: Station) -> None:
        pass

    @abstractmethod
    def get_station(self, station_id: str) -> Station:
        pass

    @abstractmethod
    def get_station_by_name(self, name: str) -> List[Station]:
        pass

    @abstractmethod
    def save_measure(self, station_id: str, measure: Measure) -> None:
        pass

    @abstractmethod
    def get_measure(self, measure_id: str) -> Measure:
        pass

    @abstractmethod
    def get_measure_by_station(self, station_id: str) -> List[Measure]:
        pass