from datetime import datetime
from typing import List

import requests

from lab6.data_model.station import Station, Measure


class DatiBolzanoConnector:
    def get_air_quality_data(self, from_date: datetime, to_date: datetime) -> List[Station]:
        url = f"https://mobility.api.opendatahub.com/v2/flat%2Cnode/EnvironmentStation/%2A/{from_date.isoformat()}/{to_date.isoformat()}?limit=200&offset=0&shownull=false&distinct=true&timezone=UTC"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        data_json = response.json()
        measure_data = data_json["data"]
        result = []

        for station_measures in measure_data:
            station = self.deserialize_station(station_measures)
            result.append(station)

        return result

    def deserialize_station(self, raw_measure: dict) -> Station:
        print(raw_measure)
        station_name = raw_measure["sname"]
        station = Station(station_name, "", "", [])
        dt = datetime.strptime(raw_measure["mvalidtime"], "%Y-%m-%d %H:%M:%S.%f%z")
        measure = Measure(None, None, None, None, None, dt)
        if raw_measure["tname"] == "NO2 - Ossidi di azoto":
            measure.no2_value = raw_measure["mvalue"]
        elif raw_measure["tname"] == "PM10 - Polveri sottili":
            measure.pm10_value = raw_measure["mvalue"]
        elif raw_measure["tname"] == "PM2.5 - Polveri sottili":
            measure.pm25_value = raw_measure["mvalue"]

        station.append_measure(measure)

        return station