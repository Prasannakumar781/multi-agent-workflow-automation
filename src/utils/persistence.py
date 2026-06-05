import os
from contextlib import contextmanager
from langgraph.checkpoint.redis import RedisSaver

@contextmanager
def get_checkpointer():
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    with RedisSaver.from_conn_string(redis_url) as checkpointer:
        yield checkpointer