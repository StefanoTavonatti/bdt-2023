import redis

conn = redis.Redis(host='localhost', port=6379, db=0)

conn.publish("my-channel", "ciao")