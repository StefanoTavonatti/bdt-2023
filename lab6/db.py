import sqlite3

conn = sqlite3.connect('lab6.db')
# cur = conn.cursor()

# cur.execute("CREATE TABLE station("
#             "name CHAR(250),"
#             "address CHAR(500),"
#             "city CHAR(500)"
#             ")")
name = "station3"

# res = cur.execute("INSERT INTO station(name) VALUES(?)", (name,))
# conn.commit()
# cur.close()
# conn.close()

# no new datas
# with conn:
#     conn.execute("INSERT INTO station(name) VALUES(?)", (name,))
#     raise Exception()

# cur = conn.cursor()
#
# res = cur.execute("SELECT name, address FROM station WHERE name=?", (name,))
# for station in res.fetchall():
#     print(station)

# with conn:
#     res = conn.execute("SELECT name, address FROM station WHERE name=?", (name,))
#     for station in res.fetchall():
#         print(station)

with conn:
    conn.execute("CREATE TABLE station("
                "ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name CHAR(250),"
                "address CHAR(500),"
                "city CHAR(500)"
                ")")

    conn.execute("CREATE TABLE measure("
                 "ID INTEGER PRIMARY KEY AUTOINCREMENT,"
                 "pm25 REAL,"
                 "pm10 REAL,"
                 "no2 REAL,"
                 "o3 REAL,"
                 "so2 REAL"
                 "dt DATETIME,"
                 "station_id INTEGER,"
                 "FOREIGN KEY (station_id) REFERENCES station(ID))" )