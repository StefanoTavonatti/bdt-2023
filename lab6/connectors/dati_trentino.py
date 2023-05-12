from datetime import datetime
from typing import List

import requests

from lab6.connectors.common import BasicConnector
from lab6.data_model.station import Station, Measure


class DatiTrentinoConnector(BasicConnector):

    def get_latest_air_quality_data(self):
        return self.get_air_quality_data()

    def deserialize_station(self, raw_station: dict) -> Station:
        station = Station(
            station_id=f"trento-{raw_station['nome']}",
            name=raw_station['nome'],
            city=raw_station['citta'],
            address=raw_station['indirizzo'],
            measurement=[]
        )

        for raw_measure_date, raw_mesures in raw_station["dati"].items():
            for hour, raw_mesure in raw_mesures.items():
                try:
                    temp = f"{raw_measure_date} {hour}:00:00"
                    measure_date = datetime.fromisoformat(temp)
                    station.append_measure(Measure(
                        pm25_value=raw_mesure["pm25"],
                        pm10_value=raw_mesure["pm10"],
                        no2_value=raw_mesure["no2"],
                        so2_value=raw_mesure["so2"],
                        o3_value=raw_mesure["o3"],
                        dt=measure_date
                    ))
                except:
                    pass

        return station

    def get_air_quality_data(self) -> List[Station]:
        response = requests.get("https://bollettino.appa.tn.it/aria/opendata/json/last/")
        raw_data = response.json()

        result = []

        for raw_station in raw_data['stazione']:
            result.append(
                self.deserialize_station(raw_station)
            )

        return result

