#!/usr/bin/env python3
"""
Redis basic exercise
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store inputs and outputs history"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


def replay(method: Callable) -> None:
    """Display the history of calls of a function"""
    r = redis.Redis()
    name = method.__qualname__

    calls = r.get(name)
    calls = int(calls.decode("utf-8")) if calls else 0

    print(f"{name} was called {calls} times:")

    inputs = r.lrange(f"{name}:inputs", 0, -1)
    outputs = r.lrange(f"{name}:outputs", 0, -1)

    for inp, out in zip(inputs, outputs):
        try:
            inp_str = inp.decode("utf-8")
        except Exception:
            inp_str = ""
        try:
            out_str = out.decode("utf-8")
        except Exception:
            out_str = ""
        print(f"{name}(*{inp_str}) -> {out_str}")


class Cache:
    """Cache class using Redis"""

    def __init__(self):
        """Initialize Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data and return key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float, None]:
        """Retrieve data and optionally convert it"""
        value = self._redis.get(key)

        if value is None:
            return None

        if fn:
            try:
                return fn(value)
            except Exception:
                raise ValueError("Conversion function failed.")

        return value

    def get_str(self, key: str) -> Optional[str]:
        """Get value as string"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Get value as integer"""
        return self.get(key, fn=lambda d: int(d))
