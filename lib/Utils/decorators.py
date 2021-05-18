from functools import wraps
from sys import exit

def retry_on_value_error(function):
    @wraps(function)
    def wrapped_function(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ValueError as e:
            print('Blad: podano niepoprawna wartosc.')
            print('---   ' + str(e) + '\n')
            return wrapped_function(*args, **kwargs)
        except KeyboardInterrupt:
            print('Zamykanie programu...')
            exit(0)
    return wrapped_function