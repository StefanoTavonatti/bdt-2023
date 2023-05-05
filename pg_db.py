import psycopg2

conn = psycopg2.connect("host=127.0.0.1 dbname=bdt user=postgres password=postgres")
# cur = conn.cursor()
#
# cur.execute("CREATE TABLE station("
#                 "ID CHAR(250) PRIMARY KEY,"
#                 "name CHAR(250),"
#                 "address CHAR(500),"
#                 "city CHAR(500)"
#                 ")")
# conn.commit()
# cur.close()
# conn.close()

with conn:
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE measure("
                 "ID SERIAL PRIMARY KEY,"
                 "pm25 REAL,"
                 "pm10 REAL,"
                 "no2 REAL,"
                 "o3 REAL,"
                 "so2 REAL,"
                 "station_id CHAR(250),"
                 "FOREIGN KEY (station_id) REFERENCES station(ID))" )
