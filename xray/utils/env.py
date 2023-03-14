import os

from xray.exceptions import EnvNotExists


def get_env(key):
    _value = os.getenv(key=key)
    if _value is None:
        raise EnvNotExists(f'The environment {key} does not exists.')
    return _value
