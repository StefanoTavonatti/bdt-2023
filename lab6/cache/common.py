from abc import ABC, abstractmethod
from typing import Optional

from lab6.data_model.station import Station


class BasicStationCache(ABC):

    @abstractmethod
    def get(self, statiion_id: str) -> Optional[Station]:
        pass

    @abstractmethod
    def put(self, station: Station, ex: Optional[int] = None):
        pass