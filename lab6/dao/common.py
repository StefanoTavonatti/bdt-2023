from abc import ABC, abstractmethod
from typing import List

from lab6.data_model.station import Station


class BasicDao(ABC):

    @abstractmethod
    def save_station(self, station: Station) -> None:
        pass

    @abstractmethod
    def update_station(self, station: Station) -> None:
        pass

    @abstractmethod
    def get_station(self, station_id: int) -> Station:
        pass

    @abstractmethod
    def get_station_by_name(self, name: str) -> List[Station]:
        pass