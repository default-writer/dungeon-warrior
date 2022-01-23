import logging


logger = logging.getLogger(__name__)


def debugger(raise_exception=True):
    def decorator(function):
        def wrapper(*args, **kwargs):
            try:
                function(*args, **kwargs)
            except Exception as ex:
                logger.debug(ex)
                print(str(ex))
                if raise_exception:
                    raise ex
        return wrapper
    return decorator