import redis

from settings import get_environment

env = get_environment()

redis_client = redis.Redis(host=env.REDIS_HOST, port=env.REDIS_PORT, password=env.REDIS_PASSWORD)
