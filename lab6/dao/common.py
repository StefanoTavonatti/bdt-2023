from abc import ABC, abstractmethod

from lab6.data_model.station import Station


class BasicDao(ABC):

    @abstractmethod
    def save_station(self, station: Station) -> None:
        pass