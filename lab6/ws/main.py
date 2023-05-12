from flask import Flask
from flask_restful import Api, Resource

from lab6.cache.redis_cache import RedisCache
from lab6.ws.resources.hello import HelloWorld
from lab6.ws.resources.station import StationResource, StationsResource

app = Flask("air_qulity")
api = Api(app)

cache = RedisCache("localhost", 6379, 0)

api.add_resource(HelloWorld, "/hello")
api.add_resource(StationResource, '/station/<string:station_id>', resource_class_kwargs={"cache": cache})
api.add_resource(StationsResource, '/stations', resource_class_kwargs={"cache": cache})

if __name__ == "__main__":
    app.run(debug=True)