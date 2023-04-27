from datetime import datetime
from typing import List

import requests

from lab6.data_model.station import Station, Measure


class DatiBolzanoConnector:

    def _get_paginated_data(self, from_date: datetime, to_date: datetime, limit: str) -> List[dict]:
        """
        This method downloads data from the API in a paginated way.

        :param from_date:
        :param to_date:
        :param limit:
        :return:
        """
        offset = 0
        result = []
        while True:
            url = f"https://mobility.api.opendatahub.com/v2/flat%2Cnode/EnvironmentStation/%2A/{from_date.isoformat()}/{to_date.isoformat()}?limit={limit}&offset={offset}&shownull=false&distinct=true&timezone=UTC"

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            data_json = response.json()
            result += data_json["data"]
            if len(data_json["data"]) < int(limit):
                break
            offset += int(limit)

        return result

    def get_air_quality_data(self, from_date: datetime, to_date: datetime) -> List[Station]:

        measure_data = self._get_paginated_data(from_date, to_date, "200")
        print(f"Downloaded {len(measure_data)} measures")
        result = []

        grouped_measures = {}

        # grouping measures by station and time
        for raw_measure in measure_data:
            if raw_measure["scode"] not in grouped_measures:
                grouped_measures[raw_measure["scode"]] = {}
            if raw_measure["mvalidtime"] not in grouped_measures[raw_measure["scode"]]:
                grouped_measures[raw_measure["scode"]][raw_measure["mvalidtime"]] = []
            grouped_measures[raw_measure["scode"]][raw_measure["mvalidtime"]].append(raw_measure)

        for scode, measures_dict in grouped_measures.items():
            # get first measure
            first_measure = list(measures_dict.values())[0][0]

            station = self._deserialize_station(first_measure)
            for mvalidtime, measures in measures_dict.items():
                station.measurement.append(self._deserialize_measure(measures))
            result.append(station)

        return result

    def _deserialize_station(self, raw_measure: dict) -> Station:
        station_name = raw_measure["sname"]
        station = Station(station_name, "", "", [])

        return station

    def _deserialize_measure(self, raw_measures: list[dict]) -> Measure:
        first_datetime = raw_measures[0]["mvalidtime"]
        dt = datetime.strptime(first_datetime, "%Y-%m-%d %H:%M:%S.%f%z")
        measure = Measure(None, None, None, None, None, dt)

        for raw_measure in raw_measures:

            if first_datetime != raw_measure["mvalidtime"]:
                raise Exception("All measures should have the same mvalidtime")

            if raw_measure["tname"] == "NO2 - Ossidi di azoto":
                measure.no2_value = raw_measure["mvalue"]
            elif raw_measure["tname"] == "PM10 - Polveri sottili":
                measure.pm10_value = raw_measure["mvalue"]
            elif raw_measure["tname"] == "PM2.5 - Polveri sottili":
                measure.pm25_value = raw_measure["mvalue"]
            elif raw_measure["tname"] == "SO2 - Anidride solforosa":
                measure.so2_value = raw_measure["mvalue"]
            elif raw_measure["tname"] == "O3 - Ozono":
                measure.o3_value = raw_measure["mvalue"]

        return measure
