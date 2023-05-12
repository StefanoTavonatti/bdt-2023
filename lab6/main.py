from datetime import datetime
import time

from lab6.cache.redis_cache import RedisCache
from lab6.connectors.dati_trentino import DatiTrentinoConnector
from lab6.connectors.dati_bolzano import DatiBolzanoConnector
from lab6.dao.common import NotExist
from lab6.dao.file_dao import FileDao
from lab6.dao.pg_dao import PgDao
from lab6.dao.sqlite_dao import SQLiteDao
from lab6.manager import AirQualityManager

connector_trento = DatiTrentinoConnector()
connector_bolzano =DatiBolzanoConnector()

dao = SQLiteDao("lab6.db")

cache = RedisCache("localhost", 6379, 0)

manager = AirQualityManager(
    bolzano_connector=connector_bolzano,
    trento_connector=connector_trento,
    dao=dao,
    cache=cache
)


if __name__ == "__main__":
    while True:
        print("start computation")
        manager.start_computation()
        print("sleep for 10 seconds")
        time.sleep(10)
