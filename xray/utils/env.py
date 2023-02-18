import os


def get_env(key):
    v = os.getenv(key=key)
    if v is None:
        raise Exception('The environment %s does not exists.' % key)
    return v
