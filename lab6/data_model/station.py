from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import List


class Station:

    def __init__(self, name: str, city: str, address: str, measurement: List[Measure]):
        self.address = address
        self.city = city
        self.name = name
        self.measurement = measurement

        if self.name == "":
            raise Exception

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

    pm10_value: float
    dt: datetime



