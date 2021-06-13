import os
from dotenv import load_dotenv

def load_config(env_prefiv):
    load_dotenv()

    return {
        'host': os.environ.get('{}DB_HOST'.format(env_prefiv)),
        'user': os.environ.get('{}DB_USERNAME'.format(env_prefiv)),
        'password': os.environ.get('{}DB_PASSWORD'.format(env_prefiv)),
        'port': os.environ.get('{}DB_PORT'.format(env_prefiv)),
        'dbname': os.environ.get('{}DB_NAME'.format(env_prefiv)),
        'minconn': os.environ.get('{}MIN_CONN'.format(env_prefiv)),
        'maxconn': os.environ.get('{}MAX_CONN'.format(env_prefiv))
    }
