from typing import Any


def validate_name(name: Any) -> bool:
    return type(name) is str
