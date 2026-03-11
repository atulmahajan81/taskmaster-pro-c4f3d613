import redis
from functools import wraps

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Decorator for caching with Redis
def cache_with_redis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = f'{func.__name__}:{args}:{kwargs}'
        result = redis_client.get(key)
        if result:
            return result
        result = func(*args, **kwargs)
        redis_client.setex(key, 300, result)  # Cache for 5 minutes
        return result
    return wrapper