import redis
from .config import settings

redis_client = redis.from_url(settings.REDIS_URL) if settings.REDIS_URL else None

def redis_set(key, value, ex=None):
    if redis_client:
        redis_client.set(key, value, ex)

def redis_get(key):
    return redis_client.get(key) if redis_client else None
