from typing import Any

HOST: str = '127.0.0.1'
PORT: int = 11600
SEX: str = 'M'
DEBUG: bool = True
LOGGING: dict[str, Any] = {
    'version': 1,
    'disable_exsting_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        '__main__': {
            'handlers': ['file'],
            'level': 'DEBUG'
        },
        'responder': {
            'handlers': ['file'],
            'level': 'DEBUG'
        },
        'websockets': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
}
