import logging


logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.DEBUG)


def logging_teapot_status(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        try:
            logging.info('Status = %s' % result.status)
        except AttributeError:
            pass
        return result
    return wrapper
