import redis

conn = redis.Redis(host='localhost', port=6379, db=0)

pubsub = conn.pubsub()

pubsub.subscribe("my-channel")

while True:
    message = pubsub.get_message()
    if message:
        print(message)