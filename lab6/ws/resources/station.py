from flask import request
from flask_restful import Resource, fields, marshal_with, abort

from lab6.cache.common import BasicStationCache


resource_field = {
    "stationId": fields.String(attribute="station_id"),
    "name": fields.String,
    "measurement": fields.List(
        fields.Nested({
            "pm10": fields.Float(attribute="pm10_value")
        }
        )
    )
}

class StationResource(Resource):

    def __init__(self, cache: BasicStationCache):
        self._cache = cache

    @marshal_with(resource_field)
    def get(self, station_id: str):
        station = self._cache.get(station_id)
        return station

class StationsResource(Resource):

    def __init__(self, cache: BasicStationCache):
        self._cache = cache

    @marshal_with(resource_field)
    def get(self):
        if "name" in request.args:
            return "OK"
        else:
            abort(400, message="missing name query parms")