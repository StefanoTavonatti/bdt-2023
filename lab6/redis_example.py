import redis

conn = redis.Redis(host='localhost', port=6379, db=0)

conn.set("mykey", 2, ex=2)
print(conn.get("mykey").decode("utf-8"))
print(conn.lrange("myarray", 0, -1))