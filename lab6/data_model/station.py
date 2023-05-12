from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import List, Optional


class Station:

    def __init__(self, station_id: str, name: str, city: str, address: str, measurement: List[Measure]):
        self.station_id = station_id
        self.address = address
        self.city = city
        self.name = name
        self.measurement = measurement

        if self.name == "":
            raise Exception

    def to_repr(self) -> dict:
        return {
            "station_id": self.station_id,
            "address": self.address,
            "city": self.city,
            "name": self.name,
            "measurements": [x.to_repr() for x in self.measurement]
        }

    @staticmethod
    def from_repr(raw_data: dict) -> Station:
        return Station(
            station_id=raw_data["station_id"],
            name=raw_data["name"],
            address=raw_data["address"],
            city=raw_data["city"],
            measurement=[Measure.from_repr(x) for x in raw_data["measurements"]]
        )

    def append_measure(self, measure: Measure) -> None:
        self.measurement.append(measure)

    def __str__(self):
         return f"Name: {self.name}, adress: {self.address}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return other.name == self.name and self.address == other.address


@dataclasses.dataclass
class Measure:
    pm25_value:Optional[float]
    no2_value: Optional[float]
    o3_value: Optional[float]
    so2_value: Optional[float]
    pm10_value: Optional[float]
    dt: datetime

    def to_repr(self) -> dict:
        return {
            "pm_10": self.pm10_value,
            "pm25": self.pm25_value,
            "no2": self.no2_value,
            "o3": self.o3_value,
            "so2": self.so2_value,
            "dt": self.dt.isoformat()
        }

    @staticmethod
    def from_repr(raw_data: dict) -> Measure:
        return Measure(
            pm10_value=raw_data["pm_10"],
            pm25_value=raw_data["pm25"],
            no2_value=raw_data["no2"],
            o3_value=raw_data["o3"],
            so2_value=raw_data["so2"],
            dt=datetime.fromisoformat(raw_data["dt"])
        )

