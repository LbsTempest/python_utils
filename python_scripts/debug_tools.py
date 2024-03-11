import traceback
from typing import Any, Callable


def traceback_call_stack(func: Callable) -> Callable:
    
    def wrapper(*args, **kwargs) -> Any:
        for frame in traceback.format_stack():
            print(frame.strip())

        return func(*args, **kwargs)

    return wrapper
