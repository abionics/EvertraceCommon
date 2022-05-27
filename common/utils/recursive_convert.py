from typing import Any, Callable


def recursive_convert(data: Any, rule: Callable) -> Any:
    if isinstance(data, list):
        return [
            recursive_convert(value, rule)
            for value in data
        ]
    elif isinstance(data, dict):
        return {
            key: recursive_convert(value, rule)
            for key, value in data.items()
        }
    else:
        return rule(data)
