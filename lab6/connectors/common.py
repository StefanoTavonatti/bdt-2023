from abc import ABC, abstractmethod


class BasicConnector(ABC):

    @abstractmethod
    def get_latest_air_quality_data(self):
        pass